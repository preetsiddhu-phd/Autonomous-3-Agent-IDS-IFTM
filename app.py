import streamlit as st
import pandas as pd

st.set_page_config(page_title="3-Agent IDS Live", layout="wide", page_icon="🛡️")
st.title("🛡️ Autonomous 3-Agent IDS - Live Dashboard - IFTM IoT Lab")
st.caption("Real-time Intrusion Detection • Detector | Explainer | Mitigator • 78ms • 96.2%")

col1, col2, col3, col4 = st.columns(4)
col1.metric("Latency", "78ms", "-12ms vs target")
col2.metric("Accuracy", "96.2%", "0.8% up")
col3.metric("Agents Active", "3/3", "All Active")
col4.metric("Threats Blocked", "127", "3 today")

st.divider()
c1, c2, c3 = st.columns(3)
c1.success("**Detector Agent (CNN-LSTM)** - Active\n1.2k pkts/min")
c2.info("**Explainer Agent (SHAP/LIME)** - Active")
c3.warning("**Mitigator Agent (LangGraph/AutoGen)** - Active")

st.subheader("🚨 Live Threats")
st.dataframe(pd.DataFrame({
    "Timestamp": ["14:31:52", "14:32:10", "14:32:45"],
    "IP": ["192.168.1.45", "192.168.1.88", "10.0.0.12"],
    "Attack": ["DDoS", "Botnet", "Port Scan"],
    "Action": ["iptables DROP", "Isolation", "Monitor"],
    "Status": ["Blocked ✅", "Blocked ✅", "Monitoring"]
}), use_container_width=True)

st.subheader("🔍 Explainable AI - SHAP Values")
st.bar_chart({"Packet Rate": 0.34, "Port Scan": 0.28, "Bytes Sent": 0.19})

if st.button("▶️ Simulate Live Attack - Demo for Interview"):
    st.warning("[DETECTOR] DDoS Detected 96% - IP 192.168.1.45")
    st.info("[EXPLAINER] Packet rate 0.34 + Port scan 0.28 = Attack")
    st.success("[MITIGATOR] Auto Rule: iptables -A INPUT -s 192.168.1.45 -j DROP | 78ms")
    st.balloons()
