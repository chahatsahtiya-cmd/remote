import streamlit as st
import requests

st.title("🚗 RC Car Remote")

# Replace with your RC car's control API or IP address
BASE_URL = "http://192.168.4.1"  # Example: ESP8266/ESP32 server

# Buttons for control
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("⬆ Forward"):
        requests.get(f"{BASE_URL}/forward")

with col2:
    if st.button("⬅ Left"):
        requests.get(f"{BASE_URL}/left")

    if st.button("Stop 🛑"):
        requests.get(f"{BASE_URL}/stop")

    if st.button("➡ Right"):
        requests.get(f"{BASE_URL}/right")

with col3:
    if st.button("⬇ Backward"):
        requests.get(f"{BASE_URL}/backward")
