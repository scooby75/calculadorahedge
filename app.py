import streamlit as st

# Função para calcular a responsabilidade da aposta Lay
def calc_lay_liability(stake_lay, odd_lay):
    return stake_lay * (odd_lay - 1)

# Função para calcular o valor da aposta Back para cobrir a responsabilidade da aposta Lay
def calc_back_stake(lay_liability, odd_back):
    return lay_liability / (odd_back - 1)

# Interface do Streamlit
st.title("Calculadora de Apostas Lay e Back (Proteção)")

st.sidebar.header("Insira os valores da aposta Lay")

# Inputs da aposta Lay
stake_lay = st.sidebar.number_input("Valor Apostado no Lay (R$):", min_value=0.0, step=0.01, value=0.04)
odd_lay = st.sidebar.number_input("Odd Lay:", min_value=1.0, step=0.01, value=25.0)

# Input da odd Back desejada para cobrir a aposta Lay
odd_back = st.sidebar.number_input("Odd Back para cobrir Lay:", min_value=1.0, step=0.01, value=12.0)

# Botão para calcular
if st.sidebar.button("Calcular"):
    # Calcular a responsabilidade da aposta Lay
    lay_liability = calc_lay_liability(stake_lay, odd_lay)
    
    # Calcular o valor da aposta Back para cobrir a responsabilidade da aposta Lay
    stake_back = calc_back_stake(lay_liability, odd_back)
    
    # Exibição dos resultados
    st.subheader("Resultados")
    
    st.write(f"**Responsabilidade da Aposta Lay:** R$ {lay_liability:.2f}")
    st.write(f"**Valor Apostado no Back:** R$ {stake_back:.2f} para cobrir a responsabilidade do Lay")

    # Simulação de resultado do trade
    st.subheader("Resumo do Trade:")
    
    st.write(f"Se a aposta Lay vencer, sua responsabilidade será de R$ {lay_liability:.2f}, coberta pela aposta Back.")
    st.write(f"Se a aposta Back vencer, você terá feito uma aposta suficiente para cobrir o risco do Lay.")

# Rodar a calculadora no Streamlit
