import streamlit as st

st.title("📌 FOREIGN KEY", anchor=False)

st.write("Uma **chave estrangeira** (*foreign key*) é um campo em uma tabela que faz referência à **chave primária** de outra tabela. Ela serve para **criar uma ligação entre duas tabelas** e garantir a integridade dos dados.")


st.write("###")



st.subheader("💡 Exemplo:", anchor=False)

st.write("Queremos armazenar **informações de clientes** e seus **números de telefone**. Cada cliente pode ter vários telefones, mas cada telefone está associado a apenas um cliente. Para isso, usaremos uma chave estrangeira para relacionar as tabelas.")


st.write("###")



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


st.write("###")



st.write("**Explicação:**")

st.write("🟢 A coluna ```id_cliente``` na tabela **Telefones** é uma **chave estrangeira** que referencia a coluna ```id_cliente``` da tabela **Clientes**.")

st.write("🟢 Isso garante que só podemos adicionar um telefone se o ```id_cliente``` correspondente existir na tabela **Clientes**.")



st.write("###")



st.write("**Inserindo Dados de Exemplo:**")

code = '''
-- Inserindo dados na tabela Clientes
INSERT INTO Clientes (id_cliente, nome, email) VALUES
(1, 'João Silva', 'joao@email.com'),
(2, 'Maria Souza', 'maria@email.com');

-- Inserindo dados na tabela Telefones
INSERT INTO Telefones (id_telefone, id_cliente, numero) VALUES
(1, 1, '11999991111'),
(2, 1, '11988882222'),
(3, 2, '21977773333');
'''
st.code(code, language="sql")



st.write("###")



st.write("**Diagrama de Tabelas: `Clientes` e `Telefones`:**")

st.write("**Tabela `Clientes`:**")

st.markdown("""
| 🔑 **id_cliente** (PK) | **nome** CHAR(50) | **email** CHAR(100)  |
|:---------------------:|-------------------|----------------------|
| 1                     | João Silva        | joao@email.com       |
| 2                     | Maria Souza       | maria@email.com      |
""")

st.write("**Tabela `Telefones`:**")

st.markdown("""
| 🔑 **id_telefone** (PK) | 🔗 **id_cliente** (FK) → `Clientes` | **numero** CHAR(11)  |
|:-----------------------:|:--------------------------------:|----------------------|
| 1                       | 1                                | 11999991111          |
| 2                       | 1                                | 11988882222          |
| 3                       | 2                                | 21977773333          |
""")
