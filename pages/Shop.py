import streamlit as st
import time
import streamlit.components.v1 as components
import webbrowser as wb

st.set_page_config(page_title="Shop", layout="centered", page_icon="🛒",initial_sidebar_state = "expanded")
st.title("🧺 Products")

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
# Custom component to show a toast message
def show_toast(message):
    components.html(f"""
    <div style="
        position: fixed;
        top: 20px;
        right: 20px;
        background-color: #28a745;
        color: white;
        padding: 16px;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.3);
        z-index: 9999;
        animation: fadeOut 3s forwards;
    ">
        <strong>{message}</strong>
    </div>
    <style>
    @keyframes fadeOut {{
        0% {{opacity: 1;}}
        100% {{opacity: 0;}}
    }}
    </style>
    """, height=100)
session = False

if "cart" not in st.session_state:
    st.session_state.cart = {}
if "show_toast" not in st.session_state:
    st.session_state.show_toast = False
if "needs_rerun" not in st.session_state:
    st.session_state.needs_rerun = False

products = {
    "Soap 1": 100,
    "Soap 2": 120,
    "Soap 3": 90,
    "Soap 4": 110,
    "Soap 5": 95,
    "Soap 6": 130,
}

st.sidebar.subheader("🛍️ Your Cart")
total = 0
if not st.session_state.cart:
    st.sidebar.info("Your cart is empty 🛒")
else:
    for item, qty in st.session_state.cart.items():
        item_total = products[item] * qty
        st.sidebar.write(f"{item} x {qty} = RS. {item_total}")
        total += item_total
    st.sidebar.markdown(f"**Total: RS. {total}**")

if st.sidebar.button("🧹 Clear Cart"):
    st.session_state.cart.clear()
    session = True
for item in list(st.session_state.cart.keys()):
    if st.sidebar.button(f"Remove {item}", key=f"remove_{item}"):
        del st.session_state.cart[item]
        session = True

if st.sidebar.button("Confirm Cart"):
    st.session_state.show_toast = True

for i, (item, price) in enumerate(products.items()):
    col1, col2 = st.columns([4, 1])
    with col1:
        st.write(f"**{item}** — RS. {price}")
    with col2:
        if st.button(f"Add {item}", key=f"add_{item}"):
            st.session_state.cart[item] = st.session_state.cart.get(item, 0) + 1
            session = True

if st.session_state.show_toast:
    st.markdown("""
    <div style="
        position: fixed;
        top: 20px;
        right: 20px;
        background-color: #28a745;
        color: white;
        padding: 16px;
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.3);
        z-index: 9999;
        animation: fadeOut 3s forwards;
    ">
        <strong>✅ YOUR CART HAS BEEN CONFIRMED</strong>
    </div>
    <style>
    @keyframes fadeOut {
        0% {opacity: 1;}
        100% {opacity: 0;}
    }
    </style>
    """, unsafe_allow_html=True)
    st.session_state.show_toast = False

st.markdown("---")
if st.button("🛒 View Cart / Checkout"):
    st.switch_page("pages/Checkout.py")

if st.button("🏠 Back to Home"):
    st.switch_page("Home.py")

if session == True:
    st.rerun()