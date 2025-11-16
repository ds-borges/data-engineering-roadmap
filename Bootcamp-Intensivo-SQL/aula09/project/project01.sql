CREATE OR REPLACE FUNCTION refresh_materialized_view_sales_acumulaed()
returns trigger as
$$
BEGIN
	refresh MATERIALIZED VIEW sales_accumulated_monthly_mv;
	RETURN NULL;
END;
$$ language plpgsql;

CREATE OR REPLACE TRIGGER refresh_materialized_sales_orders
AFTER INSERT OR UPDATE OR DELETE ON orders
FOR EACH STATEMENT
EXECUTE FUNCTION refresh_materialized_view_sales_acumulaed();

CREATE OR REPLACE TRIGGER refresh_materialized_sales_orders_details
AFTER INSERT OR UPDATE OR DELETE ON order_details
FOR EACH STATEMENT
EXECUTE FUNCTION refresh_materialized_view_sales_acumulaed();
