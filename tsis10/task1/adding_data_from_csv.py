import psycopg2

conn = psycopg2.connect(
    host='localhost',
    user='postgres',
    password='admin',
    database='testdb'
)
command = """COPY contacts (first_name, last_name, phone_number)
            FROM %s DELIMITER ',' CSV HEADER;"""
conn.autocommit = True
path = str(input())
cursor = conn.cursor()

cursor.execute(command, (path, ))

cursor.close()
conn.close()