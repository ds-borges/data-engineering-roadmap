# Aula 6 - Conceitos Teóricos e Exercícios Práticos

## Descrição da Pasta

A pasta atual contém exercícios da aula passada devido o foco ser em apresentar conceitos teóricos importantes do SQL:

- CTE (Common Table Expression)
- Subquery (Subconsulta)
- View (Visão)
- Materialized View (Visão Materializada)
- Temp Table (Tabela Temporária)

## Conceitos Principais Observados em Aula

- **CTE**: Usada para tornar a consulta mais legível, criando resultados temporários nomeados dentro da consulta. É útil para simplificar consultas complexas.
- **Subquery**: Consulta aninhada dentro de outra consulta. Embora funcional, pode ser menos legível que CTEs.
- **View**: Representa uma consulta salva como uma tabela virtual. Útil para definir permissões de leitura, permitindo que somente grupos específicos acessem dados sensíveis.
- **Materialized View**: Semelhante a um snapshot, armazena o resultado da consulta fisicamente. Muito útil para auditoria futura, pois mantém um estado congelado dos dados.
- **Temp Table**: Tabela temporária que só funciona na mesma conexão e é descartada ao final dela. Ideal para uso quando os dados não serão mais necessários após o dia.

## Aplicação na Aula

Para aplicar esses conceitos foi adotado os exercícios da aula 05, que originalmente não utilizavam CTE, views ou estruturas similares. O objetivo é transformar esses exercícios usando essas técnicas para praticar seu uso.

---
