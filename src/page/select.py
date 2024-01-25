# carregando as bibliotecas
import streamlit as st

# carregando as funções em outros arquivos .py
from src.controller.dml import db_selectall, db_delete

# função para a página de consultar dados
def consultar():

  st.title('Consultar Dados')

  colunas = st.columns((1,3,3,3,2))
  campos = ['Id','Nome','Password','Email','Excluir']
  
  for coluna, campo in zip(colunas,campos):
    coluna.write(campo)

  for item in db_selectall():
    col1,col2,col3,col4,col5 = st.columns((1,3,3,3,2))

    col1.write(item[0])
    col2.write(item[1])
    col3.write(item[2])
    col4.write(item[3])
    button_excluir = col5.empty()

    on_click_excluir = button_excluir.button('Excluir', 'btnExcluir' + str(item[0]))

    if on_click_excluir:
        db_delete(item[0])
        button_excluir.button('Excluído', 'btnExcluir' + str(item[0]))