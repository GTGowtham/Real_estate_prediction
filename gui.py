import streamlit as st
import pandas as pd
import joblib
import numpy as np
from PIL import Image  

# Load the trained model
model = joblib.load('model.pkl')

# Set Streamlit page configuration
st.set_page_config(page_title="Real Estate Price Prediction", page_icon="🏠", layout="centered")

# Display header image
image = Image.open("real_estate.jpeg")
st.image(image, caption="🏠 Real Estate Price Prediction", use_container_width=True)



# App description
st.write("Estimate your house price quickly and easily by providing square feet and some additional details.")

# Form for user inputs
st.markdown("### Enter Your House Details:")
ID=st.number_input("ID:",min_value=1, max_value=1000, value=1, step=1)
sq_feet = st.number_input("Square Feet:", min_value=50, max_value=3000, value=1000, step=1)
bedrooms = st.number_input("Bedrooms:", min_value=1, max_value=5, value=3, step=1)
bathrooms = st.number_input("Bathrooms:", min_value=1, max_value=3, value=2, step=1)
floors = st.number_input("Floors:", min_value=1, max_value=3, value=1, step=1)
years_build = st.number_input("Year Built:", min_value=1900, max_value=2022, value=2000, step=1)
garden = st.selectbox("Garden:", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
pool = st.selectbox("Pool:", options=[0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
garage_size = st.number_input("Garage Size (sq.ft):", min_value=10, max_value=500, value=200, step=1)
location = st.slider("Location Score (0 - 10):", min_value=0, max_value=10, value=7)
distance_center = st.number_input("Distance to Center (km):", min_value=0.1, max_value=50.0, value=5.0, step=0.1)

# Button for prediction
if st.button("Predict Price"):
    try:
        # Prepare input features
        input_features = np.array([[ID,sq_feet, bedrooms, bathrooms, floors, years_build, garden, pool, garage_size, location, distance_center]])
        
        # Make prediction
        predicted_price = model.predict(input_features)[0]
        
        # Display result
        st.success(f"The estimated price of your house is ${predicted_price:,.2f} USD")
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Footer
st.markdown("---")
st.markdown("Developed by **Gowtham**")

# Style customization
st.markdown(
    """
    <style>
    .stButton>button {
        color: white;
        background-color: #007BFF;
        border-radius: 8px;
        padding: 10px 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
