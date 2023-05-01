import psycopg2

conn = psycopg2.connect(
    host='localhost',
    user='postgres',
    password='admin',
    database='testdb'
)
command = """INSERT INTO contacts (first_name, last_name, phone_number)
            VALUES (%s, %s, %s);"""
conn.autocommit = True
first_name = str(input())
last_name = str(input())
phone_number = str(input())
cursor = conn.cursor()

cursor.execute(command, (first_name, last_name, phone_number))

cursor.close()
conn.close()