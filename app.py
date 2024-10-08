import streamlit as st

# Função para calcular o lucro da aposta Back
def calc_back_profit(stake_back, odd_back):
    return stake_back * (odd_back - 1)

# Função para calcular a responsabilidade da aposta Lay
def calc_lay_liability(stake_lay, odd_lay):
    return stake_lay * (odd_lay - 1)

# Função para sugerir a melhor odd Lay (um pouco menor que a odd Back) e o valor da aposta Lay
def suggest_lay(stake_back, odd_back):
    # Sugerimos uma odd Lay um pouco menor que a Back (para proteger o lucro)
    odd_lay = odd_back - 1
    
    # Cálculo do stake Lay para proteger a aposta Back
    # Queremos que o lucro do Lay cubra o lucro do Back
    stake_lay = calc_back_profit(stake_back, odd_back) / (odd_lay - 1)
    
    return odd_lay, stake_lay

# Interface do Streamlit
st.title("Calculadora de Apostas Back e Lay (com sugestão de Lay)")

st.sidebar.header("Insira os valores da aposta")

# Inputs da aposta Back
stake_back = st.sidebar.number_input("Valor Apostado no Back (R$):", min_value=0.0, step=0.01)
odd_back = st.sidebar.number_input("Odd Back:", min_value=1.0, step=0.01)

# Botão para calcular
if st.sidebar.button("Calcular"):
    # Sugerir a melhor odd e stake Lay
    suggested_odd_lay, suggested_stake_lay = suggest_lay(stake_back, odd_back)
    
    # Calcular lucro do Back e responsabilidade do Lay
    back_profit = calc_back_profit(stake_back, odd_back)
    lay_liability = calc_lay_liability(suggested_stake_lay, suggested_odd_lay)
    lay_profit = suggested_stake_lay
    
    # Exibição dos resultados
    st.subheader("Resultados")
    
    st.write(f"**Lucro Potencial do Back:** R$ {back_profit:.2f}")
    
    st.write(f"**Odd Lay Sugerida:** {suggested_odd_lay:.2f}")
    
    st.write(f"**Valor Apostado no Lay (sugerido):** R$ {suggested_stake_lay:.2f}")
    
    st.write(f"**Responsabilidade do Lay:** R$ {lay_liability:.2f}")
    
    st.write(f"**Lucro Potencial do Lay:** R$ {lay_profit:.2f}")

    # Simulação de resultado do trade
    st.subheader("Resumo do Trade:")
    
    st.write(f"Se a aposta Back vencer, seu lucro será de R$ {back_profit - lay_liability:.2f} após cobrir a responsabilidade da aposta Lay.")
    
    st.write(f"Se a aposta Lay vencer, seu lucro será de R$ {lay_profit:.2f} e você perderá a aposta Back de R$ {stake_back:.2f}.")

# Rodar a calculadora no Streamlit
