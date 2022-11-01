from ann import predict_car_value
import streamlit as st
import pandas as pd
# Loading Data
df_dum = pd.read_csv("df_app.csv")
df2 = pd.read_csv("app.csv")
# Select Page
page = st.sidebar.selectbox("Explore Or Predict", {"ANN","ML"})
if page == "ANN":
    predict_car_value(df2)
elif page == "ML":
    predict_car_value(df2)


