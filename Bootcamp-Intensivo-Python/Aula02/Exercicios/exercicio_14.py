######################################## Exercício 14 ########################################

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, #
################## em seguida, imprima o dia, o mês e o ano separadamente. ##################

from datetime import datetime

# Recebendo a data
print("Vamos separar a data de forma a mostrar o dia o mês e o ano separadamente")
data_completa = input("Digite a data no formato dd/mm/aaaa: ")

# Extraindo os dados da data
data_separada = datetime.strptime(data_completa, "%d/%m/%Y")
dia = data_separada.day
mes = data_separada.month
ano = data_separada.year

print(f"Extraindo os dados da data {data_completa} obtemos o dia {dia}, mês {mes}, ano {ano}")