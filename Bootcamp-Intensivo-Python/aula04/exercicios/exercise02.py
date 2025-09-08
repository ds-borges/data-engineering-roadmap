"""
Exercício 2: Modificar Lista de Linguagens

Objetivo:
    Permitir que o usuário substitua um elemento em uma lista pré-definida de linguagens.

Instruções:
    - O programa exibirá uma lista de linguagens.
    - O usuário deve escolher o número correspondente à linguagem que deseja alterar.
    - O usuário deve fornecer o nome da nova linguagem.
    
Exemplo de Entrada/Saída:
    [Entrada]
    Escolha entre 1 e 4: 2
    Qual colocar no lugar: JavaScript

    [Saída]
    Essas são as linguagens agora: ['C', 'JavaScript', 'C++', 'Python']
"""

languages: list = ["C", "Java", "C++", "Python"]

print(f"Essas são as linguagens atuais: {languages}")

try:
    print("Vamos trocar agora")
    remove_user=int(input(f"Escolha entre o 1 e {len(languages)}: "))
    if remove_user < 1 or remove_user> len(languages):
        raise ValueError("Número fora dos limites")
    
    inser_user=input("Qual colocar no lugar: ")
    languages[remove_user-1]=inser_user

except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    # Boa prática ter uma exceção genérica para erros inesperados
    print(f"\nOcorreu um erro inesperado: {e}")
else:
    print(f"Essas são as linguagens agora: {languages}")
