### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.
# Modelo de entrada
# transacao = {'valor': 12000, 'hora': 20}
# transacao = {"valor": 2000, 'hora': 12}
# {"valor": 131000, 'hora': 21}
# {"valor": 3000, "hora": 12}
# {"valor": 3000, "hora": 2}
import json

# Solicita a entrada do usuário.
log = input("Dê os detalhes da transação: ")

# Inicia um bloco para tratar possíveis erros.
try:
    # Se a string contiver '=', isola apenas o dicionário.
    if "=" in log:
        log = log.split("=")[1]
    
    # Substitui as aspas simples por duplas, compatível com JSON.
    if "'" in log:
        log = log.replace("'", '"')
    
    # Converte a string JSON em um dicionário Python.
    log_strip = json.loads(log)

    # Valida se as chaves 'valor' e 'hora' existem no dicionário.
    if not 'valor' in log_strip or not 'hora' in log_strip:
        # Se alguma chave estiver faltando, lança um erro.
        raise KeyError("As chaves 'valor' e 'hora' são obrigatórias.")

# Captura erros de formato de dados.
except ValueError as e:
    print(f"Error: {e}")
# Se o bloco 'try' não teve erros, executa esta parte.
else:
    # Checa se o valor é maior que 10000 OU se a hora é fora do horário comercial.
    if log_strip['valor'] > 10000 or log_strip['hora'] > 18 or log_strip['hora'] < 9:
        # Exibe aviso se a transação for suspeita.
        print(f"Aviso, transação supeita !!")
    else:
        # Exibe mensagem se a transação for normal.
        print("Tudo certo com a transação!!")