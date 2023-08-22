from connection import get_connection

conn = get_connection()

cursor = conn.cursor()

cursor.execute('SELECT * FROM anotacao')

for record in cursor:
    print(record)

conn.close()