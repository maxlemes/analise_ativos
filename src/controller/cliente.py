# carregando as funções em outros arquivos .py
import pysqlite3 as sqlite

conn = sqlite.connect("pwd.db")
c = conn.cursor()
c.execute("""CREATE TABLE if not exists pwd_mgr (app_name varchar(20) not null,
                        user_name varchar(50) not null,
                        pass_word varchar(50) not null,
                        email_address varchar(100) not null,
                        url varchar(255) not null,
                    primary key(app_name)       
                    );""")


# função para inserir registros no banco de dados
def incluir (nome, idade, profissao):
  db.cur.execute("""
           INSERT into public.clientes (nome, idade, profissao)
           values('%s', '%s', '%s')
   """ % (nome, idade, profissao))
  db.con.commit()

  https://github.com/afaqueumer/password_manager/blob/main/app.py

https://dadosaocubo.com/inserir-dados-com-streamlit-e-o-postgresql/