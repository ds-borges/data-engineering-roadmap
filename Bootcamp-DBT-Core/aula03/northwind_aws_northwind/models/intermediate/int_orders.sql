{{ config(
    materialized='view'
) }}

with orders_cte as (
    select
        order_id,
        order_date,
        customer_id,
        status,
        amount,
        country_code
    from {{ ref('stg_orders') }}
),

customers_cte as (
    select
        customer_id,
        name
    from {{ ref('stg_customers') }}
)

select
    o.order_id,
    o.order_date,
    o.customer_id,
    c.name as customer_name,
    o.status,
    o.amount,
    o.country_code
from orders_cte o
join customers_cte c on o.customer_id = c.customer_id
