{{ config(
    materialized='incremental',
    unique_key='category_id',
    on_schema_change='fail'
) }}

select * from {{ref('stg_crm__nova_tabela')}}


{% if is_incremental() %}

  -- Assuming Postgres database
  where updated_at > (select max(updated_at) from {{ this }})

{% endif %}
