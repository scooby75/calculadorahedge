import streamlit as st

def calcular_aposta_back(odd_lay, responsabilidade):
    # Calcula o valor da aposta Lay
    valor_aposta_lay = responsabilidade / (odd_lay - 1)
    return valor_aposta_lay

def mostrar_resultados(odd_lay, responsabilidade, odd_back):
    valor_aposta_lay = calcular_aposta_back(odd_lay, responsabilidade)
    
    # Calcula o valor da aposta Back para cobrir a responsabilidade
    valor_aposta_back = responsabilidade / (odd_back - 1)

    st.write(f"Para uma responsabilidade de R${responsabilidade:.2f} e odd Lay de {odd_lay}:")
    st.write(f"Você deve apostar R${valor_aposta_lay:.4f} no Lay.")
    st.write(f"Para odds Back de {odd_back}, aposte R${valor_aposta_back:.4f} no Back para cobrir a responsabilidade.")

# Título da aplicação
st.title("Calculadora de Apostas")

# Inputs para odd Lay, responsabilidade e odd Back
odd_lay = st.number_input("Informe a odd Lay:", min_value=1.0, format="%.2f")
responsabilidade = st.number_input("Informe a responsabilidade desejada:", min_value=0.01, format="%.2f")
odd_back = st.number_input("Informe a odd Back após movimentação:", min_value=1.0, format="%.2f")

# Botão para calcular
if st.button("Calcular"):
    mostrar_resultados(odd_lay, responsabilidade, odd_back)
