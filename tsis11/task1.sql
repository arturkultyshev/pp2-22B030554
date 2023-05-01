CREATE OR REPLACE FUNCTION get_data(pattern VARCHAR)
RETURNS TABLE (id INTEGER, first_name  VARCHAR, last_name VARCHAR, phone_number  VARCHAR)
AS $$
BEGIN
  RETURN QUERY
    SELECT *
    FROM contacts
    WHERE phone_book.first_name LIKE '%' || pattern || '%'
        OR phone_book.last_name LIKE '%' || pattern || '%'
       OR phone_book.phone_number LIKE '%' || pattern || '%';
END;
$$ LANGUAGE plpgsql;

SELECT * FROM get_data('artur');