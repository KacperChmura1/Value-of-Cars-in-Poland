from app import predict_car_value
import streamlit as st
import pandas as pd
# Loading Data
df_dum = pd.read_csv("df_app.csv")
df2 = pd.read_csv("C:/Users/kacpe/Desktop/programowanie/Programowanie_w_Python/Car_Value_Project/app.csv")
# Select Page
page = st.sidebar.selectbox("Explore Or Predict", {"Predict price of your car"})
if page == "Predict price of your car":
    predict_car_value(df2)


