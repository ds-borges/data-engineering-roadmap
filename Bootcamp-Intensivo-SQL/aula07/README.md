# Aula 07 – Controle de Clientes e Transações no PostgreSQL

Este passo a passo demonstra como criar e manipular tabelas, inserir dados, realizar transações, proteger restrições e utilizar um ambiente Docker com PostgreSQL e pgAdmin.

---

## Ambiente Docker para o Projeto

O projeto utiliza Docker Compose para provisionar o banco de dados PostgreSQL e o pgAdmin como interface administrativa.

### Requisitos

- Docker e Docker Compose instalados
- O arquivo docker-compose.yml na raiz do projeto
- Um diretório local chamado `files` para mapeamento de arquivos

### Configuração dos Serviços

```docker
version: '3'

services:
  db:
    container_name: aula07_db
    image: postgres:latest
    environment:
      POSTGRES_DB: jornada_aula07
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    volumes:
      - postgresql_bin:/usr/lib/postgresql
      - postgresql_data:/var/lib/postgresql/data
      - ./files:/files
    ports:
      - 55596:5432
    networks:
      - mynetdocker

  pgadmin:
    container_name: aula07_pgadmin
    image: dpage/pgadmin4
    environment:
      PGADMIN_DEFAULT_EMAIL: pgadmin4@pgadmin.org
      PGADMIN_DEFAULT_PASSWORD: postgres
      PGADMIN_LISTEN_PORT: 5050
      PGADMIN_CONFIG_SERVER_MODE: 'False'
    volumes:
      - postgresql_bin:/usr/lib/postgresql
      - pgadmin_root_prefs:/root/.pgadmin
      - pgadmin_working_dir:/var/lib/pgadmin
      - ./files:/files
    ports:
      - 5050:5050
    networks:
      - mynetdocker

networks:
  mynetdocker:
    driver: bridge

volumes:
  pgadmin_root_prefs:
    driver: local
  pgadmin_working_dir:
    driver: local
  postgresql_data:
    driver: local
  postgresql_bin:
    driver: local

```

### Inicialização

Para subir os serviços, execute:

```bash
docker compose up -d
```

- O pgAdmin ficará acessível via navegador em `http://localhost:5050`
- Login padrão:
  - Email: `pgadmin4@pgadmin.org`
  - Senha: `postgres`

---

## 💻 Acesso e Conexão

### 1. Acessando o pgAdmin

O pgAdmin estará disponível em seu navegador na porta **5050**.
```
| Detalhe         | Valor                         |
|:----------------|:------------------------------|
| URL             | http://localhost:5050         |
| Email de Login  | pgadmin4@pgadmin.org          |
| Senha           | postgres                      |
```

---

### 2. Registrando o Servidor PostgreSQL

Após logar no pgAdmin, clique em **Add New Server** e siga as instruções abaixo para conectar com o banco da aula:

#### Aba General
```
Name: aula07 (ou outro nome de sua preferência)
```

#### Aba Connection

```
Host name/address: db # nome do serviço definido no docker-compose.yml
Port: 5432
Username: postgres
Password: postgres
Maintenance database: postgres
```

Após salvar, você poderá acessar o banco de dados **jornada_aula07** (com o seu esquema já carregado) na árvore de servidores do pgAdmin.

---

## 1. Criação das Tabelas

```sql

CREATE TABLE IF NOT EXISTS transactions (
id SERIAL PRIMARY KEY NOT NULL,
tipo CHAR(1) NOT NULL,
descricao VARCHAR(10) NOT NULL,
valor INTEGER NOT NULL,
cliente_id INTEGER NOT NULL,
realizada_em TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS clients (
id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
limite INTEGER NOT NULL,
saldo INTEGER NOT NULL
);
```

---

## 2. Inserindo Clientes

```sql
INSERT INTO clients (limite, saldo)
VALUES
(10000, 0),
(80000, 0),
(1000000, 0),
(10000000, 0),
(500000, 0);
```

**Exemplo de resultado:**

| id                                      | limite   | saldo  |
|------------------------------------------|----------|--------|
| f5ad9da1-ed0d-4d6e-a58c-883c24dbea5a    | 10000    | 0      |
| 7ea94eac-069f-4d44-8986-9336b64afa52    | 80000    | 0      |
| 0bf915b8-ac03-4ffc-9204-c6a9a3f04021    | 1000000  | 0      |
| 63a9ae14-3e4b-44f9-8616-764bb73e616e    | 10000000 | 0      |
| d58b0614-0fda-4065-8af2-e3f748452bd2    | 500000   | 0      |

---

## 3. Exemplo – Comprando um Carro para o Cliente 1

```sql
-- Criando transação de compra
INSERT INTO transactions (tipo, descricao, valor, cliente_id)
VALUES ('d', 'car buyed', 80000, 1);

-- Atualizando saldo do cliente 1 (substitua o id pelo correto)
UPDATE clients
SET saldo = saldo + CASE WHEN 'd' = 'd' THEN -80000 ELSE 80000 END
WHERE id = 'f5ad9da1-ed0d-4d6e-a58c-883c24dbea5a';
```

**Verificando resultado:**

```sql
SELECT * FROM clients;
```

| id                                      | limite   | saldo  |
|------------------------------------------|----------|--------|
| 7ea94eac-069f-4d44-8986-9336b64afa52    | 80000    | 0      |
| 0bf915b8-ac03-4ffc-9204-c6a9a3f04021    | 1000000  | 0      |
| 63a9ae14-3e4b-44f9-8616-764bb73e616e    | 10000000 | 0      |
| d58b0614-0fda-4065-8af2-e3f748452bd2    | 500000   | 0      |
| f5ad9da1-ed0d-4d6e-a58c-883c24dbea5a    | 10000    | -80000 |

---

## 4. Garantindo Restrições – Saldo Não Negativo

```sql
-- Apagar tabela se necessário
DROP TABLE clients;

-- Apagar transações antigas do cliente (opcional)
DELETE FROM transactions WHERE id = 1;

-- Criar tabela clients com restrição de saldo
CREATE TABLE IF NOT EXISTS clients (
id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
limite INTEGER NOT NULL,
saldo INTEGER NOT NULL,
CHECK (saldo >= -limite),
CHECK (limite >= 0)
);
```

---

## 5. Inserindo Novos Clientes

```sql
INSERT INTO clients (limite, saldo)
VALUES
(10000, 0),
(80000, 0),
(1000000, 0),
(10000000, 0),
(500000, 0);
```

Novos UUIDs serão gerados.

```
"fbca0a69-3858-457a-88f9-0a20bdad36e1"  10000   0
"33424a77-ad33-4f06-9cca-b9e10ca63098"  80000   0
"69f67e8a-e74f-4040-8598-11ceb7cad9ec"  1000000 0
"2f44ce00-5189-4abe-8936-a166233cd726"  10000000    0
"b70c8e49-2f9f-4fb9-b989-086de23a87b9"  500000  0
```

---

## 6. Testando Restrições de Saldo

```sql
UPDATE clients
SET saldo = saldo -80000
WHERE id = 'fbca0a69-3858-457a-88f9-0a20bdad36e1';
```

**Retorno esperado:**

```
ERROR: new row for relation "clients" violates check constraint "clients_check"
SQL state: 23514
Detail: Failing row contains (fbca0a69-3858-457a-88f9-0a20bdad36e1, 10000, -80000).
```

---

## Observações

- Substitua os UUIDs conforme o retorno do seu banco.
- Essas queries exemplificam controle de saldo e restrições essenciais em sistemas de dados transacionais (bancários/financeiros).
- Adapte as operações conforme o seu fluxo de estudos.

---
