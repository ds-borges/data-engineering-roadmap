### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

"""
Instruções de uso:
1. Ao executar o script, ele pedirá para você inserir um número.
2. O script continuará aceitando números indefinidamente, desde que eles estejam
   fora do intervalo de 1 a 10.
3. Para encerrar o programa e exibir a lista de números coletados, digite qualquer
   número entre 1 e 10 (incluindo 1 e 10).

Exemplo de interação:
Digite um número para salvar (ou um número de 1 a 10 para sair): 15
Digite um número para salvar (ou um número de 1 a 10 para sair): -5
Digite um número para salvar (ou um número de 1 a 10 para sair): abc
Error: invalid literal for int() with base 10: 'abc'
Digite um número para salvar (ou um número de 1 a 10 para sair): 7

Os números coletados foram: [15, -5]
"""
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

# Lista para armazenar os números coletados que estão fora do intervalo de saída
numbers = []

# Inicia um loop infinito para continuar pedindo a entrada do usuário
while True:
    try:
        # Solicita a entrada e tenta converter para um número inteiro
        user_input = int(input("Digite um número para salvar (ou um número de 1 a 10 para sair): "))
        
        # Verifica a condição de saída: se o número estiver no intervalo de 1 a 10
        if 1 <= user_input <= 10:
            print("\nNúmero no intervalo aceito. Encerrando o programa.")
            break
        else:
            # Se o número estiver fora do intervalo, ele é válido para ser adicionado à lista
            numbers.append(user_input)
            
    except ValueError:
        # Captura o erro se a entrada não puder ser convertida para um número inteiro
        print("\nEntrada inválida. Por favor, digite apenas números.\n")
        
# Exibe a lista final com os números coletados
print(f"\nOs números coletados foram: {numbers}")