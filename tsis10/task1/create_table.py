import psycopg2

conn = psycopg2.connect(
    host='localhost',
    user='postgres',
    password='admin',
    database='testdb'
)
command = """CREATE TABLE contacts (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(50),
  last_name VARCHAR(50),
  phone_number VARCHAR(20),
);"""
conn.autocommit = True

cursor = conn.cursor()

cursor.execute(command)

cursor.close()
conn.close()