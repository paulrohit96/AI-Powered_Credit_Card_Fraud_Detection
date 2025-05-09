# -*- coding: utf-8 -*-
"""Untitled95.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CANwryCloOLCjMi_8kvbZ9p9z2NoJbWn
"""

import streamlit as st
import pandas as pd
from PIL import Image
import openai
import time  # Needed for the chatbot simulation

# Set page configuration
st.set_page_config(page_title="XYA Bank Fraud Case Manager", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        .main {
            padding: 2rem;
        }
        .section {
            padding: 1.5rem;
            margin-bottom: 2rem;
            border-radius: 10px;
            background-color: #f9f9f9;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .title {
            text-align: center;
            color: #2c3e50;
            margin-bottom: 2rem;
        }
        .case-details {
            padding: 1.5rem;
            background-color: #e8f4fc;
            border-radius: 10px;
            margin-top: 1rem;
        }
        .detail-row {
            display: flex;
            margin-bottom: 0.5rem;
        }
        .detail-label {
            font-weight: bold;
            width: 200px;
        }
        .stDataFrame {
            border-radius: 10px;
        }
        .action-buttons {
            display: flex;
            gap: 1rem;
            margin-top: 2rem;
        }
        .chat-container {
            padding: 1.5rem;
            background-color: #f0f2f6;
            border-radius: 10px;
            margin-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 class='title'>XYA Bank Financial Crime Department</h1>", unsafe_allow_html=True)

# Load sample data (replace with your actual data loading logic)
@st.cache_data
def load_data():
    return pd.DataFrame({
        "Customer_ID": ["CUST001", "CUST002", "CUST003"],
        "Transaction_Date": ["2023-01-01", "2023-01-02", "2023-01-03"],
        "Transaction_Amount": [150.00, 1200.00, 75.50],
        "Merchant_Name": ["Amazon", "Best Buy", "Walmart"],
        "Merchant_Category": ["Online Retail", "Electronics", "Supermarket"],
        "Fraud_Flag": [0, 1, 0],
        "Transaction_Hour": [14, 3, 10],
        "Transaction_Day": ["Monday", "Tuesday", "Wednesday"],
        "Transaction_Month": ["January", "January", "January"],
        "Transaction_Frequency": [5, 1, 12],
        "Location_Mismatch": [0, 1, 0],
        "Fraud_Prediction": [0, 1, 0],
        "Real_World_Reason": ["Normal purchase", "Unusual time for large purchase", "Regular grocery shopping"],
        "Model_Reason": ["Low risk pattern", "High risk pattern detected", "Low risk pattern"]
    })

df = load_data()

# Main sections
with st.container():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.write("## Fraud Cases Overview")
    st.dataframe(df.style.applymap(lambda x: 'background-color: #ffcccc' if x == 1 else '',
                                subset=['Fraud_Flag', 'Fraud_Prediction']),
              use_container_width=True)
    st.markdown("</div>", unsafe_allow_html=True)

# Case selection
with st.container():
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.write("## Case Investigation")

    case_id = st.selectbox("Select a Case ID to Investigate", df["Customer_ID"].unique())

    selected_case = df[df["Customer_ID"] == case_id].iloc[0]

    st.markdown("<div class='case-details'>", unsafe_allow_html=True)
    st.write("### Case Details")

    def display_detail(label, value):
        st.markdown(f"""
        <div class="detail-row">
            <div class="detail-label">{label}:</div>
            <div>{value}</div>
        </div>
        """, unsafe_allow_html=True)

    display_detail("Customer ID", selected_case['Customer_ID'])
    display_detail("Transaction Date", selected_case['Transaction_Date'])
    display_detail("Transaction Amount", f"${selected_case['Transaction_Amount']:,.2f}")
    display_detail("Merchant Name", selected_case['Merchant_Name'])
    display_detail("Merchant Category", selected_case['Merchant_Category'])
    display_detail("Fraud Flag", '✅ Fraudulent' if selected_case['Fraud_Flag'] == 1 else '✅ Non-Fraudulent')
    display_detail("Transaction Time", f"{selected_case['Transaction_Hour']}:00 on {selected_case['Transaction_Day']}")
    display_detail("Transaction Month", selected_case['Transaction_Month'])
    display_detail("Transaction Frequency", selected_case['Transaction_Frequency'])
    display_detail("Location Mismatch", '⚠️ Yes' if selected_case['Location_Mismatch'] else '✅ No')
    display_detail("Fraud Prediction", '🔴 Fraudulent' if selected_case['Fraud_Prediction'] == 1 else '🟢 Non-Fraudulent')
    display_detail("Real World Reason", selected_case['Real_World_Reason'])
    display_detail("Model Reason", selected_case['Model_Reason'])

    st.markdown("</div>", unsafe_allow_html=True)

    st.write("### Case Resolution")
    resolution_status = st.selectbox(
        "Select resolution status:",
        ["Select an option", "False Positive", "Confirmed Fraud", "Under Investigation", "Requires Escalation"],
        index=0
    )

    resolution_notes = st.text_area("Add notes about this case:")

    st.markdown("<div class='action-buttons'>", unsafe_allow_html=True)
    save_btn = st.button("💾 Save Case")
    cancel_btn = st.button("❌ Cancel")
    done_btn = st.button("✅ Done")
    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)