import streamlit as st
import reqease

st.set_page_config(page_title="AgoraOps Hub | 🏷️ Live Now",
                       page_icon="🎛️",layout="wide")

URL_PREPAID_MOBILES = "https://tapi.telstra.com/presentation/v1/ecommerce-products/products/mobility/PREPAID/PREPAID_MOBILE/NEW"
URL_PREPAID_TABLETS = 'https://tapi.telstra.com/presentation/v1/ecommerce-products/products/mobility/PREPAID/PREPAID_TABLET/NEW'
URL_PREPAID_MBB = 'https://tapi.telstra.com/presentation/v1/ecommerce-products/products/mobility/PREPAID/PREPAID_MBB/NEW'
URL_BOOST = 'https://tapi.telstra.com/presentation/v1/ecommerce-products/products/mobility/BOOST/BOOST/NEW'

@st.cache_data(ttl=3600)
def get_live_promos(data:dict, shop_link:str = 'telstra', segment:str='prepaid',segment_parm:str = '') -> None:
    promos = data['data']['promos']
    devices_families = data['data']['deviceFamilies']
    promos_dict = {}
    for promo in promos:
        promos_dict[promo['id']] = {"code":promo['code'], "name": promo['name'], "type":promo['type'], "discount":promo['credits'][0]['amount']}
    
    for family in devices_families:
        devices = family['devices']
        for device in devices:
            if device['promos']:
                promo = device['promos'][0]
                st.html(f'''🔥 {device['code']} - {device['name']} - {promos_dict[promo]['code']} / ({promos_dict[promo]['type']}, {(promos_dict[promo]['discount'])/100} AUD off) 
                        <a style="text-decoration:none;" href="https://checkout.{shop_link}.com.au/consumer/{segment}?sku={device['code']}{segment_parm}" target="_blank">🔗 Buy</a>''')
                #print(f"{device['code']} - {device['name']} - {promos_dict[promo]['code']} / ({promos_dict[promo]['type']}, {(promos_dict[promo]['discount'])/100} AUD off)")

st.markdown("<h1>Promotions</h1>", unsafe_allow_html=True)
st.markdown("<h2>Prepaid</h2>", unsafe_allow_html=True)

st.markdown("<h3>Mobile</h2>", unsafe_allow_html=True)
prepaid_mobile_data = reqease.Get(URL_PREPAID_MOBILES).to_dict
get_live_promos(prepaid_mobile_data)

st.markdown("<h3>Tablets</h2>", unsafe_allow_html=True)
prepaid_table_data = reqease.Get(URL_PREPAID_TABLETS).to_dict
get_live_promos(prepaid_table_data, segment_parm="&deviceType=tablet")

st.markdown("<h3>Mbb</h2>", unsafe_allow_html=True)
prepaid_mbb_data = reqease.Get(URL_PREPAID_MBB).to_dict
get_live_promos(prepaid_mbb_data, segment_parm="&deviceType=mbb")

st.markdown("<h2>Boost</h2>", unsafe_allow_html=True)
boost_data = reqease.Get(URL_BOOST).to_dict
get_live_promos(boost_data, shop_link='boost', segment='boost')