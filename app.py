import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("premium_model.pkl")

st.set_page_config(page_title="Health Insurance Premium Predictor")

st.title("🏥 Health Insurance Premium Predictor")

# User Inputs
age = st.number_input("Age", min_value=18, max_value=100, value=25)

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
    ["High", "Medium", "Low"]
)

stress = st.selectbox(
    "Stress Level",
    ["High", "Medium", "Low"]
)

dependants = st.number_input(
    "Number of Dependants",
    min_value=0,
    max_value=10,
    value=0
)

bmi = st.selectbox(
    "BMI Category",
    ["Normal", "Overweight", "Obesity", "Underweight"]
)

smoking = st.selectbox(
    "Smoking Status",
    ["No Smoking", "Occasional", "Regular"]
)

employment = st.selectbox(
    "Employment Status",
    ["Salaried", "Self-Employed", "Freelancer"]
)

income_level = st.selectbox(
    "Income Level",
    ["<10L", "10L - 25L", "25L - 40L", ">40L"]
)

income = st.number_input(
    "Income (Lakhs)",
    min_value=1,
    max_value=100,
    value=10
)

medical = st.selectbox(
    "Medical_History",
    [
        "No Disease",
        "Diabetes",
        "High blood pressure",
        "Heart disease",
        "Thyroid",
        "Diabetes & BP"
    ]
)

insurance = st.selectbox(
    "Insurance Plan",
    ["Bronze", "Silver", "Gold"]
)

if st.button("Predict Premium"):

    # Encoding
    # gender = 1 if gender == "Male" else 0
    # marital = 1 if marital == "Married" else 0

    gender_map = {
    "Female": 0,
    "Male": 1
}
    region_map = {
    "Northeast": 0,
    "Northwest": 1,
    "Southeast": 2,
    "Southwest": 3
}
    marital_map = {
    "Married": 0,
    "Unmarried": 1
}
    
    physical_map = {
    "High": 0,
    "Low": 1,
    "Medium": 2
}
    stress_map = {
    "High": 0,
    "Low": 1,
    "Medium": 2
}
    bmi_map = {
    "Normal": 0,
    "Obesity": 1,
    "Overweight": 2,
    "Underweight": 3
}
    smoking_map = {
    "No Smoking": 0,
    "Occasional": 1,
    "Regular": 2
}
    employment_map = {
    "Freelancer": 0,
    "Salaried": 1,
    "Self-Employed": 2
}
    
    income_level_map = {
    "10L - 25L": 0,
    "25L - 40L": 1,
    "<10L": 2,
    "> 40L": 3
}
    medical_map = {
    "Diabetes": 0,
    "Diabetes & Heart disease": 1,
    "Diabetes & High blood pressure": 2,
    "Diabetes & Thyroid": 3,
    "Heart disease": 4,
    "High blood pressure": 5,
    "High blood pressure & Heart disease": 6,
    "No Disease": 7,
    "Thyroid": 8
}

    plan_map = {
    "Bronze": 0,
    "Gold": 1,
    "Silver": 2
}
    physical_score = {
    "High": 0,
    "Medium": 1,
    "Low": 4
}

    stress_score = {
    "High": 4,
    "Medium": 1,
    "Low": 0
}

    # Lifestyle Risk Score
    lifestyle_risk_score = (
    physical_score[physical]
    + stress_score[stress]
)

    # Feature order MUST match the training data
    input_data = pd.DataFrame([[
    age,
    gender_map[gender],
    region_map[region],
    marital_map[marital],
    physical_map[physical],
    stress_map[stress],
    dependants,
    bmi_map[bmi],
    smoking_map[smoking],
    employment_map[employment],
    income_level_map[income_level],
    income,
    medical_map[medical],
    plan_map[insurance],
    lifestyle_risk_score
]], columns=[
    "Age",
    "Gender",
    "Region",
    "Marital_status",
    "Physical_Activity",
    "Stress_Level",
    "Number Of Dependants",
    "BMI_Category",
    "Smoking_Status",
    "Employment_Status",
    "Income_Level",
    "Income_Lakhs",
    "Medical History",
    "Insurance_Plan",
    "Lifestyle_Risk_Score"
])

    prediction = model.predict(input_data)

    st.success(f"Estimated Annual Premium: ₹ {prediction[0]:,.0f}")