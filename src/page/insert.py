# carregando as bibliotecas
import sqlite3

import streamlit as st

# carregando as funções em outros arquivos .py
import src.controller.cliente as cliente


def inserir():
    st.title('Inserir Dados')
    profissoes = [
        'Analista de Dados',
        'Engenheiro de Dados',
        'Cientista de Dados',
    ]

    with st.form(key='insert'):
        input_name = st.text_input(label='Insira o nome')
        input_age = st.number_input(
            label='Insira a idade', format='%d', step=1
        )
        input_job = st.selectbox(
            label='Insira a profissão', options=profissoes
        )
        button_submit = st.form_submit_button('Enviar')

        if button_submit:
            cliente.incluir(input_name, input_age, input_job)
            st.success('Cliente incluido com sucesso!!!')


conn = sqlite3.connect('pwd.db')
c = conn.cursor()
c.execute(
    """CREATE TABLE if not exists pwd_mgr (app_name varchar(20) not null,
                        user_name varchar(50) not null,
                        pass_word varchar(50) not null,
                        email_address varchar(100) not null,
                        url varchar(255) not null,
                    primary key(app_name)       
                    );"""
)
