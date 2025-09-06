### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.
# transacao = {'valor': 12000, 'hora': 20}
# transacao = {'valor': 131000, 'hora': 21}

log=input("Dê os detalhes da transação: ")

value_transation=None
time_transation=None

log_strip=log.split()
try:
    #log_hora=log.split("'hora':")
    for cont, sentence in enumerate(log_strip):
        if "{'valor':" == sentence:
            if cont + 1 < len(log_strip):
                value_transation = log_strip[cont+1]
                value_transation=int(value_transation.replace(",", ""))
#                print(f"valor: {value_transation}")
        if "'hora':" == sentence:
            if cont + 1 < len(log_strip):
                time_transation = log_strip[cont+1]
                time_transation=int(time_transation.replace("}", ""))
#                print(f"valor: {time_transation}")
except ValueError as e:
    print(f"Error: {e}")
else:
    if not time_transation or not value_transation:
        print("Error dados para análise incompletos !!")
    elif not 9 <= time_transation <= 20 or value_transation > 10000:
        print(f"Transação suspeita devido ao horário {time_transation}!!")
    else:
        print(f"Tudo certo para a transação no valor: {value_transation} devido o horário {time_transation}")
