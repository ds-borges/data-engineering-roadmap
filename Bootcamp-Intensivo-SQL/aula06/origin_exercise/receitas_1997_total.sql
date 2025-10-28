---Exercício: Calcular o total de receitas no ano de 1997.
---Objetivo: Medir a receita consolidada de um período específico para avaliação histórica de desempenho e comparação com outros anos.

SELECT
	SUM(od.quantity * od.unit_price) as total
FROM order_details od join
(SELECT * from orders o WHERE o.order_date >= '1997-01-01'
AND o.order_date < '1998-01-01') as o
on o.order_id = od.order_id
