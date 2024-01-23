"""
DML - Manipulação de dados

C - CREATE
R - READ
U - UPDATE
D - DELETE
"""

# carregando as bibliotecas
import sqlite3 

database = "src/data/controle.db"

def commit_close(func):
    def decorator(*args):
        # cria (ou conecta) com o banco de dados
        con = sqlite3.connect(database)
        # cria o cursor (aponta a célula a ser modificada)
        cur = con.cursor()
        # define a função com os argumentos
        sql=func(*args)
        # executa a função
        cur.execute(sql)
        # comenta o db
        con.commit()
        # fecha o db
        con.close
    return decorator



# função para inserir registros no banco de dados
@commit_close
def db_insert (name, password, email):
    return """
    INSERT INTO users(name, password, email)
        VALUES('{}', '{}', '{}')
    """.format(name, password, email)

@commit_close
def db_update(name, email):
    return """
    UPDATE users SET name = '{}' WHERE email = '{}'
    """.format(name,email)

@commit_close
def db_delete(id):
    return """
    DELETE FROM users WHERE id='{}'
    """.format(id)

def db_select(data, field):
    con = sqlite3.connect(database)
    cur = con.cursor()
    sql = """
    SELECT *
    FROM users
    WHERE '{}'={}
    """.format(data, field)

    cur.execute(sql)
    data = cur.fetchall()
    con.close()
    return data

def db_selectall():
    con = sqlite3.connect(database)
    cur = con.cursor()
    sql = """
    SELECT *
    FROM users
    """.format()

    cur.execute(sql)
    data = cur.fetchall()
    rows = []
    for rec in data:
        rows.append(rec)
    con.close()
    return rows