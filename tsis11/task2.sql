CREATE OR REPLACE PROCEDURE add_user(name VARCHAR, phone VARCHAR)
LANGUAGE plpgsql
AS $$
BEGIN
  IF EXISTS(SELECT * FROM contacts WHERE first_name = name) THEN
    UPDATE contacts SET phone_number = phone WHERE first_name = name;
  ELSE
    INSERT INTO contacts(first_name, phone_number) VALUES(name, phone);
  END IF;
END;
$$;

CALL add_user('Artur', '87000000');