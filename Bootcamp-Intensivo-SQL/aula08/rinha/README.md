# Desafio: Stored Procedure de Extrato Bancário

Esta pasta contém a solução para um desafio de banco de dados focado na criação de uma *stored procedure* para consulta de extrato bancário. A procedure, intitulada `ver_extrato`, fornece uma visão detalhada da situação financeira de um cliente, incluindo seu saldo atual e o histórico de transações recentes.

**Nota Importante:** Esta solução depende do ambiente Docker configurado pelo arquivo `docker-compose.yml` localizado na raiz da pasta [`aula07`](https://github.com/ds-borges/data-engineering-roadmap/tree/main/Bootcamp-Intensivo-SQL/aula07).

## Objetivo do Desafio

Criar uma *stored procedure* chamada `ver_extrato` que recebe o `ID` de um cliente como parâmetro de entrada e retorna duas informações principais:
1.  O saldo atual do cliente.
2.  Uma lista detalhada das suas últimas 10 transações.

O desafio faz parte da [rinha-de-backend-2024-q1](https://github.com/zanfranceschi/rinha-de-backend-2024-q1)

## Lógica da Implementação

A *stored procedure* `ver_extrato` executa as seguintes operações:

1.  **Entrada de Parâmetros:**
    * Recebe o `ID do cliente` como único parâmetro de entrada.

2.  **Obtenção do Saldo Atual:**
    * É realizada uma consulta na tabela `clients` para obter o saldo atual do cliente com base no ID fornecido.

3.  **Exibição do Saldo Atual:**
    * O saldo atual do cliente é exibido por meio de uma mensagem de aviso (ex: `RAISE NOTICE` ou `PRINT`).

4.  **Obtenção das Últimas 10 Transações:**
    * É realizada uma consulta na tabela `transactions` para obter as 10 últimas transações do cliente, filtradas pelo seu ID e ordenadas pela data de realização (`data_realizacao`) em ordem decrescente (`DESC`).

5.  **Exibição das Transações:**
    * Utilizando um loop `FOR`, a procedure itera sobre o resultado da consulta de transações.
    * Para cada transação, são exibidos os seguintes detalhes (também via mensagens de aviso):
        * ID da transação
        * Tipo (depósito ou retirada)
        * Descrição
        * Valor
        * Data de realização

## Estrutura do Repositório

* `populate_challenge.sql`: Script SQL contendo os comandos `INSERT` para popular as tabelas `clients` e `transactions` com dados de exemplo.
* `ver_extrato.sql`: Script SQL contendo a definição (`CREATE PROCEDURE`) da *stored procedure* `ver_extrato`.
* `README.md`: Este arquivo.

## Como Utilizar

Para testar a solução, siga os passos abaixo:

1.  **Inicializar o Ambiente:**
    * Navegue até a pasta [`aula07`](https://github.com/ds-borges/data-engineering-roadmap/tree/main/Bootcamp-Intensivo-SQL/aula07) (que contém o `docker-compose.yml`).
    * Execute o comando abaixo para iniciar o contêiner do banco de dados em segundo plano:
    ```bash
    docker-compose up -d
    ```

2.  **Configurar o Banco de Dados:**
    * Conecte-se ao seu SGBD (Sistema de Gerenciamento de Banco de Dados) que foi iniciado pelo Docker.
    * **Execute o script `populate_challenge.sql`** (presente nesta pasta `rinha`) para popular as tabelas necessárias.

3.  **Criar a Stored Procedure:**
    * Na mesma conexão, **execute o script `ver_extrato.sql`** (também presente nesta pasta) para compilar e armazenar a *stored procedure*.

4.  **Executar a Procedure:**
    * Para visualizar o extrato de um cliente (exemplo: cliente com UUID 'fbca0a69-3858-457a-88f9-0a20bdad36e1'), utilize o comando `CALL`:

    ```sql
    CALL ver_extrato('fbca0a69-3858-457a-88f9-0a20bdad36e1');
    ```
