lista_de_numero: list  = [40,50,60,70,0,-408593,1,50]

def ordenar_lista_de_numero(numeros: list) -> list:
    nova_lista_de_numero = numeros.copy()

    for i in range(len(nova_lista_de_numero)):
        for j in range(i+1, len(nova_lista_de_numero)):
            if nova_lista_de_numero[i]>nova_lista_de_numero[j]:
                nova_lista_de_numero[i], nova_lista_de_numero[j] = nova_lista_de_numero[j], nova_lista_de_numero[i]

    return nova_lista_de_numero

nova_lista= ordenar_lista_de_numero(lista_de_numero)
#print(nova_lista)
