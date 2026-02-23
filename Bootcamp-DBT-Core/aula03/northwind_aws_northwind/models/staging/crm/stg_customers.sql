with sources as (
    select * from {{ source('northwinddb', 'customers') }}
)

    select
        id as customer_id,
        name,
        email
    from sources
