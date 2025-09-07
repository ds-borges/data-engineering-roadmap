#Desafio da aula 2

right_enter=False
while not right_enter:
    try:
        #Inserção do nome
        nome = input("Digite seu nome: ") 
        if not nome or not nome.isalpha():
            raise ValueError("Entrada inválida! Por favor, digite apenas letras.")           
        if not nome:
            raise ValueError("Digite o nome do colaborador")
        else:
            right_enter=True
    except ValueError as e:
        print(f"\nError: {e}")


right_enter=False
while not right_enter:
    try:
        #Inserção do valor do salario e tipagem para float
        salario = float(input("Digite seu salario: "))
        if not salario:
            raise ValueError("Digite o salario do colaborador")
        else:
            right_enter=True
    except ValueError as e:
        print(f"\nErro: {e}")

right_enter=False
while not right_enter:
    try:
        #Inserção do bonus para calculo do salariofinal e tipagem para float
        bonus = float(input("Digite seu bonus em %: "))
        if not bonus:
            raise ValueError("Digite o bonus do colaborador")
        else:
            right_enter=True
    # Isso acontece se o usuário digitar algo que não seja diferente de número (ex: 'abc').
    except ValueError as e:
        print(f"\nErro: {e}")
 
#Cálculo do salário final transformando o valor do bonus em porcentagem para aaplicação do bonus
valor_total = salario + (salario * (bonus/100)) 

#Impressão do nome e salário
#print(nome +", seu salário com bonus é: " + str(valor_total)  + " !") 
print(f"O usuário {nome} possui bonus de: {bonus}% e vai reeceber salario de: {valor_total} !")