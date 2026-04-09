import streamlit as st
import joblib
import pandas as pd

# -------------------------------
# LOAD MODEL
# -------------------------------
model = joblib.load("Model.pkl")

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="AI Churn Predictor", layout="wide")

# -------------------------------
# PREMIUM CSS
# -------------------------------
st.markdown("""
<style>

/* === BASE === */
body, [data-testid="stAppViewContainer"] {
    background: #f8f9fb;
    color: #1a1a2e;
    font-family: 'Inter', 'Segoe UI', sans-serif;
}

[data-testid="stSidebar"] { display: none; }

/* === HIDE STREAMLIT DEFAULTS === */
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
header { visibility: hidden; }

/* === MAIN CONTAINER === */
.block-container {
    padding-top: 2rem !important;
    padding-bottom: 3rem !important;
    max-width: 1100px !important;
}

/* === TITLE BLOCK === */
.title {
    text-align: center;
    font-size: 36px;
    font-weight: 700;
    color: #0f172a;
    letter-spacing: -0.5px;
    margin-bottom: 4px;
}

.subtitle {
    text-align: center;
    font-size: 15px;
    color: #64748b;
    margin-bottom: 36px;
}

.badge-top {
    text-align: center;
    margin-bottom: 14px;
}

.badge-pill {
    display: inline-block;
    background: #e0f2fe;
    color: #0369a1;
    font-size: 12px;
    font-weight: 600;
    padding: 4px 14px;
    border-radius: 20px;
    letter-spacing: 0.04em;
}

/* === SECTION HEADER === */
.section-title {
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.09em;
    text-transform: uppercase;
    color: #64748b;
    margin-bottom: 16px;
    padding-bottom: 8px;
    border-bottom: 1px solid #e2e8f0;
    display: flex;
    align-items: center;
    gap: 8px;
}

/* === DIVIDER === */
.divider {
    border: none;
    border-top: 1px solid #e2e8f0;
    margin: 20px 0;
}

/* === RADIO BUTTONS === */
[data-testid="stRadio"] > label {
    font-size: 11px !important;
    font-weight: 600;
    color: #64748b !important;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 6px;
}

[data-testid="stRadio"] > div {
    flex-direction: row !important;
    gap: 8px;
    flex-wrap: wrap;
}

[data-testid="stRadio"] div[role="radio"] {
    background: #f1f5f9;
    border: 1px solid #e2e8f0;
    border-radius: 20px;
    padding: 5px 14px !important;
    font-size: 13px !important;
    color: #334155;
    cursor: pointer;
    transition: all 0.15s;
    margin: 0 !important;
}

[data-testid="stRadio"] div[role="radio"]:hover {
    background: #e0f2fe;
    border-color: #7dd3fc;
}

[data-testid="stRadio"] div[role="radio"][aria-checked="true"] {
    background: #0ea5e9 !important;
    color: white !important;
    border-color: #0ea5e9 !important;
    font-weight: 600;
}

[data-testid="stRadio"] div[role="radio"] > div {
    display: none;
}

/* === SLIDERS === */
[data-testid="stSlider"] > label {
    font-size: 11px !important;
    font-weight: 600;
    color: #64748b !important;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

[data-testid="stSlider"] [data-testid="stTickBar"] {
    display: none;
}

div[data-baseweb="slider"] div[data-testid="stSlider"] div {
    background: #0ea5e9 !important;
}

/* === SELECTBOX === */
[data-testid="stSelectbox"] > label {
    font-size: 11px !important;
    font-weight: 600;
    color: #64748b !important;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

[data-testid="stSelectbox"] > div > div {
    border-radius: 10px !important;
    border: 1px solid #e2e8f0 !important;
    background: #f8fafc !important;
    font-size: 13px;
    color: #334155;
}

/* === CHECKBOXES === */
[data-testid="stCheckbox"] > label {
    font-size: 13px !important;
    font-weight: 400;
    color: #334155 !important;
    text-transform: none !important;
    letter-spacing: 0 !important;
}

/* === INPUT LABELS GLOBALLY === */
.stTextInput label, label {
    font-size: 11px !important;
    font-weight: 600 !important;
    color: #64748b !important;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

/* === MAIN BUTTON === */
.stButton > button {
    width: 100%;
    background: #0f172a !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 12px !important;
    height: 54px !important;
    font-size: 15px !important;
    font-weight: 600 !important;
    letter-spacing: 0.02em !important;
    transition: all 0.2s !important;
    box-shadow: 0 2px 8px rgba(15,23,42,0.2) !important;
    margin-top: 8px;
}

.stButton > button:hover {
    background: #1e293b !important;
    box-shadow: 0 6px 20px rgba(15,23,42,0.3) !important;
    transform: translateY(-1px) !important;
}

.stButton > button:active {
    transform: scale(0.99) !important;
}

/* === ALERT BOXES === */
[data-testid="stSuccess"] {
    background: #f0fdf4 !important;
    border: 1px solid #bbf7d0 !important;
    border-radius: 10px !important;
    color: #15803d !important;
    font-size: 14px !important;
    font-weight: 500 !important;
}

[data-testid="stWarning"] {
    background: #fffbeb !important;
    border: 1px solid #fde68a !important;
    border-radius: 10px !important;
    color: #92400e !important;
    font-size: 14px !important;
    font-weight: 500 !important;
}

[data-testid="stError"] {
    background: #fef2f2 !important;
    border: 1px solid #fecaca !important;
    border-radius: 10px !important;
    color: #991b1b !important;
    font-size: 14px !important;
    font-weight: 500 !important;
}

/* === PROGRESS BAR === */
[data-testid="stProgress"] > div > div > div > div {
    background: linear-gradient(90deg, #0ea5e9, #6366f1) !important;
    border-radius: 4px !important;
}

[data-testid="stProgress"] > div > div {
    background: #e2e8f0 !important;
    border-radius: 4px !important;
    height: 10px !important;
}

/* === RESULT BOX === */
.result-box {
    padding: 28px 32px;
    border-radius: 16px;
    text-align: center;
    font-size: 22px;
    font-weight: 700;
    letter-spacing: -0.3px;
    margin-bottom: 12px;
}

.result-stay {
    background: #f0fdf4;
    color: #15803d;
    border: 1.5px solid #86efac;
}

.result-churn {
    background: #fef2f2;
    color: #991b1b;
    border: 1.5px solid #fca5a5;
}

/* === STAT MINI CARDS === */
.stat-row {
    display: flex;
    gap: 12px;
    margin-top: 12px;
}

.stat-mini {
    flex: 1;
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 12px 14px;
    text-align: center;
}

.stat-mini-label {
    font-size: 11px;
    color: #64748b;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 4px;
}

.stat-mini-val {
    font-size: 18px;
    font-weight: 700;
    color: #0f172a;
}

/* === COLUMNS CARD WRAPPER === */
div[data-testid="columns"] > div > div[data-testid="column"] {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 16px;
    padding: 20px 16px !important;
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# TITLE
# -------------------------------
st.markdown('<div class="badge-top"><span class="badge-pill">Churn Intelligence</span></div>', unsafe_allow_html=True)
st.markdown('<div class="title">AI Customer Churn Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Enter customer details below to predict churn probability</div>', unsafe_allow_html=True)

# -------------------------------
# COLUMNS
# -------------------------------
col1, col2, col3 = st.columns(3, gap="medium")

# -------------------------------
# CUSTOMER PROFILE
# -------------------------------
with col1:
    st.markdown('<div class="section-title">👤 &nbsp;Customer Profile</div>', unsafe_allow_html=True)

    gender   = st.radio("Gender", ["Male", "Female"], horizontal=True)
    senior   = st.radio("Age Group", ["Below 60", "Above 60"], horizontal=True)
    partner  = st.radio("Has Partner?", ["No", "Yes"], horizontal=True)
    dependents = st.radio("Has Dependents?", ["No", "Yes"], horizontal=True)
    tenure   = st.slider("Tenure with Company (months)", 0, 72, 12)

# -------------------------------
# SERVICES
# -------------------------------
with col2:
    st.markdown('<div class="section-title">📡 &nbsp;Services Used</div>', unsafe_allow_html=True)

    phone    = st.radio("Phone Service?", ["Yes", "No"], horizontal=True)
    multi    = st.radio("Multiple Lines?", ["No", "Yes"], horizontal=True)
    internet = st.selectbox("Internet Type", ["DSL", "Fiber Optic", "No Internet"])

    st.markdown("**Add-ons**")
    security = st.checkbox("Online Security")
    backup   = st.checkbox("Online Backup")
    device   = st.checkbox("Device Protection")
    support  = st.checkbox("Tech Support")
    tv       = st.checkbox("Streaming TV")
    movies   = st.checkbox("Streaming Movies")

# -------------------------------
# CONTRACT & BILLING
# -------------------------------
with col3:
    st.markdown('<div class="section-title">💰 &nbsp;Contract & Billing</div>', unsafe_allow_html=True)

    contract = st.selectbox("Contract Type", ["Month-to-Month", "1 Year", "2 Years"])
    paper    = st.radio("Paperless Billing?", ["Yes", "No"], horizontal=True)
    payment  = st.selectbox("Payment Method", ["Online Banking", "Credit / Debit Card", "Bank Transfer", "Cash"])

    monthly  = st.slider("Monthly Bill Amount (₹)", 0, 10000, 1000, step=50)
    total    = monthly * tenure

    st.markdown(f"""
    <div class="stat-row">
        <div class="stat-mini">
            <div class="stat-mini-label">Monthly</div>
            <div class="stat-mini-val">₹{monthly:,}</div>
        </div>
        <div class="stat-mini">
            <div class="stat-mini-label">Total Paid</div>
            <div class="stat-mini-val">₹{total:,}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# -------------------------------
# PREPROCESS
# -------------------------------
def preprocess():
    internet_map = {"DSL": 0, "Fiber Optic": 1, "No Internet": 2}
    contract_map = {"Month-to-Month": 0, "1 Year": 1, "2 Years": 2}
    payment_map  = {"Online Banking": 0, "Credit / Debit Card": 1, "Bank Transfer": 2, "Cash": 3}

    return pd.DataFrame([{
        "gender":           1 if gender == "Male" else 0,
        "SeniorCitizen":    1 if senior == "Above 60" else 0,
        "Partner":          1 if partner == "Yes" else 0,
        "Dependents":       1 if dependents == "Yes" else 0,
        "tenure":           tenure,
        "PhoneService":     1 if phone == "Yes" else 0,
        "MultipleLines":    1 if multi == "Yes" else 0,
        "InternetService":  internet_map[internet],
        "OnlineSecurity":   1 if security else 0,
        "OnlineBackup":     1 if backup else 0,
        "DeviceProtection": 1 if device else 0,
        "TechSupport":      1 if support else 0,
        "StreamingTV":      1 if tv else 0,
        "StreamingMovies":  1 if movies else 0,
        "Contract":         contract_map[contract],
        "PaperlessBilling": 1 if paper == "Yes" else 0,
        "PaymentMethod":    payment_map[payment],
        "MonthlyCharges":   monthly,
        "TotalCharges":     total,
    }])

# -------------------------------
# PREDICT BUTTON
# -------------------------------
btn_col = st.columns([1, 2, 1])[1]
with btn_col:
    clicked = st.button("🚀  Analyze Churn Risk")

if clicked:
    df   = preprocess()
    pred = model.predict(df)[0]

    if hasattr(model, "predict_proba"):
        prob = model.predict_proba(df)[0][1]
    else:
        prob = 0.5

    percentage = round(prob * 100, 1)

    st.markdown("<hr class='divider'>", unsafe_allow_html=True)

    r1, r2, r3 = st.columns([1, 2, 1])
    with r2:
        if pred == 1:
            st.markdown(
                f'<div class="result-box result-churn">⚠️ High Churn Risk &nbsp;·&nbsp; {percentage}%</div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f'<div class="result-box result-stay">✅ Customer Will Stay &nbsp;·&nbsp; {100 - percentage:.1f}% confidence</div>',
                unsafe_allow_html=True
            )

        st.markdown(f"**Churn probability:** {percentage}%")
        st.progress(prob)

        if percentage < 30:
            st.success("🟢  Low Risk — This customer is very likely to stay.")
        elif percentage < 70:
            st.warning("🟡  Medium Risk — Monitor this customer closely.")
        else:
            st.error("🔴  High Risk — Immediate retention action recommended.")
