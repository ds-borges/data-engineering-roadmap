---Exercício: Listar clientes do Reino Unido que pagaram mais de 1000 dólares
---Objetivo: Isolar um segmento geográfico de alto valor para possíveis ações de fidelização, up-sell e expansão regional.

WITH clientes as (
	SELECT
		c.customer_id,
		c.contact_name,
		sum(((od.quantity*od.unit_price)*(1-od.discount)) + o.freight) as valor_total_faturado_pago
	FROM customers c JOIN orders o ON o.customer_id = c.customer_id
	join order_details od on od.order_id = o.order_id
	WHERE c.country = 'UK'
	GROUP BY c.customer_id,c.contact_name
)
SELECT *
FROM clientes
where valor_total_faturado_pago > 1000
ORDER BY valor_total_faturado_pago DESC
