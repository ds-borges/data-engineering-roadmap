---Exercício: Fazer análise de crescimento mensal e calcular YTD (year-to-date).
---Objetivo: Acompanhar a evolução mês a mês, identificar variações mensais e quantificar o acumulado no ano para monitoramento de tendência e sazonalidade.

with Mensal as(
	SELECT
		EXTRACT(YEAR FROM o.order_date) as ano,
		EXTRACT(MONTH FROM o.order_date) as mes,
		SUM((od.quantity*od.unit_price) * (1 - od.discount)) as total_mensal
	from orders o join order_details od ON od.order_id = o.order_id
	GROUP BY 1,2
),
Total_Acumulado as(
	SELECT
	ano,
	mes,
	total_mensal,
	sum(total_mensal) OVER (PARTITION BY ano order by mes) as total_ytd

FROM Mensal
ORDER BY ano, mes
)

SELECT
	ano,
	mes,
	total_mensal,
	total_mensal - LAG(total_mensal, 1) OVER (PARTITION BY ano order by mes) as diference_ytd,
	total_ytd,
   (total_mensal - LAG(total_mensal) OVER (PARTITION BY ano ORDER BY mes)) / LAG(total_mensal) OVER (PARTITION BY ano ORDER BY mes) * 100 AS percent_change_month

FROM Total_Acumulado
