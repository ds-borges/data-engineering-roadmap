# Projetos de Banco de Dados: Triggers, Procedures e Materialized Views

Esta pagina contém dois projetos práticos em SQL (PostgreSQL) que demonstram o uso de:
1.  **Gatilhos (Triggers)** para atualização automática de uma **Visão Materializada (Materialized View)**.
2.  **Gatilhos (Triggers)** para auditoria de dados e o uso de **Procedimentos (Procedures)** para encapsular lógica de negócio.

---

## Projeto 1: Atualização Automática de Visão Materializada de Vendas

Este projeto implementa um mecanismo para manter uma visão materializada de vendas (`sales_accumulated_monthly_mv`) sempre atualizada. A visão resume o total de vendas mensais.

**Objetivo:** Garantir que qualquer alteração (INSERT, UPDATE, DELETE) nas tabelas `orders` ou `order_details` dispare automaticamente a atualização da visão materializada, para que os relatórios de vendas estejam sempre corretos.

### 📜 Componentes SQL

#### 1. Visão Materializada (View)
A `sales_accumulated_monthly_mv` agrupa o total de vendas por ano e mês.

```sql
CREATE MATERIALIZED VIEW sales_accumulated_monthly_mv as
(
    SELECT
        EXTRACT(YEAR FROM o.order_date) as ano,
        EXTRACT(MONTH FROM o.order_date) as mes,
        SUM((od.quantity*od.unit_price) * (1 - od.discount)) as total_mensal
    from orders o join order_details od ON od.order_id = o.order_id
    GROUP BY 1,2
    order by 1,2
);
```

#### 2. Função de Gatilho (Trigger Function)
A função refresh_materialized_view_sales_acumulaed contém a lógica para atualizar a view
```sql
CREATE OR REPLACE FUNCTION refresh_materialized_view_sales_acumulaed()
returns trigger as
$$
BEGIN
	REFRESH MATERIALIZED VIEW sales_accumulated_monthly_mv;
	RETURN NULL;
END;
$$ language plpgsql;
```

#### 3. Gatilhos (Triggers)
Dois gatilhos são criados, um para cada tabela, para chamar a função acima após qualquer modificação.

```sql
-- Gatilho na tabela 'orders'
CREATE OR REPLACE TRIGGER refresh_materialized_sales_orders
AFTER INSERT OR UPDATE OR DELETE ON orders
FOR EACH STATEMENT
EXECUTE FUNCTION refresh_materialized_view_sales_acumulaed();

```

```sql
-- Gatilho na tabela 'order_details'
CREATE OR REPLACE TRIGGER refresh_materialized_sales_orders_details
AFTER INSERT OR UPDATE OR DELETE ON order_details
FOR EACH STATEMENT
EXECUTE FUNCTION refresh_materialized_view_sales_acumulaed();
```

Como Funciona
* Um novo pedido é inserido na tabela orders e seus itens em order_details.
* Assim que a transação é concluída, o gatilho (em orders ou order_details) é disparado.
* O gatilho executa a função refresh_materialized_view_sales_acumulaed.
* A função executa o comando REFRESH MATERIALIZED VIEW, que recalcula e atualiza os dados da sales_accumulated_monthly_mv.

## Projeto 2: Auditoria de Mudanças de Cargo com Procedure
Este projeto cria um sistema de auditoria que rastreia todas as alterações no campo title (cargo) da tabela employees. Ele também fornece um procedimento armazenado (employee_update) para facilitar a atualização de cargos, garantindo que a lógica de negócio seja centralizada.

Objetivo: Manter um histórico de promoções ou mudanças de cargo de funcionários, registrando o cargo antigo e o novo na tabela employee_audit.

📜 Componentes SQL
1. Tabela de Auditoria
A tabela employee_audit armazena o histórico das mudanças.

```sql
CREATE TABLE employee_audit (
    employee_id INT,
    old_title VARCHAR,
    new_title VARCHAR,
    data_de_modificacao_do_salario TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```
#### 2. Função de Gatilho (Trigger Function)
A função registrar_auditoria_titulo é responsável por pegar os valores antigo (OLD.title) e novo (NEW.title) e inseri-los na tabela de auditoria.

```sql
CREATE OR REPLACE FUNCTION registrar_auditoria_titulo() returns trigger as
$$
BEGIN
	insert into employee_audit (employee_id, old_title, new_title)
	values (old.employee_id, old.title, new.title);
    RETURN NEW;
END;
$$ A_LANGUAGE plpgsql;
```

#### 3. Gatilho (Trigger)
O gatilho trg_title_modificaded é acionado após uma atualização (AFTER UPDATE) no campo title da tabela employees, executando a função para cada linha modificada.

```sql
CREATE TRIGGER trg_title_modificaded
AFTER UPDATE OF title ON employees
FOR EACH ROW
EXECUTE FUNCTION registrar_auditoria_titulo();
```

#### 4. Procedimento Armazenado (Stored Procedure)
O procedimento employee_update simplifica a forma como o DBA ou a aplicação atualiza o cargo de um funcionário.

```sql
CREATE OR REPLACE PROCEDURE employee_update(
	IN p_employee_id INTEGER,
	IN p_title VARCHAR
)
LANGUAGE plpgsql
as $$
BEGIN
    update employees
	set title = p_title
	where employee_id = p_employee_id;
END;
$$;
```

##Exemplo de Uso
#### 1. Inserir um funcionário (opcional, para teste):

```sql
INSERT INTO employees VALUES (10, 'denis', 'diniz', 'estagiario','Dr.','1998-12-12', '1992-08-14', '908 W. Capital Way', 'Tacoma', 'WA', '98401', 'USA', '(206) 555-9482', '3457', '\x', '...', NULL, '...');
```

#### 2. Atualizar o cargo usando o Procedimento: Em vez de um UPDATE manual, chamamos a `PROCEDURE`.

```sql
CALL employee_update(10, 'Senior');
```

#### 3. Verificar a Auditoria: Após a execução do CALL, o gatilho terá sido disparado automaticamente.

```sql
SELECT * FROM employee_audit;
```

#### 4. Resultado esperado

| employee_id | old_title | new_title | data_de_modificacao_do_salario |
| :--- | :--- | :--- | :--- |
| 10 | estagiario | Senior | 2025-11-16 14:30:00 |
