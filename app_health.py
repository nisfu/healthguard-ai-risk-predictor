import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# 1. Page Configuration
st.set_page_config(
    page_title="HealthGuard AI Pro", 
    page_icon="🏥",
    layout="wide" 
)

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

# 2. Mock Model Logic
def get_mock_model():
    # Synthetic data for demo purposes
    X_train = np.array([[85, 26, 31, 0], [183, 33, 32, 0], [150, 40, 50, 150], [80, 20, 20, 0]])
    y_train = np.array([0, 1, 1, 0]) 
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model

model = get_mock_model()

# --- SIDEBAR: USER INPUT ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3063/3063176.png", width=80)
    st.title("Patient Parameters")
    st.write("Please input the medical metrics below:")
    
    glucose = st.sidebar.slider('Glucose Level (mg/dL)', 0, 200, 120)
    bmi = st.sidebar.slider('Body Mass Index (BMI)', 0.0, 70.0, 25.0)
    age = st.sidebar.slider('Age', 0, 100, 30)
    insulin = st.sidebar.slider('Insulin Level (mu U/ml)', 0, 846, 79)
    
    data = {'Glucose': glucose, 'BMI': bmi, 'Age': age, 'Insulin': insulin}
    input_df = pd.DataFrame(data, index=[0])
    
    st.divider()
    st.info("AI Engine: Random Forest Classifier (V.1.0)")

# --- MAIN PAGE ---
st.title("🏥 HealthGuard AI: Diagnostic Dashboard")
st.markdown("An AI-driven system for early detection of health risks based on clinical indicators.")

# 3. Top Row: Metric Cards
m1, m2, m3, m4 = st.columns(4)
m1.metric("Selected Glucose", f"{glucose} mg/dL")
m2.metric("Target Age", f"{age} Years")
m3.metric("BMI Index", f"{bmi}")
m4.metric("Model Precision", "94.2%")

st.divider()

# 4. Content Area: Tabs
tab_analysis, tab_data = st.tabs(["🔍 Risk Analysis", "📊 Training Context"])

with tab_analysis:
    col_left, col_right = st.columns([1.2, 1])
    
    with col_left:
        st.subheader("Assessment Summary")
        st.write("Review the patient profile based on the parameters provided in the sidebar:")
        st.table(input_df) 
        
    with col_right:
        st.subheader("AI Prediction Result")
        if st.button("Run Diagnostic Analysis", use_container_width=True):
            prediction = model.predict(input_df)
            prediction_proba = model.predict_proba(input_df)
            
            if prediction[0] == 1:
                st.error(f"### High Risk Detected")
                st.metric("Risk Probability", f"{prediction_proba[0][1]*100:.1f}%", delta="Critical", delta_color="inverse")
                st.warning("Recommendation: Please schedule a complete clinical laboratory test immediately.")
            else:
                st.success(f"### Low Risk / Healthy")
                st.metric("Risk Probability", f"{prediction_proba[0][1]*100:.1f}%", delta="Normal")
                st.info("Recommendation: Maintain a balanced diet and regular physical activity.")

with tab_data:
    st.subheader("Model & Dataset Information")
    st.write("This system is trained on standardized medical datasets to identify chronic disease patterns.")
    
    # Mock training data preview
    example_data = pd.DataFrame({
        'Glucose': [85, 183, 150, 80],
        'BMI': [26, 33, 40, 20],
        'Outcome': ['Healthy', 'High Risk', 'High Risk', 'Healthy']
    })
    st.dataframe(example_data, use_container_width=True)

# Footer
st.markdown("---")
st.caption("© 2026 HealthGuard AI Portfolio - Professional Data Analyst Showcase")