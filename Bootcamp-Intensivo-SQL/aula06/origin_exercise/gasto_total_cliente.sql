---Exercício: Calcular o valor total já pago por cada cliente.
---Objetivo: Identificar o valor de vida/receita por cliente para priorização de relacionamento e estratégias comerciais baseadas em valor.

SELECT
	c.contact_name,
	sum((od.quantity*od.unit_price)*(1-od.discount)) as valor_mercadorias_liquido,
	sum(o.freight) as frete_gasto,
	sum(((od.quantity*od.unit_price)*(1-od.discount)) + o.freight) as valor_total_faturado_pago
FROM customers c JOIN orders o ON o.customer_id = c.customer_id
join order_details od on od.order_id = o.order_id
GROUP BY c.contact_name
