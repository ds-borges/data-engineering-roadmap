---Exercício: Separar clientes em 5 grupos (quintis) pelo valor pago.
---Objetivo: Estratificar a base em faixas de valor para análises de pareto, definição de níveis de atendimento e campanhas diferenciadas.

WITH valor_cliente as (

	SELECT
		c.contact_name as nome_cliente,
		sum(((od.quantity*od.unit_price)*(1-od.discount)) + o.freight) as valor_total_faturado_pago
	FROM customers c JOIN orders o ON o.customer_id = c.customer_id
	join order_details od on od.order_id = o.order_id
	GROUP BY c.contact_name
)

SELECT
	nome_cliente,
	valor_total_faturado_pago,
	NTILE(5) OVER(ORDER BY(valor_total_faturado_pago) DESC) AS quintil_valor
FROM valor_cliente
GROUP BY nome_cliente, valor_total_faturado_pago
ORDER BY quintil_valor, valor_total_faturado_pago DESC
