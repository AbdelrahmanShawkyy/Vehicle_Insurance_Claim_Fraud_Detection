import streamlit as st
import requests
import streamlit as st
import requests

st.set_page_config(page_title="Insurance Fraud Pro", layout="wide")

def add_custom_css():
    st.markdown(
        """
        <style>
        .stApp {
            background-image: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), 
            url("https://images.unsplash.com/photo-1459603677915-a62079ffd002?q=80&w=2000&auto=format&fit=crop");
            background-attachment: fixed;
            background-size: cover;
        }
        
        /* جعل الحاويات شفافة بشكل عصري */
        div[data-testid="stVerticalBlock"] > div:has(div.stNumberInput) {
            background-color: rgba(255, 255, 255, 0.05);
            padding: 20px;
            border-radius: 15px;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255,255,255,0.1);
        }

        h1, h2, h3, p, label {
            color: white !important;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

add_custom_css()


st.set_page_config(page_title="Insurance Fraud Pro", layout="wide")

st.title("🛡️ Advanced Fraud Detection System")
st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.header("👤 Customer Info")
    age = st.number_input("Age", 18, 100, 35)
    months_as_customer = st.number_input("Months as Customer", 0, 500, 120)
    policy_csl = st.selectbox("Policy CSL", ["100/300", "250/500", "500/1000"])

with col2:
    st.header("🚗 Incident Details")
    incident_severity = st.selectbox("Severity", ["Minor Damage", "Total Loss", "Major Damage"])
    severity_map = {"Minor Damage": 1, "Total Loss": 2, "Major Damage": 3}
    incident_type = st.selectbox("Incident Type", ["Single Vehicle Collision", "Multi-vehicle Collision", "Parked Car"])
    number_of_vehicles_involved = st.number_input("Vehicles Involved", 1, 10, 1)

with col3:
    st.header("💰 Claim Amounts")
    total_claim_amount = st.number_input("Total Claim ($)", 0, 1000000000, 75000)
    injury_claim = st.number_input("Injury Claim ($)", 0, 1000000000, 300000)
    property_claim = st.number_input("Property Claim ($)", 0, 1000000000, 200000)

st.markdown("---")

if st.button("🚀 Run Fraud Analysis"):
    payload = {
        "features": {
            "age": age,
            "months_as_customer": months_as_customer,
            "incident_severity": severity_map[incident_severity],
            "total_claim_amount": total_claim_amount,
            "injury_claim": injury_claim,
            "property_claim": property_claim,
            "number_of_vehicles_involved": number_of_vehicles_involved
        }
    }
    
    try:
        response = requests.post("http://127.0.0.1:8000/predict", json=payload)
        result = response.json()
        
        st.subheader("Analysis Results:")
        
        if result['is_fraud'] == 1:
            st.error(f"⚠️ RESULT: {result['result']}")
        else:
            st.success(f"✅ RESULT: {result['result']}")
                    
    except Exception as e:
        st.error("Connection Error: Is FastAPI running?")