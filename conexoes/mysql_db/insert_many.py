from connection import get_connection

conn = get_connection()

cursor = conn.cursor()

sql = 'INSERT INTO anotacao (titulo, conteudo) VALUES (%s, %s)'
values = [
    ('dentista', 'dentista no dia 10/10/2023 às 8h.'),
    ('aniversário', 'aniversário de dona maria no dia X.'),
]

cursor.executemany(sql, values)

conn.commit()

conn.close()