CREATE OR REPLACE PROCEDURE ver_extrato(
	IN p_cliente_id UUID
)

LANGUAGE plpgsql
as $$

DECLARE
	saldo_atual INTEGER;
    details RECORD;
BEGIN
    SELECT saldo into saldo_atual
	FROM clients
	where id = p_cliente_id;

    RAISE NOTICE E'Saldo atual do cliente: %\n', saldo_atual;

    FOR details in
        SELECT tipo, descricao , valor , cliente_id, realizada_em
        FROM transactions
        WHERE cliente_id = p_cliente_id
        ORDER BY realizada_em DESC
        LIMIT 10
    LOOP
        RAISE NOTICE 'Cliente: %, Tipo: %, Descrição: %, Valor: %, Data: %', details.cliente_id, details.tipo, details.descricao, details.valor, details.realizada_em ;
    END LOOP;
END;

$$;
