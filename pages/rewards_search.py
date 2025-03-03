import streamlit as st
import frontend.styling as css
import reqease

st.set_page_config(page_title="AgoraOps Hub | Rewards 🔍",
                       page_icon="🔍")
css.hide_streamlit_defualt_menu_footer()


# change
REWARDS_CONSUMER = 'https://tapi.telstra.com/presentation/v1/ecommerce-products/products/loyalty_con'

st.markdown("# Rewards 🔍")

sku = st.text_input(("Enter SKU"))


pull_console = st.button('Find')
if pull_console:
    response = reqease.Get(REWARDS_CONSUMER)
    if response.response.status_code == 200:
        data = response.to_dict
        product_families = data['data']['productFamilies']
        requested_id = None
        for family in product_families:
            family_id = family['id']
            products = family['products']
            for product in products:
                if sku == product['sku']:
                    product_name = product['name']
                    requested_id = family_id
                    break
            if requested_id:
                st.write(f'Product Name: {product_name}')
                st.write(f'Link: https://plus.telstra.com.au/rewards/explore/{requested_id}')
                break
        if not requested_id:
            st.write('SKU not found on Rewards Store')

    else:
        st.write('Data not available, please try later')