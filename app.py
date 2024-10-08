import streamlit as st

# Função para calcular o lucro da aposta Back
def calc_back_profit(stake_back, odd_back):
    return stake_back * (odd_back - 1)

# Função para calcular a responsabilidade da aposta Lay
def calc_lay_liability(stake_lay, odd_lay):
    return stake_lay * (odd_lay - 1)

# Função para sugerir a melhor odd Lay e o valor da aposta Lay
def suggest_lay(stake_back, odd_back, desired_lay_odd):
    # Calcular o lucro da aposta Back
    back_profit = calc_back_profit(stake_back, odd_back)
    
    # Calcular o valor da aposta Lay para cobrir o lucro da aposta Back
    stake_lay = back_profit / (desired_lay_odd - 1)
    
    # Calcular a responsabilidade da aposta Lay
    lay_liability = calc_lay_liability(stake_lay, desired_lay_odd)
    
    return desired_lay_odd, stake_lay, lay_liability

# Interface do Streamlit
st.title("Calculadora de Apostas Back e Lay (Ajustada para Dobbling)")

st.sidebar.header("Insira os valores da aposta Back e a odd Lay desejada")

# Inputs da aposta Back
stake_back = st.sidebar.number_input("Valor Apostado no Back (R$):", min_value=0.0, step=0.01, value=0.04)
odd_back = st.sidebar.number_input("Odd Back:", min_value=1.0, step=0.01, value=25.0)

# Input da odd Lay desejada
desired_lay_odd = st.sidebar.number_input("Odd Lay desejada:", min_value=1.0, step=0.01, value=12.0)

# Botão para calcular
if st.sidebar.button("Calcular"):
    # Sugerir a melhor odd Lay e calcular os valores
    suggested_odd_lay, suggested_stake_lay, lay_liability = suggest_lay(stake_back, odd_back, desired_lay_odd)
    
    # Calcular o lucro da aposta Back
    back_profit = calc_back_profit(stake_back, odd_back)
    
    # Exibição dos resultados
    st.subheader("Resultados")
    
    st.write(f"**Lucro Potencial do Back:** R$ {back_profit:.2f}")
    st.write(f"**Odd Lay Sugerida:** {suggested_odd_lay:.2f}")
    st.write(f"**Valor Apostado no Lay (sugerido):** R$ {suggested_stake_lay:.2f}")
    st.write(f"**Responsabilidade do Lay:** R$ {lay_liability:.2f}")

    # Simulação de resultado do trade
    st.subheader("Resumo do Trade:")
    
    st.write(f"Se a aposta Back vencer, seu lucro será de R$ {back_profit - lay_liability:.2f} após cobrir a responsabilidade da aposta Lay.")
    
    st.write(f"Se a aposta Lay vencer, seu lucro será de R$ {suggested_stake_lay:.2f} e você perderá a aposta Back de R$ {stake_back:.2f}.")

# Rodar a calculadora no Streamlit
