import streamlit as st
import json
import os
#login page
st.set_page_config(page_title="Login", layout="wide", page_icon="", initial_sidebar_state="collapsed")
st.markdown("<h1 style='text-align: center; color: #0bb; padding: 20px'> Login</h1>", unsafe_allow_html=True)
st.markdown("""
    <style>
        .stButton > button {
            background-color: #8BC34A;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
            transition: background-color 0.3s ease-in-out;
            transition: color 0.3s ease-in-out;
            transition: box-shadow 0.3s ease-in-out;
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
            background-color: #C7B8EA;
            color: #fff;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
            transform: scale(0.98);
            transition: transform 0.2s ease-in-out;
        }
        .stButton > button:focus {
            outline: none;
            box-shadow: 0 0 0 3px rgba(0, 123, 255, 0.5);
        }
        .stButton > button:disabled {
            background-color: #ccc;
            color: #888;
            cursor: not-allowed;
            box-shadow: none;
        }
        .stButton > button:disabled:hover {
            background-color: #ccc;
            color: #888;
            cursor: not-allowed;
            box-shadow: none;
        }
        .stButton > button:disabled:active {
            background-color: #ccc;
            color: #888;
            cursor: not-allowed;
            box-shadow: none;
            transform: none;
        }
        .stButton > button:disabled:focus {
            outline: none;
            box-shadow: none;
        }
    </style>
""", unsafe_allow_html=True)
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
                st.experimental_rerun()
            else:
                st.error("Invalid username or password.")
# Register link
st.markdown("<p style='text-align: center; color: #064b4f'>Don't have an account? <a href='/register'>Register here</a></p>", unsafe_allow_html=True)
# Redirect to home if already logged in
if "user" in st.session_state:
    st.session_state.is_logged_in = True
    st.success(f"Welcome back, {st.session_state.user}!")
    st.experimental_rerun()
# Redirect to signup if button clicked
if st.button("Sign Up", key="signup_button"):
    st.session_state.is_logged_in = False
    st.session_state.user = None
    st.switch_page("pages/Signup.py")
# Ensure users.json exists
if not os.path.exists('users.json'):
    with open('users.json', 'w') as f:
        json.dump({}, f)
# Ensure reviews.json exists
if not os.path.exists('reviews.json'):
    with open('reviews.json', 'w') as f:
        json.dump([], f)
# Ensure cart.json exists
if not os.path.exists('cart.json'):
    with open('cart.json', 'w') as f:
        json.dump({}, f)
        