### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

""""
Instruções de uso:
1. O script tentará fazer uma requisição para a URL definida na variável 'url'.
2. Ele fará até 3 tentativas, com um intervalo de 2 segundos entre elas.
3. Se a requisição retornar um código de status 200 (sucesso), a conexão será
   considerada bem-sucedida e o programa será encerrado.
4. Se o limite de tentativas for atingido sem sucesso (por erro de conexão ou
   código de status diferente de 200), o script irá exibir uma mensagem de falha.
"""

import requests
import time

url = 'https://api.github.com/users/google'

# Inicializa o contador de tentativas e a flag de sucesso
try_again = 1
conexion = False

# Inicia o loop para tentar a conexão no máximo 3 vezes
while try_again <= 3:
    try:
        # Tenta fazer a requisição para a URL, com um tempo limite de 5 segundos
        response = requests.get(url, timeout=5)
        
        # Se o código de status for 200, a conexão foi bem-sucedida
        if response.status_code == 200:
            # Define a flag de sucesso como True
            conexion = True
            # Sai do loop imediatamente, pois não precisa tentar de novo
            break
            
    except requests.exceptions.RequestException as e:
        # Captura qualquer erro de conexão (falha de rede, timeout, etc.)
        print(f"Error: {e}")
        
    # Incrementa o contador de tentativas para a próxima repetição
    try_again += 1
    # Espera 2 segundos antes de tentar novamente, para não sobrecarregar o servidor
    time.sleep(2)

# Verifica a flag de sucesso após o loop terminar
if conexion:
    print(f"Conexão com sucesso !!")
else:
    # Se o loop terminou e a flag é False, significa que todas as tentativas falharam
    print(f"Falha na conexão !!")