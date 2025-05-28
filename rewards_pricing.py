import streamlit as st
import pandas as pd

st.set_page_config(page_title="AgoraOps Hub | 💲 Rewards Pricing",
                       page_icon="🎛️",layout="wide")

st.title('Rewards Pricing Calculator')


price_details_text = st.text_area('Price details list:', placeholder='SKU RRP VPP\n1000252526 250 0.002121212121')

point_tiers = [
    0,
    1000,
    2000,
    3000,
    4000,
    5000,
    6000,
    8000,
    10000,
    12000,
    14000,
    16000,
    18000,
    20000,
    22000,
    24000,
    26000,
    28000,
    30000,
    35000,
    40000,
    45000,
    50000,
    60000,
    70000,
    80000,
    90000,
    100000,
    120000,
    140000,
    160000,
    180000,
    200000,
    250000,
    300000,
    350000,
    400000,
    450000,
    500000,
    600000,
    700000,
    800000,
    900000,
    1000000,
    1100000,
    1200000,
    1300000,
    1400000,
    1500000,
    2000000,
    2500000
]

data = {
    "Sku": [],
    "Points": [],
    "Pay": []
}

calculate_price = st.button('Calculate Price')
if calculate_price:
    products = price_details_text.split('\n')
    for product in products:
        sku, rrp, vpp = product.split('\t')
        outrightPoints = round((float(rrp)/1.1)/float(vpp), -2)
        current_price = float(rrp)
        i = 0
        while(current_price >= 0 and (point_tiers[i] < int(outrightPoints))):
            if i:
                data['Sku'].append('')
            else:
                data['Sku'].append(sku)
            data['Pay'].append(round(current_price, 2))
            data['Points'].append(point_tiers[i])
            current_price = float(rrp) - (point_tiers[i+1]*float(vpp)*1.1)
            i += 1
        data['Sku'].append('')
        data['Pay'].append(0)
        data['Points'].append(int(outrightPoints))
    st.dataframe(pd.DataFrame(data),use_container_width=True, hide_index=True)