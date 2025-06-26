import streamlit as st

st.set_page_config(page_title="Checkout", layout="wide", page_icon="🧾")
st.title("🧾 Checkout")

cart = st.session_state.get("cart", {})

if not cart:
    st.warning("Your cart is empty.")
    if st.button("🛍️ Go to Shop"):
        st.switch_page("pages/shop.py")
    if st.button("🏠Go to main page"):
        st.switch_page("Home.py")
else:
    st.subheader("Cart Items:")
    total = 0
    price_list = {"T-shirt": 20, "Shoes": 60, "Hat": 15}
    for item, quantity in cart.items():
        price = price_list.get(item, 0)
        subtotal = price * quantity
        total += subtotal
        st.write(f"{item} x {quantity} — ${subtotal:.2f}")
    st.markdown("---")
    st.markdown(f"### 🧮 Total: **${total:.2f}**")
    if st.button("✅ Place Order"):
        st.success("Thank you for your purchase!")
        st.session_state.cart = {}
if cart:
    if st.button("🔙 Back to Shop"):
        st.switch_page("shop.py")
    if st.button("🏠 Back to Home page"):
        st.switch_page("Home.py")