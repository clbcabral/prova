from mysql.connector import connect

def get_connection():
  conn = connect(
      host='localhost', 
      user='serpro', 
      password='serpro', 
      database='serpro'
  )
  return conn
