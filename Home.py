import streamlit as st
import json
import os

if not os.path.exists('reviews.json'):
    with open('reviews.json', 'w') as f:
        json.dump([], f)

st.set_page_config(
    page_title="RADIANT SUDS",
    page_icon="🛁",
    layout="centered",
    initial_sidebar_state="expanded",
)
# Custom Logo
st.markdown("""
    <style>
        body {
            background-color: #f0f8ff;  /* Light blue background */
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
        /* ✅ Logo positioning */
        .custom-logo {
            position: fixed;
            top: 12px;
            left: 50px;  /* Adjust this to move logo to the right */
            z-index: 1000;
            transition: opacity 0.3s ease-in-out;
            cursor: pointer;
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
        .stTextInput > div > label {
            font-size: 16px;
            font-weight: bold;
        }
        .stTextInput > div {
            margin-bottom: 20px;
        }
        [data-baseweb="select"] {
            border-radius: 8px;
            border: 1px solid #ccc;
            padding: 10px;
            font-size: 16px;
        }
        [data-baseweb="select"]:focus {
            outline: none;
            border-color: #007BFF;
            box-shadow: 0 0 0 3px rgba(0, 123, 255, 0.5);
        }
        [data-baseweb="select"] > label {
            font-size: 16px;
            font-weight: bold;
        }
        [data-baseweb="select"] > div {
            margin-bottom: 20px;
        }
        /* ✅ Logo image styling */
        .custom-logo img {
            height: 36px;
            opacity: 0.95;
            padding: 10px;
            transition: opacity 0.3s ease-in-out, transform 0.3s ease-in-out;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }

        /* ✅ Hover effects */
        .custom-logo:hover img {
            opacity: 1;
            transform: scale(1.05);
        }

        .stButton>button {
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

        .stButton>button:hover {
            background-color: #C7B8EA;
            color: #fff;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        }

        /* ❌ Skip trying to move this – leave as is */
        /* [data-testid="collapsedControl"] won't reliably shift position */
    </style>

    <div class="custom-logo">
        <img src="https://i.ibb.co/nsbC1w9K/radiantsuds.png" alt="Radiant Suds Logo" />
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
        [data-testid="stSidebarNav"] {
            display: none;
        }
    </style>
""", unsafe_allow_html=True)

st.sidebar.image("https://i.ibb.co/nsbC1w9K/radiantsuds.png", width=220)

# Check if user is logged in
if "is_logged_in" not in st.session_state or not st.session_state.is_logged_in:
    st.warning("Please log in to access the full features of Radiant Suds.")
else:
    st.success(f"Welcome back, {st.session_state.user}!")
col1, col2 = st.sidebar.columns([1, 3])

with col1:
    if st.sidebar.button("Sign Up"):
        st.session_state.is_logged_in = False
        st.session_state.user = None
        st.switch_page("pages/signup.py")

with col2:
    if st.sidebar.button("Login"):
        st.session_state.is_logged_in = False
        st.session_state.user = None
        st.switch_page("pages/login.py")

# Styling

st.markdown("""
    <style>
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
        .success-box {
            border-left: 6px solid #4CAF50;
        }
        .feedback {
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }
        .feedback h2 {
            color: #064b4f;
            font-size: 20px;
            margin-bottom: 10px;
        }
        .feedback p {
            color: #333;
            font-size: 16px;
            margin-bottom: 10px;
        }
        .feedback .stButton>button {
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
        .feedback .stButton>button:hover {
            background-color: #C7B8EA;
            color: #fff;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
        }
    </style>
""", unsafe_allow_html=True)

# Header and descriptions (full text)
st.markdown('<div class="title-card">🛁 Radiant Suds Soap(home delivery)</div>', unsafe_allow_html=True)

st.markdown("""
<div class="info-box">
Radiant Suds is a handcrafted bath and body brand dedicated to bringing you the purest indulgence in every bar. Made with love, care, and high-quality natural ingredients, our soaps are gentle on the skin and rich in nourishment. From refreshing scents to skin-loving botanicals, each product is designed to elevate your self-care routine. Whether you're treating yourself or gifting someone special, Radiant Suds delivers beauty, simplicity, and radiance in every lather.
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="success-box">
Radiant Suds is where skincare meets craftsmanship. We create small-batch, handmade soaps using natural oils, botanical extracts, and uplifting scents to nourish your skin and awaken your senses. Each bar is a blend of purity and passion, crafted with care to bring you a refreshing, radiant experience every day. At Radiant Suds, we believe beauty should be simple, soothing, and rooted in nature.
</div>
""", unsafe_allow_html=True)

# Sidebar Contact
contact = st.sidebar.selectbox(
    "📞 Contact Us",
    ["Choose how to contact us", "Email", "Phone"]
)

if contact == "Email":
    st.sidebar.info("📧 _________@gmail.com")
elif contact == "Phone":
    st.sidebar.success("📱 03XX XXX XXXX  or  +92 XXX XXX XXXX")
else:
    st.sidebar.warning("Please select a contact method.")

# Shop Button
if st.sidebar.button("🛍️ Shop Radiant Suds - Reasonable Prices, Reasonable beauty, Reasonable Everything"):
    st.switch_page("pages/Shop.py")

# Sidebar Feedback Form (fixed version with full style)
with st.sidebar:
    st.markdown('<div class="feedback">', unsafe_allow_html=True)
    st.markdown("### Feedback")
    st.markdown("We value your feedback! Please let us know how we can improve.")

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
st.markdown("### 💬 What others said:")

with open('reviews.json', 'r') as f:
    reviews = json.load(f)

if reviews:
    for review in reviews:
        st.write(f"{review['rating']} - {review['comment']}")
else:
    st.info("No feedback yet. Be the first to leave a comment!")
