import streamlit as st

def home_page():
    st.title("Welcome to the Education Access App")
    st.write("""
        This app aims to improve access to education in Somalia through predictive modeling and analytics.
        
        **Features:**
        - Analyze student data to predict potential dropouts.
        - Generate actionable insights for policymakers.
        - Retrain models with new data for better accuracy.

        Use the sidebar to navigate through the app.
    """)
    st.image("https://via.placeholder.com/800x400", caption="Education for All", use_column_width=True)
