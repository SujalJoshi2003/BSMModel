# Black–Scholes Option Pricing App 📈

An interactive **Streamlit web app** that calculates **European Call and Put option prices** using the **Black–Scholes (BS) model**.  
The app also visualizes option prices across different **stock price** and **volatility** ranges with heatmaps.  

---

## 🚀 Features
- Compute **Call & Put prices** with the BSM formula.  
- Interactive **Streamlit UI** with sidebar inputs.  
- Generate **heatmaps** showing how option values change:  
  - Stock Price (±10 around input)  
  - Volatility (±0.1 around input)  
- Hosted and easily accessible online.  

---

## 📊 Tech Stack
- **Python**
- **Streamlit** (web app framework)  
- **NumPy** (numerical calculations)  
- **Plotly Express** (interactive heatmaps & charts)  

---


---

## ⚡ How to Run Locally
1. Clone the repo:
   ```bash
   git clone https://github.com/SujalJoshi2003/BSMModel.git
   cd BSMModel
2.pip install -r requirements.txt

3.streamlit run app.py
