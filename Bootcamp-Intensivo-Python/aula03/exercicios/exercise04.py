# Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

print("Bem vindo ao cadastro")

try: # Inicia um bloco para capturar exceções, como a conversão de texto para número.
    name = input("Digite seu nome: ")
    if not name.strip(): # Verifica se o nome, após remover espaços em branco, está vazio.
        raise ValueError("Digite um nome")
    
    idade = int(input("Digite sua idade: ")) # Tenta converter a entrada para um número inteiro. Se o usuário digitar algo que não é um número, um erro de tipo (ValueError) é gerado aqui.
    if not 18 <= idade <= 65: # Verifica se a idade está dentro do intervalo de 18 a 65 anos.
        raise ValueError("Idade invalida !!")
    
    mail = input("Digite seu e-mail: ")
    # A validação do e-mail é um ponto a ser melhorado.
    # O código verifica se o "@" está presente, mas a segunda verificação para "gmail.com" é muito específica e restringe a entrada.
    # A validação de e-mail pode ser bem mais complexa, mas para este exercício, verificar a presença de "@" e um ponto "." após o "@" já seria um bom começo.
    if not "@" in mail: 
        raise ValueError("E-mail invalido !!")
    cut= mail.strip("@") # Esta linha não faz uma validação útil. O `strip()` remove caracteres do começo ou do fim da string, e neste caso está tentando remover "@" que não está no começo ou fim. Além disso, o resultado não é usado.
    if not "gmail.com" in mail: # Esta condição limita os e-mails apenas para o domínio "gmail.com". Isso não é ideal para um sistema de cadastro genérico.
        raise ValueError("E-mail invalido !!")

except ValueError as e: # Captura a exceção de tipo ValueError, que é gerada se a conversão de `idade` falhar ou por qualquer `raise ValueError` explícito.
    print(f"Error: {e}")

else: # Este bloco é executado somente se o `try` for concluído sem nenhuma exceção.
    print("Cadastro realizado com sucesso !!")