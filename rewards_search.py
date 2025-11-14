import streamlit as st
import frontend.styling as css
import reqease
import pandas as pd

st.set_page_config(page_title="AgoraOps Hub | Rewards 🔍",
                       page_icon="🔍",layout="wide")
css.hide_streamlit_defualt_menu_footer()


# change
REWARDS_CONSUMER = 'https://tapi.telstra.com/presentation/v1/ecommerce-products/products/loyalty_con'

st.markdown("# Rewards 🔍")

# sku = st.text_input(("Enter SKU"))


# pull_console = st.button('Find')

# if pull_console:
#     response = reqease.Get(REWARDS_CONSUMER)
#     if response.response.status_code == 200:
#         data = response.to_dict
#         product_families = data['data']['productFamilies']
#         requested_id = None
#         for family in product_families:
#             family_id = family['id']
#             products = family['products']
#             for product in products:
#                 if sku == product['sku']:
#                     product_name = product['name']
#                     requested_id = family_id
#                     break
#             if requested_id:
#                 st.write(f'Product Name: {product_name}')
#                 st.write(f'Link: https://plus.telstra.com.au/rewards/explore/{requested_id}')
#                 break
#         if not requested_id:
#             st.write('SKU not found on Rewards Store')

#     else:
#         st.write('Data not available, please try later')

response = reqease.Get(REWARDS_CONSUMER)
if response.response.status_code == 200:
    data = response.to_dict
    product_families = data['data']['productFamilies']
    data_filtered = {}
    data_filtered['Image'] = []
    data_filtered['Sku'] = []
    data_filtered['Name'] = []
    data_filtered['Stock'] = []
    data_filtered['Promotion'] = []
    data_filtered['Product URL'] = []
    
    for family in product_families:
        for product in family['products']:
            data_filtered['Image'].append(product['images'][0])
            data_filtered['Sku'].append(product['sku'])
            data_filtered['Name'].append(product['name'])
            if product['outOfStock']:
                data_filtered['Stock'].append('OUT')
            else:
                data_filtered['Stock'].append('IN')
            if product['originalPrice']:
                data_filtered['Promotion'].append('ON')
            else:
                data_filtered['Promotion'].append('OFF')
            data_filtered['Product URL'].append(f"https://plus.telstra.com.au/rewards/explore/{family['id']}")
            
    store_df = pd.DataFrame(data_filtered)

    col_left, col_right = st.columns([.3, .7])
    with col_left:
        st.markdown(
            f"""<h4>Products: {store_df['Sku'].size}</h4>
                <h4>In Stock: {(store_df['Stock'] == "IN").sum()}</h4>
                <h4>Out Stock: {(store_df['Stock'] == "OUT").sum()}</h4>
            """
        ,unsafe_allow_html=True)

    with col_right:
        st.markdown(
            f"""<h4>Promotions: {(store_df['Promotion'] == "ON").sum()}</h4>
                <h4>Promos Out Stock: {((store_df['Promotion'] == "ON") & (store_df['Stock'] == "OUT")).sum()}</h4>
                
            """
        ,unsafe_allow_html=True)

    st.dataframe(
        store_df, 
        column_config= {
            "Product URL": st.column_config.LinkColumn(),
            "Image": st.column_config.ImageColumn(width="small")
        },
        hide_index=True, 
        use_container_width=True
    )
    