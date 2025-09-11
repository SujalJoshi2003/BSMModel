import streamlit as st
from modelcal import inputBasedCalculator
from varCoolCal import variationCal
from greeks import greeksCal

callValue=0
putValue=0
stockVar,maturityVar,riskVar,strikeVar,volVar,divVar=1,1,1,1,1,1
heatVar = False


st.title("Black Scholes Option Pricing Calculator")

with st.sidebar:
    st.text("Made by Sujal Joshi ")
    st.markdown(
    """
    <a href="https://www.linkedin.com/in/sujal-joshi-aa432a232" target="_blank">
        <div style="
            display:inline-block;
            background-color:#0077b5;
            color:white;
            padding:10px 20px;
            border-radius:8px;
            text-align:center;
            text-decoration:none;
            font-weight:bold;
            font-size:16px;
        ">
            LinkedIn
        </div>
    </a>
    """,
    unsafe_allow_html=True
   )
    st.text("")
    st.text("")
    stockPrice = st.number_input("Stock Price ", min_value=0.0, value=100.0, step=1.0)
    maturity = st.number_input("Maturity (in years) ",  value=1.0, step=0.1)
    strikePrice = st.number_input("Strike Price ", min_value=0.0, value=100.0, step=1.0)
    riskFreeRate = st.number_input("Risk Free Rate (in %) ", min_value=0.0, value=5.0,step=0.1)
    volatility = st.number_input("Volatility (in %) ", min_value=0.0, value=20.0, step=0.1)
    dividendYield = st.number_input("Dividend Yield (in %) ",  value=0.0, step=0.1)
    stockVar,maturityVar,riskVar,strikeVar,volVar,divVar=stockPrice,maturity,riskFreeRate,strikePrice,volatility,dividendYield

    if st.button("Calculate"):
        heatVar = True
        call, put = inputBasedCalculator(stockPrice, strikePrice, maturity, riskFreeRate/100, volatility/100,dividendYield/100)
        callValue,putValue=call,put

st.text("")  
st.text("Call and Put values for input given in sidebar are:")
col1 , col2 = st.columns(2)
with col1:
    st.success("Call:\n" + str(callValue))
with col2:
    st.error(f"Put:\n{putValue}")

st.text("")
tabs1,tabs2 = st.tabs(["Heatmap","Greeks"])
with tabs1:
    st.text(f"Heatmap presented with input Stock price : {stockPrice}, and Volatility : {volatility}% , with few different values around it")
    st.info("Note: Heatmap is generated only when Calculate button is pressed")
    if stockVar != 1 and heatVar:
        variationCal(stockVar,maturityVar,riskVar/100,strikeVar,volVar/100,divVar/100)
with tabs2:
    greeksCal(stockVar,maturityVar,riskVar/100,strikeVar,volVar/100,divVar/100)
        