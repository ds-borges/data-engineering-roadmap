############# Exercício 25 #############

# 25: Conversão de Tipo com Validação. #

print("Bem-vindo(a) a conversão de números.")
print("Aqui iremos converter os números digitados para numeros reais.\n")

# O bloco 'try' tenta executar o código principal. Se um erro de conversão acontecer,
# a execução pula diretamente para o bloco 'except', sem quebrar o programa.
try:
    # --- ENTRADA DE DADOS ---
    print("Aviso, digite os numeros separados por espaço, exp: 1 2.2 3 3.4")
    # Captura a entrada do usuário como uma única string. Ex: "1 5.5 9 10.1"
    input_num = input("Por favor, digite os numeros desejados: ")
    
    # --- PROCESSAMENTO ---
    # O método .split() quebra a string nos espaços e a transforma em uma lista de strings.
    # Ex: a string "1 5.5 9" vira a lista ['1', '5.5', '9']
    lista_numero = input_num.split()

    # Inicializa duas listas vazias. Elas servirão para armazenar os números
    # depois que forem classificados e convertidos.
    num_int = []
    num_float = []

    # Inicia um loop 'for' que vai percorrer cada item (que é uma string) da 'lista_numero'.
    for num in lista_numero:
        # Esta é a principal lógica para diferenciar um float de um inteiro.
        # Ele verifica se o caractere '.' (ponto decimal) existe na string 'num'.
        if '.' in num:
            # Se encontrar um ponto, o código assume que é um float.
            # Converte a string para o tipo float e a adiciona na lista 'num_float' com .append().
            num_float.append(float(num))
        else:
            # Se não houver ponto, o código assume que é um inteiro.
            # Converte a string para o tipo int e a adiciona na lista 'num_int'.
            num_int.append(int(num))

# --- TRATAMENTO DE ERRO ---
# Este bloco só é executado se ocorrer um 'ValueError' dentro do bloco 'try'.
# Isso acontece se o usuário digitar algo que não pode ser convertido para número (ex: 'abc').
except ValueError as e:
    print(f"\nErro: Por favor, digite apenas números válidos. Detalhes: {e}")

# O bloco 'else' está ligado ao 'try'. Ele só será executado se o bloco 'try'
# for concluído com SUCESSO, ou seja, sem nenhum erro.
else:
    # --- SAÍDA DOS RESULTADOS ---
    # Verifica se o usuário de fato digitou algo. Se a lista estiver vazia, mostra a mensagem.
    if not lista_numero:
        print("Você não digitou nenhum número para a conversão.")
    else:
        print("\n--- Resultados ---")
        # Verifica se a lista 'num_int' tem algum item antes de tentar imprimi-la.
        if num_int:
            print(f"Números inteiros identificados: {num_int}")

        # Verifica se a lista 'num_float' tem algum item antes de tentar imprimi-la.
        if num_float:
            print(f"Números reais (float) identificados: {num_float}")