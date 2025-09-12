# Um Bilhão de Linhas: Desafio de Processamento de Dados com Python

Esta pasta (**aula05**) foi inspirada no projeto original do Luciano Filho:  
[lvgalvao/One-Billion-Row-Challenge-Python](https://github.com/lvgalvao/One-Billion-Row-Challenge-Python#um-bilh%C3%A3o-de-linhas-desafio-de-processamento-de-dados-com-python).

## Introdução

O objetivo desta atividade é explorar estratégias de processamento eficiente de grandes volumes de dados utilizando Python. O desafio proposto consiste em manipular um arquivo de medições de temperatura de várias estações meteorológicas, simulando um cenário de **1 bilhão de linhas (~14 GB)**, e calcular para cada estação a temperatura **mínima, máxima e média** (com uma casa decimal), exibindo os resultados ordenados por nome da estação.

O formato de cada linha do arquivo é:  
<nome da estação>;<medição>

text
Exemplo:  
Hamburg;12.0
Bulawayo;8.9
Palembang;38.8
...

text

Este desafio foi inspirado no [The One Billion Row Challenge](https://github.com/gunnarmorling/1brc), originalmente proposto para Java e posteriormente adaptado para Python pelo Luciano.

## Dependências e Execução

Para reproduzir os exemplos desta pasta, é recomendável utilizar as mesmas versões de bibliotecas do projeto original:  
- **Polars:** 0.20.3  
- **DuckDB:** 0.10.0  
- **Dask[complete]:** ^2024.2.0  

Recomenda-se criar um ambiente virtual e instalar as dependências necessárias.

## Resultados e Benchmarks

Os testes no projeto original apresentaram os seguintes tempos para processamento do arquivo completo:

| Implementação          | Tempo         |
|-----------------------|---------------|
| Bash + awk            | 25 minutos    |
| Python puro           | 20 minutos    |
| Python + Pandas       | 263 segundos  |
| Python + Dask         | 155,62 segundos |
| Python + Polars       | 33,86 segundos |
| Python + DuckDB       | 14,98 segundos |

Esses resultados mostram o impacto do uso de bibliotecas modernas para manipulação de dados em larga escala!

## Créditos

- Projeto original: [lvgalvao/One-Billion-Row-Challenge-Python](https://github.com/lvgalvao/One-Billion-Row-Challenge-Python)  
- Proposta do desafio em Java: [gunnarmorling/1brc](https://github.com/gunnarmorling/1brc)  
- Colaboradores: Koen Vossen, Arthur Julião, Luciano Filho

## Nota

Se deseja entender em detalhes a motivação, metodologia, scripts originais e resultados completos, acesse o repositório do Luciano no GitHub:  
https://github.com/lvgalvao/One-Billion-Row-Challenge-Python
