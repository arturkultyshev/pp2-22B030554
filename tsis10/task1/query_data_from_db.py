import psycopg2

conn = psycopg2.connect(
    host='localhost',
    user='postgres',
    password='admin',
    database='testdb'
)
command = """SELECT * FROM contacts WHERE first_name = 'Artem';"""
conn.autocommit = True

cursor = conn.cursor()

cursor.execute(command)
print(cursor.fetchone())

cursor.close()
conn.close()