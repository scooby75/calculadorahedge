import streamlit as st

# Função para calcular o lucro da aposta Back
def calc_back_profit(stake_back, odd_back):
    return stake_back * (odd_back - 1)

# Função para calcular a odd Lay e a stake Lay que cobrirão a aposta Back e ainda gerem lucro
def calc_lay_to_cover(stake_back, odd_back, desired_profit):
    back_profit = calc_back_profit(stake_back, odd_back)
    
    # Total que queremos cobrir
    total_to_cover = stake_back + desired_profit

    # Definindo uma odd Lay, que pode ser um pouco menor que a odd Back
    odd_lay = odd_back - 1  # Ajustável conforme estratégia

    # Calculando a stake Lay necessária
    stake_lay = total_to_cover / (odd_lay - 1)
    return odd_lay, stake_lay

# Função para calcular o lucro total da operação
def calc_total_profit(lay_stake, odd_lay, back_profit):
    # Lucro da aposta Lay
    lucro_lay = lay_stake
    return back_profit - lucro_lay

# Interface do Streamlit
st.title("Calculadora de Aposta Back e Lay")

st.sidebar.header("Insira os valores da aposta Back")

# Inputs da aposta Back
stake_back = st.sidebar.number_input("Valor Apostado no Back (R$):", min_value=0.0, step=0.01, value=0.04)
odd_back = st.sidebar.number_input("Odd Back:", min_value=1.0, step=0.01, value=26.0)
desired_profit = st.sidebar.number_input("Lucro desejado (R$):", min_value=0.0, step=0.01, value=0.01)

# Botão para calcular
if st.sidebar.button("Calcular"):
    # Calcular a odd e stake do Lay que cobriria a aposta Back com lucro
    odd_lay, stake_lay = calc_lay_to_cover(stake_back, odd_back, desired_profit)
    
    # Calcular o lucro total da operação
    back_profit = calc_back_profit(stake_back, odd_back)
    total_profit = calc_total_profit(stake_lay, odd_lay, back_profit)
    
    # Exibição dos resultados
    st.subheader("Resultados")
    
    st.write(f"**Lucro da Aposta Back:** R$ {back_profit:.2f}")
    st.write(f"**Odd Lay Sugerida:** {odd_lay:.2f}")
    st.write(f"**Valor Apostado no Lay:** R$ {stake_lay:.2f}")
    st.write(f"**Lucro Total da Operação:** R$ {total_profit:.2f}")
    
    st.subheader("Resumo do Trade:")
    st.write(f"Você apostou R$ {stake_back:.2f} no Back com odd {odd_back}.")
    st.write(f"A aposta Lay sugerida é de R$ {stake_lay:.2f} na odd {odd_lay:.2f} para garantir um lucro total de R$ {total_profit:.2f}.")
