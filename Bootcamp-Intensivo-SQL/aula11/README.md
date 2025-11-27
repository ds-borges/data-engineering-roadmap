# Aula – Desempenho em Banco de Dados e Plano de Execução

Este documento reúne anotações sobre como decisões de modelagem, escrita de queries e escolha de ferramentas impactam o desempenho de um banco de dados relacional.

---

## 1. Código legível vs. desempenho

- Um banco de dados mais completo e bem modelado tende a oferecer melhores possibilidades de consulta e integridade de dados.
- Porém, muitas refatorações e operações focadas apenas em legibilidade podem tornar a query mais custosa em termos de desempenho.
- É importante equilibrar clareza do código com eficiência, principalmente em cenários com grandes volumes de dados.

---

## 2. Plano de execução de uma query

- Existe uma “ideia intuitiva” da ordem em que uma query é executada (por exemplo: `FROM`/`JOIN` antes de `WHERE`, `GROUP BY`, `ORDER BY`, `LIMIT`).
- Na prática, o otimizador de consultas do banco é bastante inteligente e pode alterar essa ordem lógica para reduzir trabalho desnecessário.
- Exemplo: em um `JOIN` entre uma tabela com 5 linhas e outra com 10.000 linhas, se a query precisa apenas de 5 resultados, o banco pode aplicar um `LIMIT` mais cedo no plano de execução, evitando processar e transportar linhas em excesso.

---

## 3. Custo de processamento x custo de transporte

- Transportar 1.000 linhas é muito diferente de transportar apenas 10 linhas, tanto em tempo quanto em uso de rede.
- Otimizar queries não impacta só o processamento interno do banco, mas também:
  - O volume de dados enviado pela rede.
  - O tempo de resposta percebido pelo cliente/aplicação.
- Pensar em filtros, limites e projeções (selecionar só as colunas necessárias) ajuda a reduzir esse custo de transporte.

---

## 4. DuckDB x PostgreSQL x Pandas

- DuckDB foi mencionado como funcionando de forma semelhante ao PostgreSQL em termos de plano de execução.
- Assim como bancos relacionais tradicionais, DuckDB possui um otimizador que:
  - Analisa a query.
  - Monta um plano de execução.
  - Reorganiza operações para reduzir custo.
- Já o Pandas, de forma geral, não trabalha com um plano de execução SQL: as operações são executadas na ordem em que são escritas no código.
- Por isso, DuckDB tende a ser mais “performático” em muitos cenários analíticos, especialmente quando comparado a sequências de operações Pandas sem otimização manual.

---

## 5. Considerações finais da aula

- Nem sempre o que é mais legível é o mais eficiente; é preciso considerar o impacto em desempenho.
- Entender como o banco monta e ajusta o plano de execução ajuda a escrever queries mais eficientes.
- Reduzir a quantidade de dados processados e transportados (com filtros, limites e projeções) é uma das principais estratégias de otimização.
- Ferramentas com otimizador de consultas (como PostgreSQL e DuckDB) podem oferecer grande vantagem de performance sobre abordagens em memória sem plano de execução, como muitas operações diretas em Pandas.
