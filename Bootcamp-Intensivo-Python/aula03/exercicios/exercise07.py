### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

"""
Instruções:
- Digite os números separados por espaço ou vírgula.
- O programa aceita números inteiros ou decimais.

Exemplos de entrada:
- "10 20 30"
- "10,20,30"
- "10 , 20 , 30"
- "-5, 0, 5"

Dependências:
- É necessário ter a biblioteca scikit-learn instalada.
- Sé possível use em um ambiente virtual python -m venv .exercise07
- Use o ambiente virtual source .exercise07/bin/activate
- Instale com: pip install scikit-learn
"""
# Importa a classe MinMaxScaler da biblioteca scikit-learn. 
from sklearn.preprocessing import MinMaxScaler

# Exibe mensagens de boas-vindas ao usuário.
print("Bem vindo o normalizador de números")
print("Por favor digite apenas números para normalizar")

# Inicia o bloco de tratamento de erros.
try:
    # Recebe a entrada do usuário como uma string.
    dados = input("Digite os números para normalizar: ")
    
    # Se a string contiver vírgulas, substitui por espaços.
    if ',' in dados:
        dados = dados.replace(",", " ")
    
    # Divide a string em uma lista de strings de números, usando o espaço como separador.
    clean_list = dados.split()
    
    # Converte cada string para um float e cria uma lista de listas no formato exigido pela biblioteca.
    number_list = [[float(num)] for num in clean_list]

    # Verifica se a lista tem pelo menos 2 números para normalizar.
    if len(number_list) < 2:
        # Se não, levanta um erro com uma mensagem específica.
        raise ValueError("Quantidade insuficiente para a normalização !!")

# Captura erros do tipo ValueError, como string vazia ou conversão de tipo.
except ValueError as e:
    print(f"Error: {e}")
# Captura qualquer outro tipo de erro inesperado.
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")
    
# Bloco executado apenas se o "try" for bem-sucedido.
else:
    # Cria uma instância do normalizador.
    scaler = MinMaxScaler()

    # Aplica a normalização: encontra o min e max e transforma os dados.
    dados_normalizados = scaler.fit_transform(number_list)
    
    # Converte o resultado de volta para uma lista Python.
    dados_normalizados = dados_normalizados.tolist()
    
    # Formata cada número normalizado para ter 2 casas decimais.
    dados_formatados = [f"{num[0]:.2f}" for num in dados_normalizados]

    # Exibe a lista original.
    print(f"Dados originais: {number_list}")
    
    # Exibe a lista com os números normalizados e formatados.
    print(f"Dados normalizados: {dados_formatados}")
    