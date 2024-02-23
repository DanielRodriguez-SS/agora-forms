import streamlit as st
import frontend.styling as css
import requests
import pandas as pd

st.set_page_config(page_title="AgoraOps Hub | Console Pull",
                       page_icon="🎛️")
css.hide_streamlit_defualt_menu_footer()
css.set_footer()

def get_products_data(sku_list:list)->list:
    products = []
    for sku in sku_list:
        products.append({"productType":"RIMS","productId":sku,"quantity":1})
    return products

url = 'https://tapi.telstra.com/v1/logistics/ext/stock-check'
# products = [{"productType":"RIMS","productId":"100253285","quantity":1},
#             {"productType":"RIMS","productId":"100253284","quantity":1},
#             {"productType":"RIMS","productId":"100253286","quantity":1},
#             {"productType":"RIMS","productId":"100253287","quantity":1},
#             {"productType":"RIMS","productId":"100253299","quantity":1},
#             {"productType":"RIMS","productId":"100253300","quantity":1},
#             {"productType":"RIMS","productId":"100253279","quantity":1},
#             {"productType":"RIMS","productId":"100253280","quantity":1},
#             {"productType":"RIMS","productId":"100253281","quantity":1},
#             {"productType":"RIMS","productId":"100253282","quantity":1},
#             {"productType":"RIMS","productId":"100253302","quantity":1},
#             {"productType":"RIMS","productId":"100253305","quantity":1}]


st.markdown("# Experimental")

skus_raw_test = st.text_area("Paste SKUs")
sku_list = skus_raw_test.split("\n")
st.write(f'{len(sku_list)} SKUs added')
products = get_products_data(sku_list)
paidload = {"correlationId":"5f8404f6-7606-44dc-979f-fb562d3323b4","data":{"isExplore":True,"lineOfBusiness":"035","products":products}}


pull_console = st.button('Find on Console')
if pull_console:
    st.write('Try to find')
    response = requests.post(url, json=paidload, headers={"ConsumerId":"0KhnFrg3bhvNW38ofwPGVMHoR2luZUlG"})
    if response.status_code == 200:
        data = response.json()
        # st.write(data['data']['stockItems'])
        st.dataframe(pd.DataFrame(data['data']['stockItems']),use_container_width=True,hide_index=True)
    else:
        st.write(f'Failed to find data. {response.status_code}')