from src.interface.classes.csv_class import CsvProcessor

arquivo_csv = "src/exemplo.csv"
filtro = ["estado", "preço"]
limite = ["SP", "10,50"]

arquivo_CSV = CsvProcessor(arquivo_csv)
arquivo_CSV.carregar_csv()
print(arquivo_CSV.filtrar_por(filtro, limite))
