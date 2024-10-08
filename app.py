import streamlit as st

# Função para calcular o lucro da aposta Back
def calc_back_profit(stake_back, odd_back):
    return stake_back * (odd_back - 1)

# Função para calcular a responsabilidade da aposta Lay
def calc_lay_responsibility(stake_lay, odd_lay):
    return stake_lay * (odd_lay - 1)

# Função para calcular o resultado total da operação
def calc_total_result(stake_back, stake_lay, odd_back, odd_lay):
    back_profit = calc_back_profit(stake_back, odd_back)
    lay_responsibility = calc_lay_responsibility(stake_lay, odd_lay)

    # Resultados em caso de vitória
    result_back_winner = back_profit - stake_lay  # Lucro total se Back vencer
    result_lay_winner = stake_lay - back_profit  # Lucro total se Lay vencer

    return back_profit, lay_responsibility, result_back_winner, result_lay_winner

# Interface do Streamlit
st.title("Calculadora de Aposta Back e Lay")

# Inputs
stake_back = st.number_input("Valor Apostado no Back (R$):", min_value=0.0, step=0.01, value=0.04)
odd_back = st.number_input("Odd Back:", min_value=1.0, step=0.01, value=30.0)
stake_lay = st.number_input("Valor Apostado no Lay (R$):", min_value=0.0, step=0.01, value=0.09)
odd_lay = st.number_input("Odd Lay:", min_value=1.0, step=0.01, value=12.0)

# Botão para calcular
if st.button("Calcular"):
    back_profit, lay_responsibility, result_back_winner, result_lay_winner = calc_total_result(stake_back, stake_lay, odd_back, odd_lay)

    # Exibição dos resultados
    st.subheader("Resultados")
    st.write(f"**Lucro da Aposta Back:** R$ {back_profit:.2f}")
    st.write(f"**Responsabilidade da Aposta Lay:** R$ {lay_responsibility:.2f}")
    st.write(f"**Resultado se Back vencer:** R$ {result_back_winner:.2f}")
    st.write(f"**Resultado se Lay vencer:** R$ {result_lay_winner:.2f}")

    st.subheader("Resumo do Trade:")
    st.write(f"Você apostou R$ {stake_back:.2f} no Back com odd {odd_back}.")
    st.write(f"Você apostou R$ {stake_lay:.2f} no Lay com odd {odd_lay}.")
