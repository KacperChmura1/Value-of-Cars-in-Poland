
import streamlit as st
from tensorflow.keras.models import load_model
import pandas as pd
from pickle import load
model = load_model("Model/model_app.h5")
df_dum = pd.read_csv("df_app.csv")
#Brands(to delete probably)
brands_10k = {'Opel', 'Audi', 'BMW', 'Volkswagen', 'Škoda', 'Ford', 'Renault',
       'Mercedes-Benz', 'Toyota', 'Seat', 'Nissan', 'Kia', 'Hyundai',
       'Peugeot', 'Mazda', 'Honda', 'Citroën', 'Fiat', 'Volvo', 'Dacia',
       'Suzuki', 'Mitsubishi', 'Jeep', 'MINI', 'Saab', 'Alfa Romeo',
       'Chevrolet', 'Subaru', 'Jaguar', 'Lexus', 'Chrysler', 'Smart',
       'Land Rover'}
brands_25k = {'Opel', 'Audi', 'BMW', 'Volkswagen', 'Škoda', 'Ford', 'Renault',
       'Mercedes-Benz', 'Toyota', 'Seat', 'Nissan', 'Kia', 'Hyundai',
       'Peugeot', 'Mazda', 'Honda', 'Citroën', 'Fiat', 'Volvo', 'Dacia',
       'Suzuki', 'Mitsubishi', 'Abarth', 'Jeep', 'MINI', 'Saab',
       'Alfa Romeo', 'Chevrolet', 'Subaru', 'Porsche', 'Jaguar', 'Lexus',
       'Chrysler', 'Smart', 'Land Rover'}
brands_50k = {'Opel', 'Audi', 'BMW', 'Volkswagen', 'Škoda', 'Ford', 'Renault',
       'Mercedes-Benz', 'Toyota', 'Seat', 'Nissan', 'Kia', 'Hyundai',
       'Peugeot', 'Mazda', 'Honda', 'Citroën', 'Fiat', 'Volvo', 'Dacia',
       'Suzuki', 'Abarth', 'Mitsubishi', 'Jeep', 'MINI', 'Saab',
       'Alfa Romeo', 'Chevrolet', 'Subaru', 'Porsche', 'Jaguar', 'Lexus',
       'Chrysler', 'Smart', 'Land Rover', 'Dodge'}

brands_100k = {'Opel', 'Audi', 'BMW', 'Volkswagen', 'Škoda', 'Ford', 'Renault',
       'Mercedes-Benz', 'Toyota', 'Seat', 'Nissan', 'Kia', 'Hyundai',
       'Peugeot', 'Mazda', 'Honda', 'Citroën', 'Fiat', 'Volvo', 'Dacia',
       'Suzuki', 'Abarth', 'Mitsubishi', 'Jeep', 'MINI', 'Saab',
       'Chevrolet', 'Subaru', 'Alfa Romeo', 'Porsche', 'Jaguar', 'Lexus',
       'Chrysler', 'Smart', 'Land Rover', 'Dodge'}

brands_200k = {'Opel', 'Audi', 'BMW', 'Volkswagen', 'Škoda', 'Ford', 'Renault',
       'Mercedes-Benz', 'Seat', 'Cupra', 'Toyota', 'Nissan', 'Kia',
       'Hyundai', 'Peugeot', 'Mazda', 'Honda', 'Citroën', 'Volvo',
       'Mitsubishi', 'Jeep', 'Suzuki', 'MINI', 'Subaru', 'Alfa Romeo',
       'Porsche', 'Jaguar', 'Lexus', 'Fiat', 'Chevrolet', 'Land Rover',
       'Chrysler', 'Dodge'}
#Models
Opel = ['Astra', 'Insignia', 'Corsa', 'Zafira', 'Meriva', 'Vectra',
       'Mokka', 'Vivaro', 'Grandland X', 'Crossland X', 'Combo', 'Signum',
       'Antara', 'Agila']
Audi = ['A4', 'A6', 'A3', 'A5', 'Q5', 'A8', 'Q7', 'Q3', 'A7', 'A1',
       'A6 Allroad', 'TT', 'Q2', 'A4 Allroad']
BMW = ['Seria 3', 'Seria 5', 'Seria 1', 'X3', 'X1', 'X5', 'Seria 7',
       'Seria 2', 'Seria 4', '3GT', 'Seria 6', 'X6', 'X2', 'X4']
