import streamlit as st

st.set_page_config(page_title="Checkout", layout="wide", page_icon="🧾")
st.title("🧾 Checkout")

cart = st.session_state.get("cart", {})

if not cart:
    st.warning("Your cart is empty.")
    if st.button("🛍️ Go to Shop"):
        st.switch_page("pages/Shop.py")
    if st.button("🏠 Go to main page"):
        st.switch_page("Home")
else:
    st.subheader("Cart Items:")
    total = 0
    price_list = {"Soap 1": 100, "Soap 2": 120, "Soap 3": 90, "Soap 4": 110, "Soap 5": 95, "Soap 6": 130}
    for item, quantity in cart.items():
        price = price_list.get(item, 0)
        subtotal = price * quantity
        total += subtotal
        st.write(f"{item} x {quantity} — RS. {subtotal}")
    st.markdown("---")
    st.markdown(f"### 🧮 Total: **RS. {total}**")
    if st.button("✅ Place Order"):
        st.success("Thank you for your purchase!")
        st.session_state.cart = {}

if cart:
    if st.button("🔙 Back to Shop"):
        st.switch_page("Shop")
    if st.button("🏠 Back to Home page"):
        st.switch_page("Home")
