import streamlit as st
import json
import os

# Create reviews file if it doesn't exist
if not os.path.exists('reviews.json'):
    with open('reviews.json', 'w') as f:
        json.dump([], f)

st.set_page_config(
    page_title="RADIANT SUDS",
    page_icon="🛁",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Global CSS to remove white boxes and style elements
st.markdown("""
    <style>
        body {
            background-color: #f0f8ff;
        }
        #MainMenu, footer, header {visibility: hidden;}
        .custom-logo {
            position: fixed;
            top: 12px;
            left: 50px;
            z-index: 1000;
            transition: opacity 0.3s ease-in-out;
            cursor: pointer;
        }
        .custom-logo img {
            height: 36px;
            opacity: 0.95;
            padding: 10px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            transition: opacity 0.3s ease-in-out, transform 0.3s ease-in-out;
        }
        .custom-logo:hover img {
            opacity: 1;
            transform: scale(1.05);
        }
        .stTextInput > div > input {
            border-radius: 8px;
            border: 1px solid #ccc;
            padding: 10px;
            font-size: 16px;
        }
        .stTextInput > div > input:focus {
            outline: none;
            border-color: #007BFF;
            box-shadow: 0 0 0 3px rgba(0, 123, 255, 0.5);
        }
        .stButton>button {
            background-color: #8BC34A;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
            text-transform: uppercase;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s ease-in-out;
        }
        .stButton>button:hover {
            background-color: #C7B8EA;
            color: #fff;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        }
        .title-card {
            border-radius: 12px;
            background: linear-gradient(to right, #d1f5f5, #e0fafa);
            padding: 40px 30px;
            text-align: center;
            font-size: 26px;
            color: #064b4f;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            max-width: 600px;
            margin: 40px auto 20px auto;
        }
        .info-box, .success-box {
            background-color: #f9ffff;
            border-left: 6px solid #0bb;
            padding: 15px 25px;
            border-radius: 10px;
            margin: 20px auto;
            max-width: 700px;
            font-size: 17px;
        }
        .success-box { border-left: 6px solid #4CAF50; }
        .feedback {
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        .feedback h2 { color: #064b4f; font-size: 20px; margin-bottom: 10px; }
        .feedback p { color: #333; font-size: 16px; margin-bottom: 10px; }
        .feedback .stButton>button {
            background-color: #8BC34A;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
            border: none;
            cursor: pointer;
        }
        .feedback .stButton>button:hover {
            background-color: #C7B8EA;
            color: #fff;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        }
        [data-testid="stSidebarNav"] { display: none; }
        button[kind="header"] {
            background-color: #8BC34A !important;
            color: white !important;
            font-weight: bold;
            border-radius: 8px !important;
            padding: 6px 12px !important;
            border: none !important;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
            transition: all 0.3s ease-in-out;
            display: block !important;
        }
        header {
            visibility: visible !important;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            z-index: 1000;
            background-color: transparent !important; /* Transparent background */
            box-shadow: none !important; /* No shadow */}

        /* On hover */
        button[kind="header"]:hover {
            background-color: #C7B8EA !important;  /* Light purple on hover */
            color: #fff !important;
            transform: scale(1.05);
        }

        /* ❌ REMOVE white Streamlit container backgrounds */
        .block-container,
        section.main > div:first-child,
        div[data-testid="stVerticalBlock"] > div,
        div[data-testid="column"] > div {
            background-color: transparent !important;
            box-shadow: none !important;
            padding: 0 !important;
            margin: 0 !important;
            border: none !important;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
        .custom-footer {
            justify-content: center;
            display: flex;
            align-items: center;
            font-family: 'Arial', sans-serif;
            font-size: 14px;
            text-align: center;
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background: #e0fafa;
            color: #064b4f;
            text-align: center;
            padding: 10px;
            font-size: 14px;
            font-weight: bold;
            box-shadow: 0 -2px 10px rgba(0,0,0,0.1);
            z-index: 100;
        }
    </style>

    <div class="custom-footer">
        🛁 Radiant Suds &nbsp; | &nbsp; Beautiful Skin, Naturally Yours &nbsp; | &nbsp; © 2025 All rights reserved
    </div>
""", unsafe_allow_html=True)

# Floating logo
st.markdown("""""", unsafe_allow_html=True)

# Sidebar
st.sidebar.image("https://i.ibb.co/nsbC1w9K/radiantsuds.png", width=220)

# Login Check
if "is_logged_in" not in st.session_state or not st.session_state.is_logged_in:
    st.warning("Please log in to access the full features of Radiant Suds.")
else:
    st.success(f"Welcome back, {st.session_state.user}!")

col1, col2 = st.sidebar.columns([1, 3])
with col1:
    if st.sidebar.button("Sign Up"):
        st.session_state.is_logged_in = False
        st.session_state.user = None
        st.switch_page("pages/Signup.py")
with col2:
    if st.sidebar.button("Login"):
        st.session_state.is_logged_in = False
        st.session_state.user = None
        st.switch_page("pages/Login.py")

# Header + Info
st.markdown('<div class="title-card">🛁 Radiant Suds Soap (home delivery)</div>', unsafe_allow_html=True)
st.markdown("""
<div class="info-box">
Radiant Suds is a handcrafted bath and body brand dedicated to bringing you the purest indulgence in every bar. Made with love, care, and high-quality natural ingredients, our soaps are gentle on the skin and rich in nourishment.
</div>
""", unsafe_allow_html=True)
st.markdown("""
<div class="success-box">
Radiant Suds is where skincare meets craftsmanship. We create small-batch, handmade soaps using natural oils, botanical extracts, and uplifting scents to nourish your skin and awaken your senses.
</div>
""", unsafe_allow_html=True)

# Contact
contact = st.sidebar.selectbox("📞 Contact Us", ["Choose how to contact us", "Email", "Phone"])
if contact == "Email":
    st.sidebar.info("📧 _________@gmail.com")
elif contact == "Phone":
    st.sidebar.success("📱 03XX XXX XXXX or +92 XXX XXX XXXX")
else:
    st.sidebar.warning("Please select a contact method.")

# Shop button
if st.sidebar.button("🛍️ Shop Radiant Suds - Reasonable Prices, Reasonable beauty, Reasonable Everything"):
    st.switch_page("pages/Shop")

# Feedback section
with st.sidebar:
    st.markdown('<div class="feedback">', unsafe_allow_html=True)
    st.markdown("### Feedback")
    rating = st.selectbox("Rate us:", ["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"])
    comment = st.text_area("Your feedback:")
    if st.button("Submit Feedback"):
        if comment.strip():
            with open('reviews.json', 'r+') as f:
                data = json.load(f)
                data.append({"rating": rating, "comment": comment})
                f.seek(0)
                json.dump(data, f, indent=4)
            st.success("Thank you for your feedback!")
        else:
            st.error("Please write a comment before submitting.")
    st.markdown('</div>', unsafe_allow_html=True)

# Display reviews
st.markdown("### 💬 What others said:")
with open('reviews.json', 'r') as f:
    reviews = json.load(f)

if reviews:
    for review in reviews:
        st.write(f"{review['rating']} - {review['comment']}")
else:
    st.info("No feedback yet. Be the first to leave a comment!")
