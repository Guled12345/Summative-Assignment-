import streamlit as st

def prediction_page():
    st.title("Education Access Prediction")
    st.write("This page allows you to predict the likelihood of students needing assistance based on input data.")
    
    # Placeholder for user inputs
    st.subheader("Enter Student Data:")
    age = st.number_input("Age:", min_value=5, max_value=25, step=1)
    gender = st.selectbox("Gender:", ["Male", "Female", "Other"])
    socioeconomic_status = st.selectbox("Socioeconomic Status:", ["Low", "Medium", "High"])
    attendance_rate = st.slider("Attendance Rate (%):", min_value=0, max_value=100, step=5)

    if st.button("Predict"):
        # Dummy prediction logic
        st.success("Prediction: The student is at low risk of dropping out.")
        st.info("This is a placeholder result. Integrate with a trained model for real predictions.")
