from enum import unique
import streamlit as st
from tensorflow.keras.models import load_model
import pandas as pd
from pickle import load
import numpy as np
from datetime import datetime
#Lists Import
from important_lists import * 
#Data and Model Import
model = load_model("Model/model_with_features_under_200k.h5")
df2 = pd.read_csv("app.csv")

def model_selection(brand):
    for i in range(0,len(brands_all)):
       if brand == brands_all[i]:
            model_c = st.selectbox("Vehicle model", models_list[i])
            return model_c
def predict_car_value_ann(df2):
       st.title("Car Value Predictor")
       page = 0
       condition = st.selectbox("New or Used", {"New","Used"})
       brand = st.selectbox("Vehicle Brand", brands_all)
       model_c = model_selection(brand)
       year = st.selectbox("Production Year", production_year)
       millage_km = st.number_input("Millage(km)",step = 100)
       power_hp = st.number_input("Power(hp)",step = 1)
       displacement_cm3 = 	st.number_input("Displacement(cm3)",step = 1)
       fuel_type = st.selectbox("Fuel Type", {'Diesel', 'Gasoline', 'Gasoline + LPG', 'Hybrid', 'Gasoline + CNG'})
       drive = st.selectbox("Drive", {'Front wheels', 'Rear wheels', '4x4 (permanent)','4x4 (attached automatically)', '4x4 (attached manually)'})
       transmission = st.selectbox("Transmission", {'Manual', 'Automatic'})
       type = st.selectbox("Type", {'station_wagon', 'compact', 'sedan', 'SUV', 'city_cars', 'minivan',
       'coupe', 'small_cars', 'convertible'})
       doors = st.selectbox("Doors Number", {5.,  3.,  2.,  4., 55.,  7.,  6.,  1.,  9.})
       colour = st.selectbox("Colour", {'red', 'green', 'black', 'silver', 'blue', 'gray', 'white','burgundy', 'other', 'beige', 'brown', 'golden', 'yellow','violet'})
       features2 = st.multiselect("Features",unique_features)
       month = int(datetime.now().month)
       to_day_year = int(datetime.now().year)

       x = 0
       i = 0
       y = []
       for el in unique_features:
              for i in range(0,len(features2)):
                     if el in features2:
                            x = 1
                     else:
                            x = 0
              y.append(x)    
       ok = st.button("Calculate Price")

       if ok:  
              car_df = pd.DataFrame(data = [[0, condition, brand, model_c, year, millage_km, power_hp, displacement_cm3,fuel_type, drive, transmission,type, doors, colour,y[0],y[1],y[2],y[3],y[4],y[5],y[6],y[7],y[8],y[9],y[10],
                    y[11],y[12],y[13],y[14],y[15],y[16],y[17],y[18],y[19],y[20],y[21],y[22],y[23],y[24],y[25],y[26],y[27],y[28],y[29],y[30],y[31],y[32],y[33],y[34],y[35],y[36],y[37],y[38],y[39],y[40],y[41],y[42],y[43],y[44],y[45],
                    y[46],y[47],y[48],y[49],y[50],y[51],y[52],y[53],y[54],y[55],y[56],y[57],y[58],y[59],y[60],y[61],y[62],y[63],y[64],y[65],y[66],y[67],y[68],y[69],
                    month,to_day_year]],columns = columns)
              df2 = df2.append(car_df).fillna(0)
              car_dum = pd.get_dummies(df2,drop_first=True)
              scaler = load(open('Scalers/scaler_with_features.pkl', 'rb'))
              X_car = car_dum.drop(["Price",'Unnamed: 0'], axis = 1)
              X_car = X_car.iloc[[1,-1]]
              to_pred = scaler.transform(X_car)
              car_price = model.predict(to_pred)[-1]
              true_value = f'<p style="font-family:Courier; color:Green; font-size: 30px;">Predicted Value: {round(car_price[0])}PLN</p>'
              st.markdown(true_value, unsafe_allow_html=True)