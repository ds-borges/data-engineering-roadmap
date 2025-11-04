Desafio
Criar uma stored procedure "ver_extrato" para fornecer uma visão detalhada do extrato bancário de um cliente, incluindo seu saldo atual e as informações das últimas 10 transações realizadas. Esta operação recebe como entrada o ID do cliente e retorna uma mensagem com o saldo atual do cliente e uma lista das últimas 10 transações, contendo o ID da transação, o tipo de transação (depósito ou retirada), uma breve descrição, o valor da transação e a data em que foi realizada.

Explicação Detalhada:

Entrada de Parâmetros:

    A stored procedure recebe o ID do cliente como parâmetro de entrada.

Obtenção do Saldo Atual:

    É realizada uma consulta na tabela "clients" para obter o saldo atual do cliente com base no ID fornecido.

Exibição do Saldo Atual:

    O saldo atual do cliente é exibido por meio de uma mensagem de aviso.

Obtenção das Últimas 10 Transações:

    É realizada uma consulta na tabela "transactions" para obter as últimas 10 transações do cliente, ordenadas pela data de realização em ordem decrescente.

Exibição das Transações:

    Utilizando um loop FOR, cada transação é iterada e suas informações são exibidas por meio de mensagens de aviso.
    Para cada transação, são exibidos o ID da transação, o tipo de transação (depósito ou retirada), uma breve descrição da transação, o valor da transação e a data em que foi realizada.
    O loop é interrompido após exibir as informações das últimas 10 transações.

populando as tabelas
