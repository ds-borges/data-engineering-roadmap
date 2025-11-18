# Resumo da Aula sobre Conceitos Fundamentais de Banco de Dados

Este `README` resume os principais tópicos abordados na aula, focando nos conceitos de **ACID** (Transações) e um breve histórico sobre a origem dos SGBDs (Sistemas Gerenciadores de Banco de Dados).

---

## 🔒 Os Quatro Pilares: Conceito ACID

O acrônimo **ACID** representa um conjunto de propriedades que garantem que as transações de banco de dados sejam processadas de forma confiável em um SGBD.

| Propriedade | Nome Completo | Descrição |
| :--- | :--- | :--- |
| **A** | **Atomicidade** (Atomic) | Uma transação é tratada como uma única e indivisível unidade de trabalho. Ou todas as operações são concluídas com sucesso, ou nenhuma delas é. Cada comando faz uma coisa específica. |
| **C** | **Consistência** (Consistency) | Uma transação deve levar o banco de dados de um estado válido para outro estado válido. Se algo der errado, haverá um **`ROLLBACK`** (voltando ao estado anterior); se der certo, haverá um **`COMMIT`**. |
| **I** | **Isolamento** (Isolation) | Transações concorrentes devem ser isoladas umas das outras. Uma transação em andamento não pode interferir ou ser afetada por outras transações. Isso permite, por exemplo, que um `INSERT` não interfira em um `SELECT` de análise. |
| **D** | **Durabilidade** (Durability) | Depois que uma transação é confirmada (`COMMIT`), suas alterações são permanentes e não podem ser perdidas, mesmo em caso de falha do sistema. A informação inserida deve permanecer inalterada. |

---

## 🏛️ História do Banco de Dados

* **Pioneirismo:** Foi mencionado que a **Oracle** é frequentemente associada ao primeiro banco de dados comercial amplamente adotado.
* **Fundação:** A empresa Oracle foi fundada com o objetivo principal de **vender software de banco de dados**, estabelecendo-se como uma das gigantes do setor.
