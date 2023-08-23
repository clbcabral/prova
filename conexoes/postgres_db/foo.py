from psycopg2 import connect

conn = connect(
    host='localhost',
    user='serpro',
    password='serpro',
    database='serpro')

cursor = conn.cursor()

cursor.execute("""
create table if not exists note (
    id serial primary key not null,
    title varchar(50) not null,
    content text null
)
""")

conn.commit()

cursor.executemany('insert into note(title, content) values (%s, %s)', [
    ('foobar', 'bal bal ablla lbalabl'),
    ('bee', 'lakjqjl  ajalkjal al ja'),
])

conn.commit()

cursor.execute('select * from note')

for row in cursor:
    print(row)

conn.close()