# carregando as bibliotecas
import streamlit as st

# carregando as funções em outros arquivos .py
import src.page.insert as insert
import src.page.select as select


# criando a barra lateral do menu
st.sidebar.title('Menu')
page = st.sidebar.selectbox(
    'Cliente', ['Inserir', 'Consultar', 'Alterar', 'Deletar', 'Login']
)

# carregando as páginas de acordo com a seleção do menu
if page == 'Inserir':
    insert.inserir()

if page == 'Consultar':
    select.consultar()



# https://github.com/afaqueumer/password_manager/blob/main/app.py
# https://dadosaocubo.com/inserir-dados-com-streamlit-e-o-postgresql/