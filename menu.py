from app import predict_car_value
from explore import explore
import streamlit as st
import pandas as pd
#Pages choose
page = st.sidebar.selectbox("Explore Or Predict", {"Predict price of your car","Explore some informations"})
df_dum = pd.read_csv("df_app.csv")
if page == "Predict price of your car":
    predict_car_value(df_dum)
elif page == "Explore some informations":
    explore(df_dum)



