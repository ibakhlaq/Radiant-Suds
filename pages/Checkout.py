import streamlit as st

st.set_page_config(page_title="Checkout", layout="wide", page_icon="", initial_sidebar_state="collapsed")

# Header Section
st.markdown("<h1 style='text-align: center; color: #0bb; padding: 20px'> Checkout</h1>", unsafe_allow_html=True)

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
        .element-container:has(.stAlert) {
            background-color: #f9ffff;
            border-left: 6px solid #0bb;
            padding: 15px 25px;
            border-radius: 10px;
            margin: 5px auto;
            max-width: 700px;
            font-size: 17px;
        }
        .element-container:has(.stAlert) .stAlert > div > p {
            margin: 0;
        }
    </style>
    """, unsafe_allow_html=True)

# Cart Section
cart = st.session_state.get("cart", {})

if not cart:
    st.error("Your cart is empty.")
    if st.button("GO TO SHOP", key="go_to_shop_empty"):
        st.switch_page("pages/Shop.py")
    if st.button("GO TO MAIN PAGE", key="go_to_home_empty"):
        st.switch_page("Home.py")
else:
    st.subheader("Cart Items:")
    total = 0
    price_list = {"Soap 1": 100, "Soap 2": 120, "Soap 3": 90, "Soap 4": 110, "Soap 5": 95, "Soap 6": 130}
    for item, quantity in cart.items():
        price = price_list.get(item, 0)
        subtotal = price * quantity
        total += subtotal
        st.write(f"{item} x {quantity} — RS. {subtotal}")

    # Total Section
    st.markdown("---")
    st.markdown(f"### : **RS. {total}**")

    # Call to Action Section
    if st.button("PLACE ORDER", key="place_order"):
        st.success("Thank you for your purchase!")
        st.session_state.cart = {}
        st.rerun()

    # Navigation Section
    if cart:
        if st.button("BACK TO SHOP", key="back_to_shop"):
            st.switch_page("pages/Shop.py")
        if st.button("BACK TO HOME", key="back_to_home"):
            st.switch_page("Home.py")