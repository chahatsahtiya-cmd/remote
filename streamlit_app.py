import streamlit as st
import requests

# === CONFIG ===
CAR_API_URL = "http://192.168.4.1:5000"  # Change to your RC car's API endpoint

# === FUNCTION TO SEND COMMANDS ===
def send_command(command):
    try:
        response = requests.get(f"{CAR_API_URL}/{command}")
        if response.status_code == 200:
            st.success(f"Sent: {command}")
        else:
            st.error(f"Failed: {command} (status {response.status_code})")
    except Exception as e:
        st.error(f"Error: {e}")

# === PAGE SETUP ===
st.set_page_config(page_title="RC Car Remote", page_icon="🚗", layout="centered")

st.title("🚗 RC Car Remote Control")
st.write("Click buttons below to control your RC car.")

# === BUTTON CONTROLS ===
col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    if st.button("⬆️ Forward"):
        send_command("forward")

with col1:
    if st.button("⬅️ Left"):
        send_command("left")

with col3:
    if st.button("➡️ Right"):
        send_command("right")

with col2:
    if st.button("⬇️ Backward"):
        send_command("backward")

# Stop button (full width)
if st.button("⏹ Stop"):
    send_command("stop")

# Optional: Speed slider
speed = st.slider("Speed", min_value=0, max_value=100, value=50)
if st.button("Set Speed"):
    send_command(f"speed/{speed}")
