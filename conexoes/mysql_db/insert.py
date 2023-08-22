from connection import get_connection

conn = get_connection()

cursor = conn.cursor()

sql = 'INSERT INTO anotacao (titulo, conteudo) VALUES (%s, %s)'

cursor.execute(sql, ('feira', 'comprar pão e queijo.'))

conn.commit()

conn.close()