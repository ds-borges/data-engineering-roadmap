def receiving_value():
    """
    Função para Receber Números Do usuário e retornar como uma lista
    """

    print("-->Para números decimais use ponto<--\n")
    try:
        input_user = input("Digite os números desajados: ")

        if "," in input_user:
            input_user = input_user.replace(",", " ")

        lista_numeros = [float(x.strip()) for x in input_user.split()]
    except ValueError as e:
        print(f"Error: {e}")
    else:
        return lista_numeros
