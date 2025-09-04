## Projeto de exemplo em python 

# Meus Primeiros Projetos em Python

Projeto 01: Saudação e Soma Simples

Este é um script introdutório que realiza duas tarefas básicas:
1. Solicita o nome do usuário e exibe uma mensagem de boas-vindas personalizada.

2. Calcula e exibe o resultado da operação matemática 3 + 4.

````
Python

print("exemplo 01\n")
print("Seja bem vindo(a): " + input("Digite seu nome: ") + " !")
print(3+4)
````

Projeto 02: Calculadora de Soma

Este script funciona como uma calculadora simples que soma dois valores numéricos inseridos pelo usuário.

Funcionalidades:

1. Pede ao usuário para digitar um primeiro valor.

2. Pede ao usuário para digitar um segundo valor.

3. Calcula a soma dos dois e exibe o resultado final.

````
Python

valor_01 = int(input("Digite o primeiro valor: "))
valor_02 = int(input("Digite o segundo valor: "))

valor_total = valor_01 + valor_02

print("A soma dos valores é: " + str(valor_total) + " !")
````

 Projeto 03: Desafio - Cálculo de Salário com Bônus

 Desafio proposto pelo Luciano da Jornada de Dados. O programa recebe as informações sobre o salário de alguem e seu bonus e faz o calculo informando o salário final.

 Funcionalidades:

 1. Solicita o nome do funcionário.

 2. Solicita o valor do seu salário (aceita valores decimais, como 1500.50).
 
 3. Solicita a porcentagem do bônus a ser aplicado.
 
 4. Calcula o salário final (salário + (salário * bônus / 100)).

 5. Exibe uma mensagem formatada com o nome do usuário, o bônus e o valor final a receber.


````
Python

# Inserção do nome
nome = input("Digite seu nome: ")

# Inserção do valor do salario e tipagem para float
salario = float(input("Digite seu salario: "))

# Inserção do bonus para calculo do salariofinal e tipagem para float
bonus = float(input("Digite seu bonus em %: "))

# Cálculo do salário final
valor_total = salario + (salario * (bonus/100)) 

# Impressão do nome e salário final formatado
print(f"O usuário {nome} possui bonus de: {bonus}% e vai reeceber salario de: {valor_total} !")
````
Como Executar

Para executar qualquer um desses projetos em sua máquina local, você precisa ter o Python instalado.

1. Clone este repositório ou baixe os arquivos .py.

2. Abra um terminal ou prompt de comando.

3. Navegue até a pasta onde os arquivos estão salvos.

4. Execute o script desejado com o comando:

````
Bash

python nome_do_arquivo.py
````

Sinta-se à vontade para explorar, modificar e usar esses códigos como referência para seus estudos!



