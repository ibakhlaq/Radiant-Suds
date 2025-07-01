import streamlit as st
import json
import os

# Ensure users.json exists
if not os.path.exists('users.json'):
    with open('users.json', 'w') as f:
        json.dump([], f)

# Set Streamlit page settings
st.set_page_config(page_title="Sign Up", layout="wide", page_icon="", initial_sidebar_state="collapsed")
st.markdown("""
    <style>
        #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)
# Heading
st.markdown("<h1 style='text-align: center; color: #0bb; padding: 20px'> Sign Up</h1>", unsafe_allow_html=True)

# Signup form
with st.form("signup_form"):
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    submit_button = st.form_submit_button("Sign Up")

    if submit_button:
        if not username or not email or not password or not confirm_password:
            st.error("All fields are required.")
        elif password != confirm_password:
            st.error("Passwords do not match.")
        else:
            with open("users.json", "r") as f:
                try:
                    users = json.load(f)
                except json.JSONDecodeError:
                    users = []

            # Check if username or email already exists
            if any(user.get("username") == username for user in users):
                st.error("Username already exists.")
            elif any(user.get("email") == email for user in users):
                st.error("Email already registered.")
            else:
                users.append({
                    "username": username,
                    "email": email,
                    "password": password  # Password is stored as plain text for now
                })
                with open("users.json", "w") as f:
                    json.dump(users, f, indent=2)

                st.success("Sign up successful! You may now log in.")

# Redirect to login if button clicked
if st.button("Go to Login Page", key="login_button"):
    st.session_state.is_logged_in = False
    st.session_state.user = None
    st.switch_page("pages/Login.py")