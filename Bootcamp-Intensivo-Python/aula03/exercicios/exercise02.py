### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

# Exibe uma mensagem de boas-vindas ao usuário.
print("Bem vindo a classificação de temperatura")

# Inicia um bloco para tentar executar uma operação que pode falhar (a conversão de texto para número).
try:
    # Pede a temperatura e tenta converter o valor digitado para um número decimal (float).
    celsius = float(input("Digite a temperatura atual: "))
# Se o usuário digitar algo que não seja um número, um 'ValueError' ocorre e este bloco é executado.
except ValueError:
    # Informa ao usuário que a entrada foi inválida.
    print("Digite um valor para a análise !!")
# Este bloco 'else' só é executado se o 'try' for bem-sucedido (ou seja, um número válido foi digitado).
else:
    # Verifica se a temperatura é considerada "baixa" (menor que 18).
    if celsius < 18:
        print(f"A temperatura {celsius} está muito baixa") 
    # Se não for baixa, verifica se está na faixa "normal" (de 18 a 32, inclusive).
    elif celsius >= 18 and celsius <= 32:
        print(f"A temperatura {celsius} está normal") 
    # Se não se encaixar em nenhuma das condições anteriores, assume-se que é "alta".
    else:
        print(f"A temperatura {celsius} está muito alta")