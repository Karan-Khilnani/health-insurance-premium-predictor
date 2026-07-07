import streamlit as st
import pandas as pd
import joblib

model = joblib.load("premium_model.pkl")

st.title("Health Insurance Premium Predictor")

age = st.number_input("Age", 18, 100)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

region = st.selectbox(
    "Region",
    ["Northeast", "Northwest", "Southeast", "Southwest"]
)

marital = st.selectbox(
    "Marital Status",
    ["Married", "Unmarried"]
)

physical = st.selectbox(
    "Physical Activity",
    ["Low", "Medium", "High"]
)

stress = st.selectbox(
    "Stress Level",
    ["Low", "Medium", "High"]
)

dependants = st.number_input(
    "Dependants",
    0,
    10
)

income = st.number_input(
    "Income Lakhs",
    1,
    100
)

if st.button("Predict"):

    gender = 1 if gender=="Male" else 0
    marital = 1 if marital=="Married" else 0

    region_map = {
        "Northeast":0,
        "Northwest":1,
        "Southeast":2,
        "Southwest":3
    }

    physical_map = {
        "Low":0,
        "Medium":1,
        "High":2
    }

    stress_map = {
        "Low":0,
        "Medium":1,
        "High":2
    }

    input_data = [[

        age,

        gender,

        region_map[region],

        marital,

        physical_map[physical],

        stress_map[stress],

        dependants,

        1,

        1,

        1,

        1,

        income,

        1,

        1

    ]]

    prediction = model.predict(input_data)

    st.success(

        f"Estimated Premium ₹ {prediction[0]:,.0f}"

    )