CREATE TABLE employee_audit (
    employee_id INT,
    old_title VARCHAR,
    new_title VARCHAR,
    data_de_modificacao_do_salario TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE OR REPLACE FUNCTION registrar_auditoria_titulo() returns trigger as
$$
BEGIN
	insert into employee_audit (employee_id, old_title, new_title)
	values (old.employee_id, old.title, new.title);
    RETURN NEW;
END;
$$ 	LANGUAGE plpgsql;

CREATE TRIGGER trg_title_modificaded
AFTER UPDATE OF title ON employees
FOR EACH ROW
EXECUTE FUNCTION registrar_auditoria_titulo();
