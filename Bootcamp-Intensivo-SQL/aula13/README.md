# Indexação e Particionamento em Banco de Dados

Este documento reúne anotações sobre técnicas de otimização de performance em bancos de dados PostgreSQL, focando em Índices B-Tree e Particionamento de Tabelas (List e Range).

Para os testes, criamos uma tabela de pessoas e uma função para gerar dados aleatórios em massa (10 milhões de registros).

```sql
-- Criação da tabela base
CREATE TABLE pessoas (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(3),
    last_name VARCHAR(3),
    estado VARCHAR(3)
);

-- Função para gerar estados aleatórios
CREATE OR REPLACE FUNCTION random_estado()
RETURNS VARCHAR(3) AS $$
BEGIN
   RETURN CASE floor(random() * 5)
         WHEN 0 THEN 'SP'
         WHEN 1 THEN 'RJ'
         WHEN 2 THEN 'MG'
         WHEN 3 THEN 'ES'
         ELSE 'DF'
         END;
END;
$$ LANGUAGE plpgsql;

-- Inserção massiva (10 milhões de registros)
INSERT INTO pessoas (first_name, last_name, estado)
SELECT
   substring(md5(random()::text), 0, 3),
   substring(md5(random()::text), 0, 3),
   random_estado()
FROM
   generate_series(1, 10000000);

```

## 1. Índices (Indexação)
Os índices são estruturas de dados que permitem localizar registros rapidamente sem a necessidade de percorrer toda a tabela (Sequential Scan).

Criação do Índice
```sql
CREATE INDEX first_name_index ON pessoas(first_name);
```
### Comparativo de Desempenho

Abaixo, a diferença de tempo entre uma consulta em coluna indexada (first_name) vs. coluna não indexada (last_name):

| Tipo de Consulta | Query                                                | Tempo de Execução |
| ---------------- | ---------------------------------------------------- | ----------------- |
| Com Índice       | SELECT COUNT(first_name) ... WHERE first_name = 'aa' | 0.127s            |
| Sem Índice       | SELECT COUNT(last_name) ... WHERE last_name = 'aa'   | 0.408s            |

O índice reduz o tempo de busca, pois o PostgreSQL utiliza a estrutura B-Tree para localizar registros diretamente, sem precisar percorrer todas as linhas da tabela (*Sequential Scan*).  

> **Observação sobre Processamento Paralelo**  
> O PostgreSQL pode otimizar consultas sem índice usando **execução paralela**, dividindo o trabalho entre múltiplas “threads” de processamento.  
> Na prática, isso faz com que uma varredura sequencial em uma tabela muito grande seja distribuída entre vários workers, reduzindo o tempo total da consulta.

## 2. Particionamento
O particionamento divide uma tabela logicamente grande em partes físicas menores, melhorando a manutenção e a performance de busca (Partition Pruning).

A. Particionamento por Lista (LIST)
Ideal para colunas com valores discretos e definidos, como Estados ou Categorias.

```sql
CREATE TABLE pessoas_partition_estado (
    id SERIAL,
    first_name VARCHAR(3),
    last_name VARCHAR(3),
    estado VARCHAR(3),
    PRIMARY KEY (id, estado)
) PARTITION BY LIST (estado);

-- Criando as partições específicas
CREATE TABLE pessoas_sp PARTITION OF pessoas_partition_estado FOR VALUES IN ('SP');
CREATE TABLE pessoas_rj PARTITION OF pessoas_partition_estado FOR VALUES IN ('RJ');
CREATE TABLE pessoas_mg PARTITION OF pessoas_partition_estado FOR VALUES IN ('MG');
CREATE TABLE pessoas_es PARTITION OF pessoas_partition_estado FOR VALUES IN ('ES');
CREATE TABLE pessoas_df PARTITION OF pessoas_partition_estado FOR VALUES IN ('DF');
```

### Comparativo de desempenho

Foram comparadas duas consultas semelhantes: uma executada em tabela **particionada por estado** e outra em tabela **sem particionamento**.

| Tipo de Consulta | Query | Tempo de Execução |
|------------------|--------|-------------------|
| **Com Partição** | `SELECT COUNT(estado) FROM pessoas_partition_estado WHERE estado = 'RJ';` | **0.195s** |
| **Sem Partição** | `SELECT COUNT(estado) FROM pessoas WHERE estado = 'RJ';` | **1.060s** |



B. Particionamento por Intervalo (RANGE)
Comumente utilizado para datas ou IDs sequenciais.

```sql
CREATE TABLE pessoas_partition_id (
    id SERIAL,
    first_name VARCHAR(3),
    last_name VARCHAR(3),
    estado VARCHAR(3),
    PRIMARY KEY (id)
) PARTITION BY RANGE (id);

-- Definição dos intervalos
CREATE TABLE pessoas_part1 PARTITION OF pessoas_partition_id FOR VALUES FROM (MINVALUE) TO (2000001);
CREATE TABLE pessoas_part2 PARTITION OF pessoas_partition_id FOR VALUES FROM (2000001) TO (4000001);
CREATE TABLE pessoas_part3 PARTITION OF pessoas_partition_id FOR VALUES FROM (4000001) TO (6000001);
CREATE TABLE pessoas_part4 PARTITION OF pessoas_partition_id FOR VALUES FROM (6000001) TO (8000001);
CREATE TABLE pessoas_part5 PARTITION OF pessoas_partition_id FOR VALUES FROM (8000001) TO (MAXVALUE);
```

### Considerações Finais
O Problema do Particionamento por ID
Embora o particionamento por ID (Range) seja útil para organizar dados históricos, ele apresenta um desafio de escalabilidade:

Inflação da última partição: Como os IDs são sequenciais e crescentes, todos os novos registros serão inseridos na última partição configurada.

Manutenção: Requer a criação constante de novas partições para evitar que uma única tabela se torne um "gargalo", perdendo o benefício da divisão de dados.
