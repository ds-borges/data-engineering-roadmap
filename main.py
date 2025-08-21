print("Jornada de dados")

# Variáveis
idade = 34
Nome = "Luciano"

# Print
print(idade)

# Soma
nova_idade = idade + 1
print(nova_idade)

# Para criar uma LISTA, use colchetes []
lista = [1, 2, 3, 4, 5]
print(f"Lista original: {lista}")

# O método .reverse() inverte a própria lista. Ele não retorna um valor.
lista.reverse()

# Agora a variável 'lista' contém os valores invertidos
print(f"Lista após o .reverse(): {lista}")

# Se você tentar fazer lista_invertida = lista.reverse(), o valor será None
lista_invertida_none = lista.reverse()
print(f"Resultado de atribuir o .reverse(): {lista_invertida_none}")

# Nova forma de inverter uma lista
lista_original = [1, 2, 3, 4, 5]

# Usando slicing [::-1] para criar uma CÓPIA invertida
lista_invertida = lista_original[::-1]

print(f"Lista original não foi alterada: {lista_original}")
print(f"Nova lista invertida: {lista_invertida}")