Volkswagen = ['Golf', 'Passat', 'Polo', 'Tiguan', 'Touran', 'Caddy', 'Golf Plus',
       'Sharan', 'Jetta', 'up!', 'Arteon', 'Transporter', 'T-Roc',
       'Touareg', 'T-Cross', 'Caravelle', 'CC', 'Multivan', 'Scirocco',
       'New Beetle', 'Golf Sportsvan', 'Passat CC', 'Fox']
Škoda = ['Octavia', 'Fabia', 'Superb', 'RAPID', 'Scala', 'Karoq', 'Citigo',
       'Kodiaq', 'Roomster', 'Yeti']
Ford = ['Focus', 'Mondeo', 'Fiesta', 'S-Max', 'Kuga', 'C-MAX', 'Galaxy',
       'Mustang', 'Fusion', 'EcoSport', 'Puma', 'Grand C-MAX', 'EDGE',
       'KA', 'B-MAX', 'Focus C-Max', 'Transit', 'Tourneo Custom',
       'Ranger', 'Transit Custom']
Renault = ['Megane', 'Clio', 'Scenic', 'Laguna', 'Captur', 'Grand Scenic',
       'Kadjar', '5', 'Trafic', 'Espace', 'Talisman', 'Twingo', 'Modus',
       'Kangoo', 'Koleos', 'Grand Espace']
Mercedes_Benz = ['Klasa E', 'Klasa C', 'Klasa A', 'Klasa B', 'Klasa S', 'CLA', 'ML',
       'GLA', 'CLK', 'SL', 'CLS', 'GLC', 'Vito', 'W124 (1984-1993)', 'GL',
       'CL', 'GLK']
Seat = ['Leon', 'Ibiza', 'Altea', 'Arona', 'Altea XL', 'Alhambra',
       'Toledo', 'Ateca', 'Exeo']
Cupra = ['Leon', 'Ateca']
Toyota = ['Avensis', 'Yaris', 'Corolla', 'Auris', 'RAV4', 'C-HR', 'Aygo',
       'Verso', 'Corolla Verso', 'Prius', 'Camry', 'Land Cruiser']
Nissan = ['Qashqai', 'Juke', 'Micra', 'X-Trail', 'Note', 'Qashqai+2']
Kia = ['Ceed', 'Sportage', 'Picanto', 'Rio', 'Venga', 'Optima', 'Stonic',
       'XCeed', 'Sorento', 'Carens', "Pro_cee'd"]
Hyundai = ['I30', 'Tucson', 'ix35', 'i20', 'i40', 'Kona', 'Santa Fe', 'i10',
       'ix20', 'Elantra']
Peugeot = ['308', '508', '3008', '208', '207', '5008', '407', '2008', '307',
       'Partner', '206', 'Rifter', '301', '107']
Mazda = ['6', '3', 'CX-5', '5', '2', 'CX-3', 'CX-30']
Honda = ['Civic', 'CR-V', 'Accord', 'Jazz', 'HR-V']
Citroën = ['C5', 'C3', 'C4 Picasso', 'C4', 'Berlingo', 'C4 Grand Picasso',
       'C5 Aircross', 'C1', 'C3 Picasso', 'C3 Aircross', 'Xsara Picasso',
       'C4 Cactus', 'DS3', 'C2', 'DS4', 'DS5']
Volvo = ['XC 60', 'V40', 'V60', 'V50', 'S60', 'V70', 'XC 90', 'S80', 'S40',
       'C30', 'XC 40', 'V90', 'S90', 'XC 70']
Dacia = ['Duster', 'Sandero', 'Logan', 'Sandero Stepway', 'Lodgy', 'Dokker']
Suzuki = ['Swift', 'Vitara', 'SX4', 'SX4 S-Cross', 'Grand Vitara', 'Ignis',
       'Jimny']
Abarth = ['500', 'Grande Punto']
Mitsubishi = ['Outlander', 'ASX', 'Colt', 'Lancer', 'Space Star']
Jeep = ['Grand Cherokee', 'Renegade', 'Compass', 'Cherokee', 'Wrangler']
MINI = ['Cooper', 'Countryman', 'ONE', 'Cooper S', 'Clubman']
Saab = ['9-3']
Alfa_Romeo = ['159', 'Giulietta', 'Mito', 'Giulia']
Chevrolet = ['Cruze', 'Aveo', 'Captiva', 'Camaro', 'Spark']
Subaru = ['Forester', 'Legacy', 'Impreza', 'OUTBACK']
Porsche = ['Cayenne']
Jaguar = ['XF', 'XJ', 'XE']
Lexus = ['IS', 'NX', 'RX', 'GS']
Chrysler = ['Town & Country', 'Pacifica']
Smart = ['Fortwo']
Land_Rover = ['Range Rover Sport', 'Range Rover Evoque']
Fiat = ['Tipo', '500', 'Panda', 'Grande Punto', 'Bravo', 'Punto', 'Doblo',
       '500X', 'Punto Evo', 'Freemont', '500L', 'Sedici']
