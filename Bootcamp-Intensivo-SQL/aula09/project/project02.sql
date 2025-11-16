--Trigger to register update in employee title
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

-- Procedure to help update
CREATE OR REPLACE PROCEDURE employee_update(
	IN p_employee_id INTEGER,
	IN p_title VARCHAR
)

LANGUAGE plpgsql
as $$
BEGIN
    update employees
	set title = p_title
	where employee_id = p_employee_id;
END;
$$;
