######### Exercício 21 #########

# 21: Conversor de Temperatura #

print("Conversor de temperatura de Celsius para Fahrenheit")
while True:
    try:
        celsius = float(input("Digite a temperatura em Celsius: "))
        break
    except ValueError:
        print("Digite apenas um valor para converter !!\n")

# Convertendo para Fahrenheit e arredondando para ter apenas 2 casas decimais
Fahrenheit = round((celsius * 1.8) +32, 2)
print(f"A temperatura {celsius} em Celsius é igual {Fahrenheit} em Fahrenheit") 