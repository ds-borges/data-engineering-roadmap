with sources as (
    select * from {{ source('northwinddb', 'orders') }}
)

    select
        order_id,
        order_date,
        customer_id,
        status,
        amount,
        country_code
    from sources
