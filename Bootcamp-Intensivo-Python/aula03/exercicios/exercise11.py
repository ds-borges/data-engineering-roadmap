### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

"""
Instruções de uso:
1. Ao executar o script, ele pedirá para você inserir um dado por vez.
2. Cada dado será adicionado a uma lista.
3. Para encerrar a entrada de dados, digite "sair" (não diferencia maiúsculas de minúsculas).
   A lista final com os dados coletados será exibida.

Exemplo de interação:
Entre com um nome (ou digite 'sair' para encerrar): Ana
Entre com um nome (ou digite 'sair' para encerrar): Bruno
Entre com um nome (ou digite 'sair' para encerrar): SAIR

Saída esperada:
Os nomes coletados foram: ['Ana', 'Bruno']
"""

# Lista para armazenar os dados coletados
nomes = []

# Inicia um loop infinito para ler as entradas
while True:
    # Pede a entrada do usuário
    entrada = input("Entre com um nome (ou digite 'sair' para encerrar): ")
    
    # Verifica se a entrada é a palavra-chave para sair (tratando maiúsculas e minúsculas)
    if entrada.lower() == "sair":
        break
    
    # Adiciona a entrada à lista, evitando entradas vazias
    if entrada:
        nomes.append(entrada)

# Exibe a lista final com os dados coletados após o loop ser interrompido
print(f"\nOs nomes coletados foram: {nomes}")