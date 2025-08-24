#Desafio

nome = input("Digite seu nome: ")
#print("\n")
salario = float(input("Digite seu salario: "))
#print("\n")
bonus = float(input("Digite seu bonus em %: "))
#print("\n")

valor_total = salario + (salario * (bonus/100)) 
#print(nome +", seu salario com bonus é: " + str(valor_total)  + " !") 
print(f"O usuário {nome} possui bonus de: {bonus}% e vai reeceber salario de: {valor_total} !") 