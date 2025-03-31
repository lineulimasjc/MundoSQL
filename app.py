import streamlit as st

st.set_page_config(
    page_title="Mundo SQL",
    page_icon="img/sql.png",
    layout="centered",
    initial_sidebar_state="auto",
)

pgs = {
    "Linguagem SQL": [
        st.Page("pages/home.py", title="Home", icon="🏡"),
        st.Page("pages/select.py", title="SELECT", icon="✅"),
        st.Page("pages/distinct.py", title="DISTINCT", icon="💎"),
        st.Page("pages/count.py", title="COUNT", icon="🔢"),
        st.Page("pages/sum.py", title="SUM", icon="➕"),
        st.Page("pages/max.py", title="MAX", icon="🥇"),
        st.Page("pages/min.py", title="MIN", icon="🔻"),
        st.Page("pages/avg.py", title="AVG", icon="⚖️"),
        st.Page("pages/round.py", title="ROUND", icon="⭕"),
        st.Page("pages/where.py", title="WHERE", icon="🔍"),
    ],
    # "C++ Orientado a Objetos": [
    #      st.Page("pages/example_three.py", title="Learn about us"),
    #      st.Page("pages/example_two.py", title="Try it out"),
    # ],
}

pg = st.navigation(pgs)

pg.run()
