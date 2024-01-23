# carregando as bibliotecas
import sqlite3

import streamlit as st

# carregando as funções em outros arquivos .py
from src.controller.dml import db_insert


def inserir():
    st.title('Criar usuário')

    #definindo os perfis
    perfil = [
        'Pessoal',
        'Profissional'
    ]

    with st.form(key='insert'):
        input_name = st.text_input(label='Nome')
        input_password = st.text_input(label='Password')
        input_email = st.text_input(label='email')
        input_age = st.number_input(
            label='Idade', format='%d', step=1
        )
        input_profile = st.selectbox(
            label='Perfil', options=perfil
        )
        button_submit = st.form_submit_button('Enviar')

        if button_submit:
            db_insert(input_name, input_password, input_email)
            st.success('Cliente incluido com sucesso!!!')
