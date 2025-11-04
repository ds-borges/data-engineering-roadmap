CREATE OR REPLACE PROCEDURE realizar_transacao(
	IN p_tipo CHAR(1),
	IN p_descricao VARCHAR(10),
	IN p_valor INTEGER,
	IN p_cliente_id UUID
)

LANGUAGE plpgsql
as $$
DECLARE
	saldo_atual INTEGER;
	limite_cliente INTEGER;
	saldo_apos_transacao INTEGER;
BEGIN
	-- Pegando informações dos clientes e colocando nas novas variáveis para fazer operações
	SELECT saldo, limite into saldo_atual, limite_cliente
	FROM clients
	where id = p_cliente_id;

	RAISE NOTICE 'Saldo atual do cliente: %', saldo_atual;
	RAISE NOTICE ' Limite atual do cliente: %', limite_cliente;

    -- O saldo mais o limite não podem ser menor que o valor da transação(p_value)
	IF p_tipo = 'd' and saldo_atual + limite_cliente < p_valor THEN
		RAISE EXCEPTION ' Saldo mais o limite é insuficiente para realizar a transação';
	END IF;

	--Debitará ou dará credito (depositar)
	UPDATE clients
	SET saldo = saldo + CASE WHEN p_tipo = 'd' THEN -p_valor ELSE +p_valor END
	WHERE id = p_cliente_id;

	INSERT INTO transactions(tipo, descricao, valor, cliente_id)
	VALUES (p_tipo, p_descricao, p_valor, p_cliente_id);

	SELECT saldo INTO saldo_apos_transacao
	FROM clients
	where id = p_cliente_id;

	RAISE NOTICE 'Saldo do cliente após transação: %', saldo_apos_transacao;
END;
$$;
