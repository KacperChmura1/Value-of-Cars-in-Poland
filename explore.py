import streamlit as st
import pandas as pd
df_dum = pd.read_csv("df_app.csv")
def explore(df_dum):
    st.title("Most Populars Brands in Poland")
    st.image("Plots/output1.png")
    st.title("Most Populars Models in Poland")
    st.image("Plots/output2.png")
    st.title("Most Populars type of fuel in Poland")
    st.image("Plots/output3.png")
    st.title("Most Populars price range in Poland")
    st.image("Plots/output4.png")
    st.title("Most Populars car color in Poland")
    st.image("Plots/output5.png")
      