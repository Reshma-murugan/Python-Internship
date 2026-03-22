import streamlit as st

st.title("Student Grade Predictor")

tamil = st.number_input("Tamil Marks")
english = st.number_input("English Marks")
maths = st.number_input("Maths Marks")
science = st.number_input("Science Marks")
social = st.number_input("Social Marks")

if st.button("Calculate Grade"):
    avg = (tamil + english + maths + science + social) / 5
    
    if avg >= 90:
        grade = "A+"
    elif avg >= 80:
        grade = "A"
    elif avg >= 70:
        grade = "B+"
    elif avg >= 60:
        grade = "B"
    elif avg >= 50:
        grade = "C"
    elif avg >= 40:
        grade = "D"
    else:
        grade = "F"

    st.success(f"Average: {avg}")
    st.success(f"Grade: {grade}")