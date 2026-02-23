{{ config(
    materialized='table'
) }}

with orders_summary_cte as (
    select
        order_id,
        customer_id,
        customer_name,
        status,
        amount
    from {{ ref('int_orders') }}
),

business_logic as (
    select
        order_id,
        customer_id,
        customer_name,
        status as order_status,
        sum(amount) as total_sales,
        count(order_id) as total_orders
    from orders_summary_cte
    group by
        order_id,
        customer_id,
        customer_name,
        order_status
)

select * from business_logic
