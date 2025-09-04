################################ Exercício 15 #################################

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário. #

# Recebendo a palavra ou a frase
print("Concatenando 2 palavras ou frases")
palavra_inicial = input("Digite a primeira palavra ou frase: ")
palavra_final = input("Digite a segunda palavra ou frase: ")

# Concatenando as entradas e acrescentando um espaço no meio para não ficar muito estranho
palavra_concatenada = palavra_inicial + " " + palavra_final

print(f"A contenção das palavras/frases é: {palavra_concatenada} com {len(palavra_concatenada)} caracteres")