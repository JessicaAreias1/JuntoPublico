import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Título do aplicativo
st.title("Aplicativo de Gráfico com Streamlit")

# Entrada de dados do usuário
st.header("Configuração do Gráfico")
num_points = st.slider("Número de Pontos", min_value=10, max_value=100, value=50)
line_color = st.selectbox("Cor da Linha", options=["blue", "red", "green", "black"])

# Gerar dados
x = np.linspace(0, 10, num_points)
y = np.sin(x)
# Criar gráfico
fig, ax = plt.subplots()
ax.plot(x, y, color=line_color)
ax.set_title("Gráfico de Seno")
ax.set_xlabel("X")
ax.set_ylabel("Y")

# Mostrar gráfico no Streamlit
st.pyplot(fig)

# Exibir dados da entrada
st.write(f"Número de Pontos: {num_points}")
st.write(f"Cor da Linha: {line_color}")
