import streamlit as st

st.title("📌 PRIMARY KEY", anchor=False)

st.write("Uma **chave primária** (*primary key*) em um banco de dados é um campo (ou conjunto de campos) que identifica de forma **única** cada registro em uma tabela. Ela **não pode ter valores repetidos** nem **valores nulos**.")

st.subheader("💡 Exemplo:", anchor=False)

st.write("Na tabela ```Clientes```:")

st.image("img/pk_tabela.png")

st.write("Aqui, a coluna ```id_cliente``` é a **chave primária**, pois cada cliente tem um ID único.")

st.write("**Em SQL:**")

code = '''
CREATE TABLE Clientes (
    id_cliente  INT         PRIMARY KEY,
    nome        CHAR(50),
    email       CHAR(100)
);
'''
st.code(code, language="sql")

st.write("Essa definição garante que **id_cliente** será único e obrigatório para cada cliente.")
