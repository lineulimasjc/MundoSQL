import streamlit as st

st.set_page_config(
    page_title="Mundo SQL",
    page_icon="img/sql.png",
    layout="centered",
    initial_sidebar_state="auto",
)

pgs = {
    "Linguagem SQL": [
        st.Page("pages/home.py", title="Home", icon="🏡"), #house_with_garden
        st.Page("pages/select.py", title="SELECT", icon="🔍"),
        #st.Page("pages/saida_de_dados.py", title="Saída de Dados", icon="📊"), #bar_chart
        #st.Page("pages/variaveis.py", title="Variáveis", icon="🗄️"), #file_cabinet
        #st.Page("pages/entrada_de_dados.py", title="Entrada de Dados", icon="⌨️"), #keyboard
        #st.Page("pages/estrutura_de_decisao.py", title="Estrutura de Decisão", icon="❓"), #question
        #st.Page("pages/laco_de_repeticao.py", title="Laço de Repetição", icon="🔁"), #repeat
        #st.Page("pages/funcao.py", title="Função", icon="⚙️"), #gear
        #st.Page("pages/vetor.py", title="Vetor", icon="📏"), #straight_ruler
        #st.Page("pages/matriz.py", title="Matriz", icon="📋"), #clipboard
        #st.Page("pages/registro.py", title="Registro", icon="📦"), #package
    ],
    # "C++ Orientado a Objetos": [
    #      st.Page("pages/example_three.py", title="Learn about us"),
    #      st.Page("pages/example_two.py", title="Try it out"),
    # ],
}

pg = st.navigation(pgs)

pg.run()
