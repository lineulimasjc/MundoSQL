import streamlit as st

st.title("📌 JOIN", anchor=False)

st.write("O `JOIN` é usado para **combinar registros de duas ou mais tabelas** com base em uma coluna relacionada (geralmente uma chave primária/estrangeira).")


st.write("###")



st.write("**Principais Tipos:**")

st.write("🔵 **`INNER JOIN`**: Retorna apenas registros que têm correspondência em ambas as tabelas.")

st.write("🔵 **`LEFT JOIN`**: Retorna todos os registros da tabela à esquerda (primeira tabela) e os correspondentes da direita (ou `NULL` se não houver).")

st.write("🔵 **`RIGHT JOIN`**: O inverso do `LEFT JOIN`.")

st.write("🔵 **`FULL JOIN`**: Retorna todos os registros quando há correspondência em qualquer uma das tabelas.")



st.divider()



st.write("**Estrutura das Tabelas ```Clientes``` e ```Telefones```:**")

# st.image("img/pk_tabela.png")

code = '''
-- Criando a tabela Clientes
CREATE TABLE Clientes (
    id_cliente      INT         PRIMARY KEY,
    nome            CHAR(50)    NOT NULL,
    email           CHAR(100)
);

-- Criando a tabela Telefones com chave estrangeira
CREATE TABLE Telefones (
    id_telefone     INT         PRIMARY KEY,
    id_cliente      INT,
    numero          CHAR(11)    NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES Clientes (id_cliente)
);
'''
st.code(code, language="sql")



st.write("**Inserindo Dados de Exemplo:**")

code = '''
-- Inserindo dados na tabela Clientes
INSERT INTO Clientes (id_cliente, nome, email) VALUES
(1, 'João Silva', 'joao@email.com'),
(2, 'Maria Souza', 'maria@email.com'),
(3, 'Carlos Souza', 'csouza@email.com');

-- Inserindo dados na tabela Telefones
INSERT INTO Telefones (id_telefone, id_cliente, numero) VALUES
(1, 1, '11999991111'),
(2, 1, '11988882222'),
(3, 2, '21977773333');
'''
st.code(code, language="sql")



st.divider()



st.subheader("💡 Exemplo de `JOIN`:", anchor=False)

st.write("📝 A consulta retorna o **nome de cada cliente com seus respectivos telefones**, apenas se existir correspondência nas duas tabelas.")

code = '''
SELECT c.nome, t.numero
FROM Clientes c INNER JOIN Telefones t
ON c.id_cliente = t.id_cliente;
'''
st.code(code, language="sql")

st.write("🎯 **Resultado:**")

st.markdown("""
| nome         | numero          |
|:------------:|:---------------:|
| João Silva   | (11) 9999-8888  |
| João Silva   | (11) 7777-5555  |
| Maria Souza  | (21) 3333-4444  |
""")



st.write("###")



st.subheader("💡 Exemplo de `LEFT JOIN`:", anchor=False)

st.write("📝 A consulta retorna o **nome de cada cliente com seus respectivos telefones**, mesmo que o cliente não possua telefone.")

code = '''
SELECT c.nome, t.numero
FROM Clientes c LEFT JOIN Telefones t
ON c.id_cliente = t.id_cliente;
'''
st.code(code, language="sql")

st.write("🎯 **Resultado:**")

st.markdown("""
| nome         | numero          |
|:------------:|:---------------:|
| João Silva   | (11) 9999-8888  |
| João Silva   | (11) 7777-5555  |
| Maria Souza  | (21) 3333-4444  |
| Carlos Souza | *NULL*          |
""")