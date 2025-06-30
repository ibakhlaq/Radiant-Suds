import streamlit as st
import json
import os
# Ensure users.json exists
if not os.path.exists('users.json'):
    with open('users.json', 'w') as f:
        json.dump([], f)
st.set_page_config(page_title="Sign Up", layout="wide", page_icon="", initial_sidebar_state="collapsed")
st.markdown("<h1 style='text-align: center; color: #0bb; padding: 20px'> Sign Up</h1>", unsafe_allow_html=True)

# Signup form
with st.form("signup_form"):
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    submit_button = st.form_submit_button("Sign Up")
    if submit_button:
        if password == confirm_password:
            with open("users.json", "r") as f:
                users = json.load(f)
            users[username] = password
            with open("users.json", "w") as f:
                json.dump(users, f)
            st.success("Sign up successful!")
            st.experimental_rerun()
        else:
            st.error("Passwords do not match.")

# Redirect to login if button clicked
if st.button("Login", key="login_button"):
    st.session_state.is_logged_in = False
    st.session_state.user = None
    st.switch_page("pages/login.py")
# Redirect to home if already logged in
if "user" in st.session_state:
    st.session_state.is_logged_in = True
    st.switch_page("Home.py")
    st.success(f"Welcome back, {st.session_state.user}!")
    st.experimental_rerun()
    