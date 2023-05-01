import psycopg2

conn = psycopg2.connect(
    host='localhost',
    user='postgres',
    password='admin',
    database='testdb'
)
command = """UPDATE contacts SET first_name = 'Artem' WHERE phone_number = '87770230743';"""
conn.autocommit = True

cursor = conn.cursor()

cursor.execute(command)

cursor.close()
conn.close()