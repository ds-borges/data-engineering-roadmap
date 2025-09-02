########################################## Exercício 20 #########################################

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes. #

# Pegando os valores
print("Comparando se 2 números são diferentes !!")
number_01 = float(input("Digite o primeiro número da comparação: "))
number_02 = float(input("Digite o segundo número da comparação: "))

# Comparando os numeros
if(number_01 != number_02):
    print(f"Os números são diferentes !!") 
else:
    print(f"Os números não são diferentes !!!")