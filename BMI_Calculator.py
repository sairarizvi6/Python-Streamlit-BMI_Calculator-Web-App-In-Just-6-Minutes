import streamlit as  st 
import pandas as pd 

st.title("BMI CALCULATOR")

height =st.slider("Enter Your height (in cm):", 100, 250, 175)
weight = st.slider("Enter your weight (in kg):", 40, 200, 70)

bmi = weight / ((height/100) **2)

st.write(f"Your BMI is {bmi:.2f}")

st.write("### BMI Categoris ###")
st.write("- Underweight: BMI less than 18.5")
st.write("-Normal weight: BMI between 18.5 and 24.9")
st.write("- Overnight: BMI between 25 and 29.9")
st.write("-Obesity: BMI 30 or greater")