from app import predict_car_value
from explore import explore
import streamlit as st
import pandas as pd
#Loading Data
df_dum = pd.read_csv("df_app.csv")
df2 = pd.read_csv("Data/app.csv")
#Select Page
page = st.sidebar.selectbox("Explore Or Predict", {"Predict price of your car","Explore some informations"})
if page == "Predict price of your car":
    predict_car_value(df2)
elif page == "Explore some informations":
    explore(df_dum)



