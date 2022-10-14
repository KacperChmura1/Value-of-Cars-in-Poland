from app import predict_car_value
from explore import explore
import streamlit as st
import pandas as pd
#Pages choose
page = st.sidebar.selectbox("Explore Or Predict", {"Predict price of your car","Explore some informations"})
df_dum = pd.read_csv("df_app.csv")
df2 = pd.read_csv("xxx.csv")
if page == "Predict price of your car":
    predict_car_value(df2)
elif page == "Explore some informations":
    explore(df_dum)



