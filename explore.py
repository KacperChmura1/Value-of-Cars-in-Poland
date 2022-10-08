import streamlit as st
import pandas as pd
import plotly.graph_objects as go
df_dum = pd.read_csv("df_app.csv")
night_colors = [
    "rgb(253, 231, 37)",
    "rgb(181, 222, 43)",
    "rgb(110, 206, 88)",
    "rgb(53, 183, 121)",
    "rgb(31, 158, 137)",
    "rgb(38, 130, 142)",
    "rgb(49, 104, 142)",
    "rgb(62, 73, 137)",
    "rgb(72, 40, 120)",
    "rgb(68, 1, 84)"]
def explore(df_dum):

    df_pie = pd.read_csv("piechart.csv")
    # This dataframe has 244 lines, but 4 distinct values for `day`
    x = df_pie["Vehicle_brand_19"].value_counts().index
    y = df_pie["Vehicle_brand_19"].value_counts().values    
    fig = go.Figure(data=[go.Pie(labels=x, values=y, pull=[0.1,0,0,0,0,0,0,0,0],marker_colors=night_colors)])
    #fig = go.Figure(values=df_pie["Vehicle_brand_19"].value_counts().values, names=df_pie["Vehicle_brand_19"].value_counts().index,
    #            labels=img2,color_discrete_sequence=px.colors.sequential.Plasma)
    #fig = go.Figure(data=[go.Pie(labels=labels, values=values, pull=[0, 0, 0.2, 0])])
    st.title("Piechart with Brands")
    st.plotly_chart(fig)
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
    
      