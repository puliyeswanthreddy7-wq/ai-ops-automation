import streamlit as st
import requests
import pandas as pd

BACKEND_URL = "http://localhost:8001"

st.title("AI Operations Dashboard")

if st.button("Run Data Pipeline"):
    res = requests.get(f"{BACKEND_URL}/run")
    data = res.json()
    df = pd.DataFrame(data)
    st.dataframe(df)
    st.bar_chart(df.set_index("sku")["revenue"])

q = st.text_input("Ask AI")
if st.button("Ask AI"):
    res = requests.get(f"{BACKEND_URL}/ask", params={"q": q})
    st.json(res.json())