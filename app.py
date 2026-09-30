import streamlit as st
from detector.dns_analyzer import analyze_domain

st.set_page_config(
    page_title="CyberGuard AI",
    page_icon="🛡️",
    layout="wide"
)

st.title(" CyberGuard AI")
st.subheader("DNS Security & Tunneling Risk Analyzer")

st.write(
    "Enter a DNS domain below and CyberGuard will analyze "
    "its characteristics and estimate its security risk."
)

domain = st.text_input(
    "Enter DNS Domain",
    placeholder="example.com"
)

if st.button(" Scan Domain"):

    if domain.strip():

        result = analyze_domain(domain.strip())

        score = result["risk_score"]
        level = result["risk_level"]

        st.divider()

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Risk Score", f"{score} / 100")

        with col2:
            st.metric("Risk Level", level)

        st.subheader(" Analysis")

        if result["reasons"]:
            for reason in result["reasons"]:
                st.write("", reason)
        else:
            st.success("No major suspicious indicators found.")

    else:
        st.warning("Please enter a domain first.")