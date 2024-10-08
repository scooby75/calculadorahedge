import streamlit as st

def calcular_responsabilidade(odd_lay, valor_apostado):
    # Calcula a responsabilidade da aposta Lay
    responsabilidade = valor_apostado * (odd_lay - 1)
    return responsabilidade

# Título da aplicação
st.title("Calculadora de Responsabilidade de Apostas")

# Inputs para odd Back, valor apostado e odd Lay
odd_back = st.number_input("Informe a odd Back:", min_value=1.0, format="%.2f")
valor_apostado = st.number_input("Informe o valor apostado:", min_value=0.01, format="%.2f")
odd_lay = st.number_input("Informe a odd Lay:", min_value=1.0, format="%.2f")

# Botão para calcular
if st.button("Calcular"):
    responsabilidade = calcular_responsabilidade(odd_lay, valor_apostado)
    st.write(f"A responsabilidade da aposta Lay é R${responsabilidade:.2f}.")
