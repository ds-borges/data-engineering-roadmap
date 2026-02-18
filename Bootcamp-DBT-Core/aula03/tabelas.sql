-- Criação da tabela customers
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255)
);

-- Inserção de dados na tabela customers com valores nulos e duplicados
INSERT INTO customers (name, email) VALUES
('Alice', 'alice@example.com'),
('Bob', NULL),
(NULL, 'charlie@example.com'),
('Charlie', 'alice@example.com');

-- Criação da tabela orders
CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    order_date DATE,
    customer_id INT,
    status VARCHAR(50),
    amount DECIMAL(10, 2),
    country_code CHAR(2)
);

-- Inserção de dados na tabela orders com valores nulos e status inválido
INSERT INTO orders (order_date, customer_id, status, amount, country_code) VALUES
('2024-01-01', 1, 'placed', 100.00, 'US'),
('2024-01-02', 2, 'invalid_status', 200.00, 'CA'), -- Status inválido
(NULL, 3, 'completed', 300.00, 'GB'), -- Data do pedido nula
('2024-01-04', 4, 'returned', 150.00, NULL); -- Código do país nulo
