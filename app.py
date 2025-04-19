import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("house_price_model.pkl")

st.title("California House Price Predictor 🏡")

st.write("Enter the neighborhood features:")

# Input fields
MedInc = st.number_input("Median Income (10k USD)", value=5.0)
HouseAge = st.number_input("House Age", value=30)
AveRooms = st.number_input("Average Rooms", value=6.0)
AveBedrms = st.number_input("Average Bedrooms", value=1.2)
Population = st.number_input("Population", value=900)
AveOccup = st.number_input("Average Occupants", value=3.0)
Latitude = st.number_input("Latitude", value=34.25)
Longitude = st.number_input("Longitude", value=-118.45)

# Predict when button is clicked
if st.button("Predict Price"):
    input_data = pd.DataFrame([{
        'MedInc': MedInc,
        'HouseAge': HouseAge,
        'AveRooms': AveRooms,
        'AveBedrms': AveBedrms,
        'Population': Population,
        'AveOccup': AveOccup,
        'Latitude': Latitude,
        'Longitude': Longitude
    }])

    prediction = model.predict(input_data)[0]
    st.success(f"🏠 Predicted House Price: ${prediction * 100000:.2f}")
