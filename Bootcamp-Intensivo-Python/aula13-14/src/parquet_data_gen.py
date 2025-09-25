import pandas as pd

data = {"id": [1, 2, 3], "nome": ["Nina", "Tobias", "Bruna"]}
df = pd.DataFrame(data)
df.to_parquet("data/parquet_files/teste.parquet")
