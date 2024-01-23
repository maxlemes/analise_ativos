# carregando as bibliotecas
import streamlit as st

# carregando as funções em outros arquivos .py
import src.page.insert as insert

# criando a barra lateral do menu
st.sidebar.title('Menu')
page = st.sidebar.selectbox(
    'Cliente', ['Inserir', 'Consultar', 'Alterar', 'Deletar']
)

# carregando as páginas de acordo com a seleção do menu
if page == 'Inserir':
    insert.inserir()
