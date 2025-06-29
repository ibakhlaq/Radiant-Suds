import streamlit as st
import time

st.set_page_config(page_title="Shop", layout="centered", page_icon="🛒")
st.title("🧺 Products")

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
        st.session_state.needs_rerun = True

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
    st.switch_page("Checkout")

if st.button("🏠 Back to Home"):
    st.switch_page("Home")

if session == True:
    st.rerun()