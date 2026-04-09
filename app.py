import streamlit as st
import joblib
import pandas as pd

# -------------------------------
# LOAD MODEL (PIPELINE SAFE)
# -------------------------------
try:
    model = joblib.load("model.pkl")
except:
    st.error("❌ Model not found or incompatible. Please upload correct model.pkl")
    st.stop()

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="AI Churn Predictor", layout="wide")

# -------------------------------
# PREMIUM INLINE CSS 🔥
# -------------------------------
st.markdown("""
<style>

body {
    background: linear-gradient(135deg, #0f172a, #1e293b);
}

/* Title */
.title {
    text-align: center;
    font-size: 48px;
    font-weight: bold;
    background: linear-gradient(90deg, #38bdf8, #6366f1);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 20px;
}

/* Card */
.card {
    background: rgba(255,255,255,0.05);
    padding: 30px;
    border-radius: 20px;
    backdrop-filter: blur(20px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    margin-bottom: 20px;
}

/* Section title */
.section {
    font-size: 20px;
    color: #38bdf8;
    margin-bottom: 10px;
}

/* Result */
.result {
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    font-size: 24px;
    font-weight: bold;
}

/* Button */
.stButton>button {
    width: 100%;
    height: 55px;
    border-radius: 12px;
    background: linear-gradient(90deg, #6366f1, #8b5cf6);
    color: white;
    font-size: 18px;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# TITLE
# -------------------------------
st.markdown('<div class="title">🚀 AI Customer Churn Predictor</div>', unsafe_allow_html=True)

# -------------------------------
# INPUT CARD
# -------------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

# -------------------------------
# USER FRIENDLY INPUTS
# -------------------------------
with col1:
    st.markdown('<div class="section">👤 Customer Info</div>', unsafe_allow_html=True)
    gender = st.radio("Gender", ["Male", "Female"])
    senior = st.radio("Age Group", ["Below 60", "Above 60"])
    partner = st.radio("Has Partner?", ["No", "Yes"])
    dependents = st.radio("Has Family?", ["No", "Yes"])
    tenure = st.slider("Months with company", 0, 72)

with col2:
    st.markdown('<div class="section">📡 Services</div>', unsafe_allow_html=True)
    phone = st.radio("Phone Service?", ["Yes", "No"])
    multi = st.radio("Multiple Lines?", ["No", "Yes"])
    internet = st.selectbox("Internet Type", ["DSL", "Fiber optic", "No"])
    security = st.checkbox("Online Security")
    backup = st.checkbox("Online Backup")

with col3:
    st.markdown('<div class="section">⚙️ Features</div>', unsafe_allow_html=True)
    device = st.checkbox("Device Protection")
    support = st.checkbox("Tech Support")
    tv = st.checkbox("Streaming TV")
    movies = st.checkbox("Streaming Movies")
    contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])

st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# BILLING CARD
# -------------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown('<div class="section">💰 Billing (Simple)</div>', unsafe_allow_html=True)

monthly = st.slider("💵 Monthly bill (₹)", 0, 10000, 1000)

# AUTO CALCULATE
total = monthly * tenure
st.info(f"📊 Total paid so far: ₹ {total}")

paper = st.radio("Paperless Billing?", ["Yes", "No"])
payment = st.selectbox("Payment Method", [
    "Electronic check",
    "Mailed check",
    "Bank transfer (automatic)",
    "Credit card (automatic)"
])

st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------
# CREATE INPUT (NO MANUAL ENCODING 🔥)
# -------------------------------
input_df = pd.DataFrame([{
    "gender": gender,
    "SeniorCitizen": 1 if senior=="Above 60" else 0,
    "Partner": partner,
    "Dependents": dependents,
    "tenure": tenure,
    "PhoneService": phone,
    "MultipleLines": multi,
    "InternetService": internet,
    "OnlineSecurity": "Yes" if security else "No",
    "OnlineBackup": "Yes" if backup else "No",
    "DeviceProtection": "Yes" if device else "No",
    "TechSupport": "Yes" if support else "No",
    "StreamingTV": "Yes" if tv else "No",
    "StreamingMovies": "Yes" if movies else "No",
    "Contract": contract,
    "PaperlessBilling": paper,
    "PaymentMethod": payment,
    "MonthlyCharges": monthly,
    "TotalCharges": total
}])

# -------------------------------
# PREDICTION
# -------------------------------
if st.button("🚀 Analyze Customer"):

    pred = model.predict(input_df)[0]

    if hasattr(model, "predict_proba"):
        prob = model.predict_proba(input_df)[0][1]
    else:
        prob = 0.5

    percentage = round(prob * 100, 2)

    st.markdown('<div class="card">', unsafe_allow_html=True)

    if pred == 1:
        st.markdown(
            f'<div class="result" style="background:#7f1d1d;">⚠️ High Churn Risk ({percentage}%)</div>',
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f'<div class="result" style="background:#14532d;">✅ Customer Will Stay ({100 - percentage}%)</div>',
            unsafe_allow_html=True
        )

    st.progress(prob)

    st.markdown('</div>', unsafe_allow_html=True)
