import os
import sqlite3

import pandas as pd
from lib.classes.FilesSources import FilesSources


class DbSource(FilesSources):
    def create_path(self):
        current_directory = os.getcwd()
        self.folder_path = os.path.join(current_directory, "data", "db_files")
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)

    def check_for_new_files(self):
        current_files = os.listdir(self.folder_path)
        new_files = [
            file
            for file in current_files
            if file not in self.previous_files and file.endswith(".db")
        ]

        if new_files:
            print("New files detected:", new_files)
            # Update the list of previous files
            self.previous_files = current_files
        else:
            print("No new DB files detected.")
            self.get_data()

    def get_data(self, query=None):
        if self.previous_files:
            try:
                db_file = os.path.join(self.folder_path, self.previous_files[0])
                with sqlite3.connect(db_file) as conn:
                    cursor = conn.cursor()
                    if query is None:
                        cursor.execute(
                            "SELECT name FROM sqlite_master WHERE type='table';"
                        )
                        tables = cursor.fetchall()
                        if not tables:
                            print("Nenhuma tabela encontrada no banco de dados.")
                            return None

                        all_tables_data = {}
                        for table in tables:
                            table_name = table[0]
                            df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
                            all_tables_data[table_name] = df
                            print(f"Tabela: {table_name}")
                            print(df)
                            print("\n")
                        return all_tables_data
                    else:
                        df = pd.read_sql_query(query, conn)
                        print(df)
                        return df
            except Exception as e:
                print(f"Erro ao acessar o banco de dados: {e}")
                return None

    def transform_data_to_df(self):
        return super().transform_data_to_df()
