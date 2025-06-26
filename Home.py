import streamlit as st

st.set_page_config(
    page_title="RADIANT SUDS",
    page_icon="🛁",
    layout="centered"
)

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
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title-card">🛁 Radiant Suds Soap(home delivery)</div>', unsafe_allow_html=True)

st.markdown('<div class="info-box">Radiant Suds is a handcrafted bath and body brand dedicated to bringing you the purest indulgence in every bar. Made with love, care, and high-quality natural ingredients, our soaps are gentle on the skin and rich in nourishment. From refreshing scents to skin-loving botanicals, each product is designed to elevate your self-care routine. Whether you\'re treating yourself or gifting someone special, Radiant Suds delivers beauty, simplicity, and radiance in every lather.</div>', unsafe_allow_html=True)

st.markdown('<div class="success-box">Radiant Suds is where skincare meets craftsmanship. We create small-batch, handmade soaps using natural oils, botanical extracts, and uplifting scents to nourish your skin and awaken your senses. Each bar is a blend of purity and passion, crafted with care to bring you a refreshing, radiant experience every day. At Radiant Suds, we believe beauty should be simple, soothing, and rooted in nature.</div>', unsafe_allow_html=True)

contact = st.sidebar.selectbox(
    "📞 Contact Us",
    ["Choose how to contact us", "Email", "Phone"]
)

if contact == "Email":
    st.sidebar.info("📧 nida.akhlaq@gmail.com")
elif contact == "Phone":
    st.sidebar.success("📱 0322 400 1910  or  +92 322 4001910")
else:
    st.sidebar.warning("Please select a contact method.")


if st.sidebar.button("🛍️ Shop Radiant Suds - Reasonable Prices, Reasonable beauty, Reasonable Everything"):
    st.switch_page("pages/shop.py")

st.sidebar.markdown("""
<blockquote style="opacity: 100%;
                   background: bisque;
                   border-radius: 20px;
                   display: flex;
                   justify-content: center;"><tt style="font-size: large;"><Address>
    <hr style="margin: 50px;">
    phone number : 03224001910<br>
    email : nida.akhlaq@gmail.com<br>
    address : askari 10<br>
    <div style="margin-top:0px ;
                       margin-left: 87px;
                      ">sector C<br>
              house no.294<br></div>
</Address></tt></blockquote>""", unsafe_allow_html = True)


sentiment_mapping = ["one", "two", "three", "four", "five"]
selected = st.sidebar.feedback("stars")
if selected is not None:
    st.sidebar.markdown(f"⭐ You selected {sentiment_mapping[selected]} star(s). Thank you for helping us improve!")