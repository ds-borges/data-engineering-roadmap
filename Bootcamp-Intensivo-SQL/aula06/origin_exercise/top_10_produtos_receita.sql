---Exercício: Identificar os 10 produtos com maiores vendas
---Objetivo: Descobrir produtos campeões de receita para orientar reposição de estoque, promoções, cross-sell e planejamento de portfólio.

select
	p.product_name as produto,
	sum((od.quantity*od.unit_price)*(1-od.discount)) as valor_total_mercadoria
from order_details od join products p ON p.product_id = od.product_id
GROUP BY p.product_name
ORDER BY valor_total_mercadoria DESC
LIMIT 10
