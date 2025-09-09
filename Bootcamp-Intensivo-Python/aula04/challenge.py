#Desafio da aula 4

def calcular_bonus_funcionario(detalhes_funcionario:dict) -> dict :

    """
    Calcula o salário final com bônus a partir de um dicionário de detalhes do salário.
    """
    novo_salario_com_bonus = detalhes_funcionario.copy()
    
    salario = novo_salario_com_bonus['salario']
    bonus = novo_salario_com_bonus['bonus']
    
    # Fórmula simplificada e mais legível
    salario_final = salario * (1 + bonus / 100)
    
    novo_salario_com_bonus['salario_final'] = salario_final
    return novo_salario_com_bonus

informacoes_funcionario:dict = {}

right_name: bool =False
right_wage: bool =False
right_bonus: bool =False

while not right_name:
        try:
            #Inserção do nome
            informacoes_funcionario['nome']=(input("Digite seu nome: ")) 
            if not informacoes_funcionario['nome'] or not informacoes_funcionario['nome'].isalpha():
                raise ValueError("Entrada inválida! Por favor, digite apenas letras.")           
            if not informacoes_funcionario['nome']:
                raise ValueError("Digite o nome do colaborador")
            else:
                right_name=True
        except ValueError as e:
            print(f"\nError: {e}")

while not right_wage:
    try:
        #Inserção do valor do salario e tipagem para float
        informacoes_funcionario['salario']=(float(input("Digite seu salario: ")))
        if not informacoes_funcionario['salario']:
            raise ValueError("Digite o salario do colaborador")
        else:
            right_wage=True
    except ValueError as e:
        print(f"\nErro: {e}")

while not right_bonus:
    try:
        #Inserção do bonus para calculo do salariofinal e tipagem para float
        informacoes_funcionario['bonus']=(float(input("Digite seu bonus em %: ")))
        if not informacoes_funcionario['bonus']:
            raise ValueError("Digite o bonus do colaborador")
        else:
            right_bonus=True
    # Isso acontece se o usuário digitar algo que não seja diferente de número (ex: 'abc').
    except ValueError as e:
        print(f"\nErro: {e}")
    
    #Cálculo do salário final transformando o valor do bonus em porcentagem para aaplicação do bonus

novo_salario=calcular_bonus_funcionario(informacoes_funcionario)
print(novo_salario)