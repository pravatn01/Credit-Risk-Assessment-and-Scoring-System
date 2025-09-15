import streamlit as st
from prediction_helper import predict

# --- Page Config ---
st.set_page_config(
    page_title="Credit Risk Assessment and Scoring System",
    page_icon="📊",
    layout="wide"
)

# --- Custom Styling ---
st.markdown("""
    <style>
        /* Center titles and add spacing */
        .stTitle { text-align: center; padding-bottom: 1rem; }
        /* Expander headers styling */
        .streamlit-expanderHeader {
            font-weight: 600 !important;
            font-size: 1.1rem !important;
        }
        /* Metric cards */
        div[data-testid="stMetricValue"] {
            font-size: 1.5rem;
            font-weight: 700;
        }
        div[data-testid="stMetricLabel"] {
            font-size: 0.9rem;
            font-weight: 500;
        }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.title("📊 Credit Risk Assessment and Scoring System")
st.markdown(
    "A modern tool to estimate **default probability**, **credit score**, "
    "and **risk rating** for borrowers."
)
st.divider()

# --- Borrower Information ---
with st.expander("👤 Borrower Information", expanded=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.number_input("Age", min_value=18, max_value=100, step=1, value=28)
    with col2:
        income = st.number_input("Annual Income (₹)", min_value=0, value=1200000)
    with col3:
        residence_type = st.selectbox("Residence Type", ["Owned", "Rented", "Mortgage"])

# --- Loan Details ---
with st.expander("💰 Loan Details", expanded=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        loan_amount = st.number_input("Loan Amount (₹)", min_value=0, value=2560000)
    with col2:
        loan_tenure_months = st.number_input("Loan Tenure (months)", min_value=0, step=1, value=36)
    with col3:
        loan_type = st.selectbox("Loan Type", ["Unsecured", "Secured"])

    col4, col5 = st.columns(2)
    with col4:
        loan_purpose = st.selectbox("Loan Purpose", ["Education", "Home", "Auto", "Personal"])
    with col5:
        loan_to_income_ratio = loan_amount / income if income > 0 else 0
        st.progress(min(1.0, loan_to_income_ratio / 5))  # bar visualization
        st.caption(f"Loan-to-Income Ratio: **{loan_to_income_ratio:.2f}**")

# --- Credit Behavior ---
with st.expander("📈 Credit Behavior", expanded=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        avg_dpd_per_delinquency = st.number_input("Avg DPD", min_value=0, value=20)
    with col2:
        delinquency_ratio = st.number_input("Delinquency Ratio (%)", min_value=0, max_value=100, step=1, value=30)
    with col3:
        credit_utilization_ratio = st.number_input("Credit Utilization Ratio (%)", min_value=0, max_value=100, step=1, value=30)

    col4, _ = st.columns([1, 2])
    with col4:
        num_open_accounts = st.number_input("Open Loan Accounts", min_value=1, max_value=10, step=1, value=2)

st.divider()

# --- Prediction Button ---
if st.button("🚀 Calculate Risk", use_container_width=True, type="primary"):
    probability, credit_score, rating = predict(
        age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
        delinquency_ratio, credit_utilization_ratio, num_open_accounts,
        residence_type, loan_purpose, loan_type
    )

    st.subheader("🔎 Results")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Default Probability", f"{probability:.2%}")
        st.progress(int(probability * 100))
    with col2:
        st.metric("Credit Score", f"{credit_score}")
    with col3:
        st.metric("Risk Rating", rating)

    # Helpful interpretation
    st.info(
        f"📌 Based on your inputs, the model predicts a **{probability:.2%}** "
        f"chance of default. The borrower is rated as **{rating}** with a credit score of **{credit_score}**."
    )
