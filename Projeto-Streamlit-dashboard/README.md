# Real-Time Streamlit Dashboard

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-FF4B4B)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Supabase-336791)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED)
![n8n](https://img.shields.io/badge/n8n-Automation-EA4B71)

> Um dashboard analítico de alta performance desenvolvido para superar limitações de atualização em tempo real e custos de infraestrutura de ferramentas tradicionais.

---


## Sobre o Projeto
Este projeto nasceu da necessidade de visualizar dados transacionais (oriundos de um agente de IA no WhatsApp) em tempo real.
Ferramentas de BI tradicionais exigiam licenças caras ou gateways em máquinas Windows ligadas 24/7 para atualização constante.

A solução foi desenvolver uma arquitetura com foco em integridade de dados:
1.  **Ingestão:** O n8n gerencia o fluxo de mensagens do WhatsApp e realiza a inserção no PostgreSQL.
2.  **Segurança e Integridade:** O banco de dados utiliza **Triggers** e **Materialized Views** como uma camada de proteção. Essa estrutura isola a tabela de inserção, garantindo que apenas o agente autorizado realize gravações, prevenindo erros manuais, bugs externos ou tentativas de inserção não autorizada.
3.  **Processamento e Visualização:** O Streamlit consome os dados seguros e utiliza **Pandas** para calcular métricas e KPIs em tempo real.

## Arquitetura e Fluxo de Dados
```mermaid
    sequenceDiagram
    participant U as 📱 WhatsApp
    participant N as 🤖 n8n
    participant D as 🐘 PostgreSQL
    participant S as 🐍 Streamlit

    Note over U, N: 1. Ingestão
    U->>N: Envia Mensagem
    N->>D: Insere Dado (Seguro)

    Note over D: 2. Segurança
    D->>D: Trigger / Materialized View

    Note over S, D: 3. Visualização
    loop Real-Time Check
        S->>D: Consulta Dados
        D-->>S: Retorna atualizações
        S->>S: Calcula KPIs (Pandas)
    end
```

## Funcionalidades
Conexão Nativa: Integração direta com PostgreSQL (via Supabase).

Live Data: Atualização dinâmica refletindo o banco de dados.

Modularização: Código separado em camadas (Data Loader, Metrics, UI).

Dockerizado: Ambiente completo orquestrado via Docker Compose.

Tratamento SQL: Uso de triggers para evitar processamento pesado no lado do Python.

## Estrutura do Projeto

```tree
Projeto-Streamlit-dashboard/
├── app.py                  # Aplicação principal (Entry point)
├── Dockerfile              # Imagem Docker da aplicação
├── docker-compose.yml      # Orquestração dos containers
├── requirements.txt        # Lista de dependências Python
├── README.md               # Documentação do projeto
└── modulos/                # Pacote de lógica do sistema
    ├── database.py         # Conexão Singleton com Supabase
    ├── data_loader.py      # Extração e cache de dados
    ├── metrics.py          # Regras de negócio e cálculo de KPIs
    ├── graphics.py         # Gráficos Plotly e visualizações
    └── ui_componentes.py   # Componentes visuais (Cards, CSS)
```

| Módulo            | Responsabilidade                                                         |
| ----------------- | ------------------------------------------------------------------------ |
| database.py       | Conexão segura com Supabase usando psycopg2 ou sqlalchemy                                    |
| data_loader.py    | Carrega dados brutos para DataFrames Pandas com otimização de memória.                         |
| metrics.py        | Transforma dados em KPIs e métricas |
| graphics.py       | Gera gráficos (Plotly/Streamlit)    |
| ui_componentes.py | Cards, tabelas e layout responsivo  |

## Como Executar

Pré-requisitos
Docker e Docker Compose instalados.

Uma conta no Supabase (ou um banco Postgres local).

1. Configuração de Variáveis
Crie um arquivo .env na raiz do projeto seguindo o modelo:

```
SUPABASE_URL=seu_url_supabase
SUPABASE_KEY=sua_chave_supabase
# Exemplo de Connection String: postgresql://user:pass@host:5432/db
DATABASE_URL=postgresql://user:pass@host:port/db
```

2. Execução com Docker (Recomendado)
Todo o ambiente Python é construído automaticamente:

```
# Clone o repositório
git clone [https://github.com/ds-borges/data-engineering-roadmap.git](https://github.com/ds-borges/data-engineering-roadmap.git)

# Entre na pasta do projeto
cd Projeto-Streamlit-dashboard

# Suba o container
docker-compose up --build
```

Acesse o dashboard em: http://localhost:8501

3. Configuração do Banco de Dados (SQL)
Para que o dashboard funcione com o desempenho ideal, certifique-se de criar as tabelas e triggers conforme a documentação (ou adicione aqui o script SQL básico).
