# 🐘 Ambiente PostgreSQL + pgAdmin com Docker (Northwind Schema)

## 🚀 Visão Geral

Este projeto simplifica a configuração de um ambiente de banco de dados robusto, provisionando o **PostgreSQL** e a interface de gerenciamento **pgAdmin 4** utilizando **Docker Compose**.

Um diferencial importante é a **carga automática do esquema Northwind**: o banco de dados é implantado na inicialização do serviço `db` a partir do arquivo `northwind.sql`, permitindo que você comece a trabalhar imediatamente com um *dataset* de exemplo.

> **⚠️ Observação Importante:** O pgAdmin não descobre servidores automaticamente. Após subir os contêineres, será necessário **registrar manualmente a conexão** com o servidor PostgreSQL dentro da interface do pgAdmin. O passo a passo para configurar o servidor encontra-se ao final deste README.

---

## 📋 Pré-requisitos

Para executar este projeto, você precisa ter:

1.  **Docker** e **Docker Compose** instalados.
2.  O arquivo **`northwind.sql`** na raiz do projeto (junto ao `docker-compose.yml`).
3.  Um diretório local chamado **`files`** (mapeado nos volumes de ambos os serviços).

---

## 🛠️ Arquivos de Configuração

### `docker-compose.yml`

Este arquivo define os serviços `db` (PostgreSQL) e `pgadmin`, a rede `db` e os volumes para persistência de dados.

```bash
version: '3'

services:
  db:
    container_name: db
    image: postgres:latest
    environment:
      POSTGRES_DB: northwind
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: postgres
    volumes:
      - postgresql_bin:/usr/lib/postgresql
      - postgresql_data:/var/lib/postgresql/data
      - ./northwind.sql:/docker-entrypoint-initdb.d/northwind.sql
      - ./files:/files
    ports:
      - 55596:5432
    networks:
      - db

  pgadmin:
    container_name: pgadmin
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
      - db

networks:
  db:
    driver: bridge

volumes:
  pgadmin_root_prefs:
    driver: local
  pgadmin_working_dir:
    driver: local
  postgresql_data:
    driver: local
  postgresql_bin:
    driver: local**
```

### `northwind.sql`

Este script realiza a criação e configuração das tabelas para o banco de dados, realizando ainda a inserção de dados fictícios na tabela Northwind.

---

## ▶️ Uso e Inicialização

Para iniciar o ambiente, navegue até a pasta do projeto e execute o comando:

```bash
docker compose up -d
```

💻 Acesso e Conexão
1. Acessando o pgAdmin
O pgAdmin estará disponível em seu navegador na porta 5050.


|Detalhe        | Valor                     |
|:---           |:---                       |
|URL            |	http://localhost:5050   |
|Email de Login |	pgadmin4@pgadmin.org    |
|Senha          |	postgres                |

2. Registrando o Servidor PostgreSQL
Após logar no pgAdmin, clique em Add New Server e siga as instruções para configurar a conexão com o banco de dados:


## Aba General
```
Name: Northwind (ou um nome de sua preferência)
```

## Aba Connection
```
Host name/address: db (Este é o nome do serviço no Docker Compose)

Port: 5432

Username: postgres

Password: postgres

Maintenance database: postgres (O banco de dados padrão do usuário postgres)

Após salvar, você poderá acessar o banco de dados northwind (que já terá o esquema carregado) na árvore de servidores.
```
