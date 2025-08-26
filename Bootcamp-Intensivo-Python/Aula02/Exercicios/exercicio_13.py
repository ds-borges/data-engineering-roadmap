################################ Exercício 13 ################################

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e,   #
# em seguida, imprima esta frase sem espaços em branco no início e no final. #

# Recebendo a frase
print("Vamos limpar a frase de forma que tiremos os espaços iniciais e/ou finais")
frase_suja = input("Digite a frase: ")

# Convertendo para maiúsculo
frase_limpa = frase_suja.strip()

print(f"A frase: {frase_suja}, continha {len(frase_suja)} caracteres, após limpar a frase: {frase_limpa}, contém {len(frase_limpa)} caracteres")