# Aula sobre `TRIGGER` e `FUNCTION` em Banco de Dados

Este repositório contém o material de uma aula prática demonstrando a criação e o uso de **Triggers** e **Functions** em um banco de dados (assumindo PostgreSQL devido ao uso de `SERIAL` e `plpgsql`).

## Conceitos Chave

Um **Trigger** (Gatilho) é um procedimento armazenado no banco de dados que é **executado automaticamente** em resposta a um evento específico em uma tabela.

* **Finalidade Principal:** Lidar com eventos importantes e evitar **inconsistências** no Banco de Dados.
* **Eventos de Acionamento:** Pode ser acionado em eventos como `INSERT`, `UPDATE`, e `DELETE`.

Para que o Trigger funcione, ele geralmente precisa invocar uma **Function** (Função) que contém a lógica a ser executada.

## 🛠️ Configuração Inicial

Para replicar o exemplo, você precisará criar duas tabelas: `Funcionario` e `Funcionario_Auditoria`.

### 1. Criação das Tabelas

```sql
-- Criação da tabela principal
CREATE TABLE Funcionario (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    salario DECIMAL(10, 2),
    dtcontratacao DATE
);

-- Criação da tabela de auditoria para registrar mudanças de salário
CREATE TABLE Funcionario_Auditoria (
    id INT,
    salario_antigo DECIMAL(10, 2),
    novo_salario DECIMAL(10, 2),
    data_de_modificacao_do_salario TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id) REFERENCES Funcionario(id)
);
```

### 2. Inserção de Dados de Teste

```sql
INSERT INTO Funcionario (nome, salario, dtcontratacao) VALUES ('Maria', 5000.00, '2021-06-01');
INSERT INTO Funcionario (nome, salario, dtcontratacao) VALUES ('João', 4500.00, '2021-07-15');
INSERT INTO Funcionario (nome, salario, dtcontratacao) VALUES ('Ana', 4000.00, '2022-01-10');
INSERT INTO Funcionario (nome, salario, dtcontratacao) VALUES ('Pedro', 5500.00, '2022-03-20');
INSERT INTO Funcionario (nome, salario, dtcontratacao) VALUES ('Lucas', 4700.00, '2022-05-25');
```

## Implementação do Trigger
Este exemplo demonstra a criação de uma rotina de auditoria de salário, onde qualquer alteração no campo salario da tabela Funcionario é registrada na tabela Funcionario_Auditoria.

### 1. Criação da Função (Function)
A função é o procedimento que será executado pelo trigger. Ela registra o valor antigo (OLD.salario) e o novo valor (NEW.salario) na tabela de auditoria.

```sql
CREATE OR REPLACE FUNCTION registrar_auditoria_salario() returns trigger as
$$
BEGIN
    -- Insere o registro de auditoria.
    -- OLD.id, OLD.salario (antes da atualização) e NEW.salario (depois da atualização)
    insert into Funcionario_Auditoria (id, salario_antigo, novo_salario)
    values (old.id, old.salario, new.salario);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```
### 2. Criação do Gatilho (Trigger)
O gatilho associa a função registrar_auditoria_salario à tabela Funcionario.

* AFTER UPDATE OF salario ON Funcionario: O gatilho só será ativado após uma operação de UPDATE na coluna salario da tabela Funcionario.

* FOR EACH ROW: A função será executada para cada linha afetada pelo UPDATE.

```sql
CREATE TRIGGER trg_salario_modificado
AFTER UPDATE OF salario ON Funcionario
FOR EACH ROW
EXECUTE FUNCTION registrar_auditoria_salario();
```

## Teste
Para testar o funcionamento, execute uma atualização no salário de um funcionário e, em seguida, verifique o conteúdo da tabela de auditoria.

```sql
-- Exemplo de uso: Atualizando o salário da Maria
UPDATE Funcionario
SET salario = 5200.00
WHERE nome = 'Maria';

-- Verifique a tabela de auditoria
SELECT * FROM Funcionario_Auditoria;
```

O SELECT na tabela Funcionario_Auditoria deve retornar um novo registro indicando que o salário do id correspondente foi alterado de 5000.00 para 5200.00.
