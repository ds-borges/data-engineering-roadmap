with renamed as (
    select
        *
    from
    {{ref('raw_crm__nova_tabela')}}
)

select * from renamed
