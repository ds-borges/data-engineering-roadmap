from etl import pipeline_calcular_kpi_de_vendas_consolidados

pasta_argumento = "data"
formato_de_saida = ["csv", "parquet"]
pipeline_calcular_kpi_de_vendas_consolidados(pasta_argumento, formato_de_saida)
