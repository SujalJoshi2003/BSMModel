import numpy as np
import plotly.express as px
from modelcal import inputBasedCalculator
import streamlit as st

def variationCal(S,T,r,K,sigma):
    sRange = np.linspace(S - 10, S + 10, 20)
    sigmaRange = np.linspace(sigma - 0.1, sigma + 0.1, 20)

    call_grid = np.zeros((len(sigmaRange), len(sRange)))
    put_grid  = np.zeros((len(sigmaRange), len(sRange)))

    for i, sigma in enumerate(sigmaRange):
        for j, S in enumerate(sRange):
            call, put = inputBasedCalculator(S, K, T, r, sigma)
            call_grid[i, j] = call
            put_grid[i, j] = put

    st.subheader("Call Option Heatmap")
    fig_call = px.imshow(call_grid,
                     x=np.round(sRange, 2),
                     y=np.round(sigmaRange, 3),
                     labels=dict(x="Stock Price", y="Volatility", color="Call Price"),
                     origin="lower",
                     aspect="auto")
    st.plotly_chart(fig_call, use_container_width=True)

    st.subheader("Put Option Heatmap")
    fig_put = px.imshow(put_grid,
                    x=np.round(sRange, 2),
                    y=np.round(sigmaRange, 3),
                    labels=dict(x="Stock Price", y="Volatility", color="Put Price"),
                    origin="lower",
                    aspect="auto")
    st.plotly_chart(fig_put, use_container_width=True)