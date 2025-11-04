Recriando a tabela transactons com o cliente_id do tipo UUID

CREATE TABLE IF NOT EXISTS transactions (
id SERIAL PRIMARY KEY NOT NULL,
tipo CHAR(1) NOT NULL,
descricao VARCHAR(10) NOT NULL,
valor INTEGER NOT NULL,
cliente_id UUID NOT NULL,
realizada_em TIMESTAMP NOT NULL DEFAULT NOW()
);

SELECT * FROM clients
"33424a77-ad33-4f06-9cca-b9e10ca63098"	80000	0
"69f67e8a-e74f-4040-8598-11ceb7cad9ec"	1000000	0
"2f44ce00-5189-4abe-8936-a166233cd726"	10000000	0
"b70c8e49-2f9f-4fb9-b989-086de23a87b9"	500000	0
"fbca0a69-3858-457a-88f9-0a20bdad36e1"	10000	0

fazer teste

CALL realizar_transacao ('d', 'amarelo', 80000000, 'b70c8e49-2f9f-4fb9-b989-086de23a87b9')
    NOTICE:  Saldo atual do cliente: 0
    NOTICE:   Limite atual do cliente: 500000

    ERROR:  Saldo mais o limite é insuficiente para realizar a transação
    CONTEXT:  PL/pgSQL function realizar_transacao(character,character varying,integer,uuid) line 17 at RAISE

    ERROR:   Saldo mais o limite é insuficiente para realizar a transação
    SQL state: P0001

CALL realizar_transacao ('d', 'amarelo', 80000, '33424a77-ad33-4f06-9cca-b9e10ca63098')
    NOTICE:  Saldo atual do cliente: 0
    NOTICE:   Limite atual do cliente: 80000
    NOTICE:  Saldo do cliente após transação: -80000
    CALL

    Query returned successfully in 98 msec.



Resultado após testes

"69f67e8a-e74f-4040-8598-11ceb7cad9ec"	1000000	0
"2f44ce00-5189-4abe-8936-a166233cd726"	10000000	0
"b70c8e49-2f9f-4fb9-b989-086de23a87b9"	500000	0
"fbca0a69-3858-457a-88f9-0a20bdad36e1"	10000	0
"33424a77-ad33-4f06-9cca-b9e10ca63098"	80000	-80000