Dodge = ['Challenger']


brands_all = ['Opel', 'Audi', 'BMW', 'Volkswagen', 'Škoda', 'Ford', 'Renault',
       'Mercedes-Benz', 'Toyota', 'Seat', 'Cupra', 'Nissan', 'Kia',
       'Hyundai', 'Peugeot', 'Mazda', 'Honda', 'Citroën', 'Fiat', 'Volvo',
       'Dacia', 'Suzuki', 'Abarth', 'Mitsubishi', 'Jeep', 'MINI', 'Saab',
       'Alfa Romeo', 'Chevrolet', 'Subaru', 'Porsche', 'Jaguar', 'Lexus',
       'Chrysler', 'Smart', 'Land Rover', 'Dodge']

models_list = [Opel, Audi, BMW, Volkswagen, Škoda, Ford, Renault,
       Mercedes_Benz, Toyota, Seat, Cupra, Nissan, Kia,
       Hyundai, Peugeot, Mazda, Honda, Citroën, Fiat, Volvo,
       Dacia, Suzuki, Abarth, Mitsubishi, Jeep, MINI, Saab,
       Alfa_Romeo, Chevrolet, Subaru, Porsche, Jaguar, Lexus,
       Chrysler, Smart, Land_Rover, Dodge]
production_year = {2015, 2006, 2010, 2007, 2008, 2005, 2013, 2011, 2002, 2018, 2017,
       2001, 2003, 2012, 2004, 2014, 2016, 1999, 2019, 2009, 2020, 1998,
       2000, 1994, 1993, 2021, 1997, 1995, 1996, 1975, 1991, 1992, 1987,
       1990, 1980, 1988, 1989, 1982, 1985, 1983, 1986, 1978, 1977, 1979,
       1981, 1984, 1973, 1976, 1966, 1970, 1971, 1968, 1963, 1965, 1967,
       1964, 1972, 1969, 1961, 1974}

def model_selection(brand):
    for i in range(0,len(brands_all)):
       if brand == brands_all[i]:
            model_c = st.selectbox("Vehicle model", models_list[i])
            return model_c

st.title("Car Value Predictor")
page = 0
#page = st.selectbox("Price Range", {"0-10k","10k-25k","25k-50k","50k-100k","100k-200k"})
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
doors = st.selectbox("Doors Number", {5.,  3.,  2.,  4., 55.,  7.,  6.,  1.,  9.})
colour = st.selectbox("Colour", {'red', 'green', 'black', 'silver', 'blue', 'gray', 'white','burgundy', 'other', 'beige', 'brown', 'golden', 'yellow','violet'})
features = 30
ok = st.button("Calculate Price")

if ok:
       car_df = pd.DataFrame(data = [[0, condition, brand, model_c, year, millage_km, power_hp, displacement_cm3,fuel_type, drive, transmission, doors, colour, features]], columns =
       ['Price', 'Condition', 'Vehicle_brand', 'Vehicle_model',
       'Production_year', 'Mileage_km', 'Power_HP', 'Displacement_cm3',
       'Fuel_type', 'Drive', 'Transmission', 'Doors_number', 'Colour',
       'Features'] )
       #model.predic([[condition,brand,year,millage_km,pow]])

       car_dum = pd.DataFrame(car_df)
       car_dum = pd.get_dummies(car_dum)
       df_dum = df_dum.append(car_dum).fillna(0)
       
       scaler = load(open('Scalers/scaler_app.pkl', 'rb'))
       X_car = df_dum.drop(["Price","Unnamed: 0"], axis = 1)
       # jeden feature za duzo
       to_pred = scaler.transform(X_car)
       

       car_price = model.predict(to_pred)[-1]
       true_value = f'<p style="font-family:Courier; color:Green; font-size: 30px;">Predicted Value: {round(car_price[0])}PLN</p>'
       st.markdown(true_value, unsafe_allow_html=True)