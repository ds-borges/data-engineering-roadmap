---Exercício: Selecionar apenas os clientes dos grupos 1, 2 e 3 para ações de Marketing.
---Objetivo: Focar esforços de Marketing em clientes de média a alta contribuição, maximizando ROI de campanhas e retenção.

WITH valor_cliente as (

	SELECT
		c.contact_name as nome_cliente,
		sum(((od.quantity*od.unit_price)*(1-od.discount)) + o.freight) as valor_total_faturado_pago
	FROM customers c JOIN orders o ON o.customer_id = c.customer_id
	join order_details od on od.order_id = o.order_id
	GROUP BY c.contact_name
),

quintil_cliente as (
	SELECT
		nome_cliente,
		valor_total_faturado_pago,
		NTILE(5) OVER(ORDER BY(valor_total_faturado_pago) DESC) AS quintil_valor
	FROM valor_cliente
	GROUP BY nome_cliente, valor_total_faturado_pago
	ORDER BY quintil_valor, valor_total_faturado_pago DESC
)

SELECT *
FROM quintil_cliente
where quintil_valor in (1,2,3)
ORDER BY
    quintil_valor,
    valor_total_faturado_pago DESC;
