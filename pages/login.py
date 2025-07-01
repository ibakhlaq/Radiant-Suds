import streamlit as st
import json
import os

# Ensure necessary JSON files exist before anything else
if not os.path.exists('users.json'):
    with open('users.json', 'w') as f:
        json.dump({}, f)
if not os.path.exists('reviews.json'):
    with open('reviews.json', 'w') as f:
        json.dump([], f)
if not os.path.exists('cart.json'):
    with open('cart.json', 'w') as f:
        json.dump({}, f)

# Page config
st.set_page_config(page_title="Login", layout="wide", page_icon="", initial_sidebar_state="collapsed")
st.markdown("<h1 style='text-align: center; color: #0bb; padding: 20px'> Login</h1>", unsafe_allow_html=True)

# Button Styling
st.markdown("""
    <style>
        #MainMenu, footer, header {visibility: hidden;}
        .stButton > button {
            background-color: #8BC34A;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
            transition: background-color 0.3s ease-in-out, color 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
            text-transform: uppercase;
            border: none;
            cursor: pointer;
        }
        .stButton > button:hover {
            background-color: #C7B8EA;
            color: #fff;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        }
        .stButton > button:active {
            transform: scale(0.98);
        }
    </style>
""", unsafe_allow_html=True)

# If already logged in, redirect to home or wherever
if st.session_state.get("is_logged_in"):
    st.success(f"Welcome back, {st.session_state.user}!")
    st.stop()

# Login form
with st.form("login_form"):
    username = st.text_input("Username", key="username")
    password = st.text_input("Password", type="password", key="password")
    submit_button = st.form_submit_button("Login")

    if submit_button:
        with open("users.json", "r") as f:
            users = json.load(f)

        if username in users and users[username] == password:
            st.session_state.user = username
            st.session_state.is_logged_in = True
            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Invalid username or password.")

# Register link
st.markdown("""
    <p style='text-align: center; color: #064b4f'>
        Don't have an account? 
        <a href='radiantsuds.streamlit.app/signup'>Register here</a>
    </p>
""", unsafe_allow_html=True)