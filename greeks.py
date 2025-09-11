import streamlit as st
import math

def greeksCal(S, T, r, K, sigma, d):
    st.subheader("Option Greeks")

    st.info(
        f"**Inputs:**\n"
        f"- Stock Price: {S}\n"
        f"- Strike Price: {K}\n"
        f"- Maturity: {T} years\n"
        f"- Risk-Free Rate: {r*100}%\n"
        f"- Volatility: {sigma*100}%\n"
        f"- Dividend Yield: {d*100}%"
    )

    d1 = (math.log(S / K)+(r-d+ 0.5*sigma**2)*T)/(sigma*(T**0.5))
    d2 = d1 - sigma*(T**0.5)
    N_d1 = 0.5 * (1 + math.erf(d1 /(2**0.5)))
    N_d2 = 0.5 * (1 + math.erf(d2 /(2**0.5)))

    delta_call = math.exp(-d*T)*N_d1
    delta_put = math.exp(-d*T)*(N_d1 - 1)

    gamma = (math.exp(-d*T) * (1 / (S * sigma * math.sqrt(T))) * (1 / math.sqrt(2 * math.pi)) * math.exp(-0.5 * d1**2))
    vega = S * math.exp(-d*T) * math.sqrt(T) * (1 / math.sqrt(2 * math.pi)) * math.exp(-0.5 * d1**2)

    theta_call = (- (S * sigma * math.exp(-d*T) * (1 / (2 * math.sqrt(T))) * (1 / math.sqrt(2 * math.pi)) * math.exp(-0.5 * d1**2))
                    - r * K * math.exp(-r * T) * N_d2)
    theta_put = (- (S * sigma * math.exp(-d*T) * (1 / (2 * math.sqrt(T))) * (1 / math.sqrt(2 * math.pi)) * math.exp(-0.5 * d1**2))
                    + r * K * math.exp(-r * T) * (1 - N_d2))

    st.markdown("###  Call Greeks")
    c1, c2, c3 = st.columns(3)
    with c1: st.metric("Delta", f"{delta_call:.4f}")
    with c2: st.metric("Gamma", f"{gamma:.4f}")
    with c3: st.metric("Theta (per day)", f"{theta_call/365:.4f}")
    
    st.markdown("###  Put Greeks")
    p1, p2, p3 = st.columns(3)
    with p1: st.metric("Delta", f"{delta_put:.4f}")
    with p2: st.metric("Gamma", f"{gamma:.4f}")
    with p3: st.metric("Theta (per day)", f"{theta_put/365:.4f}")

    st.markdown("###  Common Greeks")
    v1, v2 = st.columns(2)
    with v1: st.metric("Vega (per 1%)", f"{vega/100:.4f}")
    with v2: st.metric("d1 / d2", f"{d1:.2f} / {d2:.2f}")
