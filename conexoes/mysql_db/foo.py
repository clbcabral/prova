from mysql.connector import connect


conn = connect(
    host='localhost',
    user='serpro',
    password='serpro',
    database='serpro'
)

cursor = conn.cursor()

cursor.execute('select * from note')

for row in cursor:
    print(row)

cursor.execute('insert into note (title, content) values (%s, %s)', (
    'teste',
    'teste conteudo'
))

conn.commit()

sql = """
create table if not exists foo (
    id int auto_increment primary key, 
    nome varchar(50) not null
)
"""

cursor.execute(sql)

conn.commit()

cursor.execute('select count(1) from foo')

for row in cursor:
    print(row)

cursor.execute('drop table foo')

conn.commit()

conn.close()