---Exercício: Identificar os 10 produtos com maiores vendas
---Objetivo: Descobrir produtos campeões de receita para orientar reposição de estoque, promoções, cross-sell e planejamento de portfólio.

CREATE VIEW TopProductsRevenues AS
(
	SELECT
		p.product_name as produto,
		sum((od.quantity*od.unit_price)*(1-od.discount)) as valor_total_mercadoria
	FROM order_details od join products p ON p.product_id = od.product_id
	GROUP BY p.product_name
	ORDER BY valor_total_mercadoria DESC
)

GRANT SELECT ON TopProductsRevenues TO test_user;

--Create User
--CREATE ROLE test_user;
--EXEC sp_addrolemember 'test_user', 'SEU_USUARIO';

SELECT *
FROM TopProductsRevenues
LIMIT 10
