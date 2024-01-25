# carregando as bibliotecas
import streamlit as st

# carregando as funções em outros arquivos .py
from src.controller.dml import db_delete
from src.controller.dml import db_selectall, db_select



# função para a página de deletar dados
def deletar():
 
  ids = [t[0] for t in db_selectall()]    # id na posição 0
  emails = [t[3] for t in db_selectall()] # email na posição 3

  if "dele" not in st.session_state:
    st.session_state.dele = False

    st.title('Deletar Dados')

    with st.form(key='insert'):
      delete_email =  st.selectbox(
            label='Selecione o usuário', options=emails)
      button_delete_select = st.button('Consultar')

      item = db_select(delete_email,'email')
        st.write(item)
  

    # delete_email =  st.selectbox(
    #         label='Selecione o usuário', options=emails)
    
    # # item = db_select(delete_email,'email')
    # st.write(delete_email)

    # # button_delete_select = st.button('Consultar')
    # # delete_id = st.number_input(label='Insira o email', format='%d', step=1)
    # # button_delete_select = st.button('Consultar')

    # if button_delete_select:
    #   st.session_state.dele = True

    #   if st.session_state.dele == True:
    #     item = db_select(delete_email,'email')[0]
    #     st.write(item)
    #     button_delete = st.button('Deletar')

    #     # if button_delete:
    #     #   cliente.excluir(item[0])
    #     #   st.success('Cliente deletado com sucesso!!!')
    #     #   st.session_state.dele = False