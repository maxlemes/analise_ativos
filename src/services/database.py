# carregando as bibliotecas
import sqlite3 


database = "src/data/controle.db"

# cria (ou conecta) com o banco de dados
con = sqlite3.connect(database)

# cria o cursor (aponta a célula a ser modificada)
cur = con.cursor()


sql = """
CREATE TABLE if not exists users (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                  name TEXT NOT NULL,
                                  password TEXT NOT NULL,
                                  email TEXT UNIQUE NOT NULL)"""


cur.execute(sql)

# fechando o banco de dados
con.commit()
con.close() 
