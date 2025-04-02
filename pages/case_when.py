import streamlit as st

# st.image("img/file.png")

st.title("📌 CASE...WHEN", anchor=False)

st.write("O comando ```CASE...WHEN``` no SQL é usado para criar condições dentro de uma consulta, funcionando como uma estrutura condicional.")

st.write("Sintaxe:")

code = '''
CASE  
    WHEN condição1 THEN resultado1  
    WHEN condição2 THEN resultado2  
    ...  
    ELSE resultado_padrão  
END
'''
st.code(code, language="sql")


st.divider()


url = "https://mundosql.streamlit.app/select"
st.write("⚠️ Usaremos o mesmo [contexto](%s) do comando ```SELECT```." % url)


st.text("")

st.subheader("💡 Exemplo:", anchor=False)

code = '''
SELECT nome, lim_cred,
       CASE
           WHEN lim_cred >= 5000 THEN 'Alto'
           WHEN lim_cred >= 3000 THEN 'Médio'
           ELSE 'Baixo'
       END AS categoria_credito
FROM Clientes;
'''
st.code(code, language="sql")

st.write("🎯 **Resultado:**")

st.markdown("""
|    **nome**    | **lim_cred** | **categoria_credito** |
|:--------------:|--------------|----------------|
|   João Silva   |         8500 |      Alto      |
| Maria Oliveira |         3500 |      Médio     |
|  Carlos Souza  |         1400 |      Baixo     |
|   Ana Pereira  |         2000 |      Baixo     |
|  Pedro Santos  |         6500 |      Alto      |
| Lucia Ferreira |         4750 |      Médio     |
|  Rafael Costa  |         8500 |      Alto      |
""")

st.write("📝 Essa consulta retorna os dados da tabela **Clientes**, exibindo o **nome**, o **lim_cred** (limite de crédito) e uma classificação categorizada com base nesse limite:")

st.write("🔷 **Alto** para valores a partir de 5000")

st.write("🔷 **Médio** para valores entre 3000 e 4999")

st.write("🔷 **Baixo** para valores abaixo de 3000")

st.write("Isso ajuda a organizar os clientes de acordo com seu limite de crédito.")
