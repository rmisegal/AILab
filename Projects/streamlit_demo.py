import streamlit as st
import pandas as pd
import numpy as np

st.title("AI Environment Demo")
st.write("Welcome to your portable AI development environment!")

# Sample data
data = pd.DataFrame({
    'x': np.random.randn(100),
    'y': np.random.randn(100)
})

st.subheader("Sample Chart")
st.line_chart(data)

st.subheader("Sample Data")
st.dataframe(data.head())
