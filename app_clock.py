import streamlit as st
import reqease
from shop_ulrs import PublicAPIs

st.set_page_config(page_title="AgoraOps Hub | 🕐 App o'clock",
                       page_icon="🎛️",layout="wide")


STOCK_API = 'https://tapi.telstra.com/presentation/v1/ecommerce-products/con/stocks'
# New Sotck
def get_stocks(sku:str) -> int:
    stocks_maui_api = reqease.Get(STOCK_API).to_dict
    stocks = stocks_maui_api['data']['stocks']
    for stock in stocks:
        if stock['sku'] == sku:
            return stock['stockLevel']

st.markdown("<h1>Units Available</h1>", unsafe_allow_html=True)
st.markdown("<h2>Prepaid</h2>", unsafe_allow_html=True)

left, right = st.columns([0.3, 0.7], vertical_alignment="center")
left.html(f'''🔥 $39 Pre-Paid SIM Starter Kit''')
click_units_left = right.button("👉 Units Left")
if click_units_left:
    st.html(f'''
            <span style="font-size: 2rem; font-weight: bold; color: #e63946; background-color: #ffe5e5; padding: 0.5rem 1rem; border-radius: 0.5rem;">
                {get_stocks('100253952')}
            </span>''')