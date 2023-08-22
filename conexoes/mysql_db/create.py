from connection import get_connection

conn = get_connection()

cursor = conn.cursor()

cursor.execute('CREATE TABLE anotacao (id INT AUTO_INCREMENT PRIMARY KEY, titulo VARCHAR(255) NOT NULL, conteudo TEXT NULL)')

conn.close()
