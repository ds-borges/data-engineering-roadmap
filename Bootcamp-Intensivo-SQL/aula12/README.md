# Estrutura de Dados, Indexação e Big Tree

Este documento reúne anotações sobre **estruturas de dados**, **indexação** e o funcionamento de **índices no PostgreSQL**.

---

## Conceito Básico

> **Quanto mais fácil é inserir dados em uma estrutura, mais difícil é selecioná-los.**

Isso ocorre porque estruturas otimizadas para inserção priorizam velocidade na escrita, enquanto estruturas otimizadas para leitura, como árvores balanceadas (B+ Tree), demandam mais processamento na inserção.

---

## Indexação no PostgreSQL

Quando um banco de dados é criado, o PostgreSQL automaticamente cria tabelas de índices relacionados às tabelas principais por meio da primary-key.  
À medida que novos registros são inseridos, mais índices são gerados para otimizar consultas.

### Observações Importantes

- O operador `LIKE` **não utiliza índice** em buscas com caracteres variáveis, por exemplo:  
```sql
SELECT * FROM pessoas WHERE nome LIKE 'c%'; -- Não usa índice
```

- Entretanto, o `LIKE` com correspondência exata **pode usar** índice:  

```sql
SELECT * FROM pessoas WHERE nome LIKE 'cc'; -- Usa índice
```

- O uso de índices **aumenta o consumo de espaço** — pode até **triplicar** o tamanho necessário de armazenamento.

- Índices são mais úteis em colunas usadas com **ORDER BY** e **WHERE**.

---

## Exemplo de Criação de Tabela e Índice

### Criando uma tabela com UUID

```sql
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE pessoas (
id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
first_name VARCHAR(3),
last_name VARCHAR(3)
);
```

### Verificando índices existentes

```sql
SELECT
tablename AS "Tabela",
indexname AS "Índice",
indexdef AS "Definição do Índice"
FROM
pg_indexes
WHERE
tablename = 'pessoas';
```

Observação: a criação de índices utilizando chaves do tipo UUID demanda mais tempo em comparação com chaves do tipo serial, devido ao maior tamanho e complexidade dos valores UUID.

Para os testes realizados, optou-se pelo uso de chaves serial.

---

## Teste de Performance: com e sem Índice

### 1. Criando tabela

```sql
CREATE TABLE pessoas (
id SERIAL PRIMARY KEY,
first_name VARCHAR(3),
last_name VARCHAR(3)
);
```

### 2. Criando índice

```sql
CREATE INDEX first_name_index ON pessoas(first_name);
```

### 3. Inserindo 1 milhão de registros aleatórios

```sql
INSERT INTO pessoas (first_name, last_name)
SELECT
substring(md5(random()::text), 0, 3),
substring(md5(random()::text), 0, 3)
FROM
generate_series(1, 1000000);
```

### 4. Resultados de inserção

| Situação | Tempo de Inserção | Resultado |
|-----------|------------------|------------|
| Com o índice criado antes da inserção | 7.49 s | `INSERT 0 1000000` |
| Sem o índice criado antes da inserção | 4.17 s | `INSERT 0 1000000` |

➡️ **Com índice, a inserção foi ~79% mais lenta.**

---

## Tamanho dos Dados

### Verificando tamanho da coluna `first_name`

```sql
SELECT pg_size_pretty(SUM(pg_column_size(first_name))::bigint) AS tamanho_total
FROM pessoas;
```

**Resultado:** 2930 kB

### Verificando tamanho do índice `first_name_index`

```sql
SELECT pg_size_pretty(pg_relation_size('first_name_index'));
```

**Resultado:** 6912 kB

➡️ **O índice ocupou mais que o dobro do espaço da coluna.**

---

## Efeito na Busca

### Com índice

```sql
SELECT * FROM pessoas WHERE id = 100;
```

**Tempo:** 0.105 s

### Sem índice

```sql
SELECT * FROM pessoas WHERE last_name LIKE 'd%';
```

**Tempo:** 0.170 s

➡️ **O índice reduziu o tempo de busca em 38,24%.**

---

## Conclusões

- Índices melhoram significativamente a **velocidade de leitura**, mas:
  - Aumentam o **tempo de escrita** (inserção).
  - Consomem **mais espaço em disco**.
- Devem ser usados **estrategicamente**, apenas em colunas que participam frequentemente de buscas e ordenações.
