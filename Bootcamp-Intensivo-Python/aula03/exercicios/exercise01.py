### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

# Inicia um bloco para tentar executar operações que podem dar erro.
try:
    # Pede a descrição do produto.
    description = str(input("Digite a descrição do produto: "))
    # Se a descrição estiver vazia, gera um erro intencional.
    if not description:
        raise ValueError("Digite a descrição")
    
    # Pede a quantidade e a converte para número.
    quant= float(input("Digite a quantidade vendida: "))
    # Se a quantidade for negativa, gera um erro.
    if quant <0:
        raise ValueError("A quantidade vendida não pode ser negativa")
    
    # Pede o preço e o converte para número.
    price= float(input("Digite o preço: "))
    # Se o preço for negativo, gera um erro.
    if price <0:
        raise ValueError("O preço não pode ser negativo")
    
# Se qualquer um dos 'raise' acima for acionado, este bloco captura o erro.
except ValueError as e:
    # Imprime que os dados são inválidos e mostra a mensagem de erro específica.
    print(f"DADOS INVALIDOS: {e}")
# Este bloco 'else' só é executado se o bloco 'try' terminar sem nenhum erro.
else:
    # Se tudo deu certo, imprime que os dados são válidos.
    print("DADOS VALIDOS")