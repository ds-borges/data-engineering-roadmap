#Desafio da aula 2

try:
    #Inserção do nome
    nome = input("Digite seu nome: ") 
    if not nome:
        raise ValueError("Digite o nome do colaborador")

except ValueError as e:
    print(f"\nErro: Por favor, digite apenas números válidos. Detalhes: {e}")

else:
    try:
        #Inserção do valor do salario e tipagem para float
        salario = float(input("Digite seu salario: "))

        #Inserção do bonus para calculo do salariofinal e tipagem para float
        bonus = float(input("Digite seu bonus em %: "))

    # Isso acontece se o usuário digitar algo que não seja diferente de número (ex: 'abc').
    except ValueError as e:
        print(f"\nErro: Por favor, digite apenas números válidos. Detalhes: {e}")
    else:
        #Cálculo do salário final transformando o valor do bonus em porcentagem para aaplicação do bonus
        valor_total = salario + (salario * (bonus/100)) 

        #Impressão do nome e salário
        #print(nome +", seu salário com bonus é: " + str(valor_total)  + " !") 
        print(f"O usuário {nome} possui bonus de: {bonus}% e vai reeceber salario de: {valor_total} !")