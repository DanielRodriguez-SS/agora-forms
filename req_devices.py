import streamlit as st
import frontend.styling as css
from shop_map import tree
from dataclasses import dataclass
from pdf_builder import export_new_products
import datetime
import pandas as pd

@dataclass
class LaunchDetails:
    launch_date:str = '_NA'
    launch_time:str = '_NA'
    stock_notice:str = '_NA'

if 'product_data' not in st.session_state:
    product_data = {}
    product_data['Shop'] = []
    product_data['Device'] = []
    product_data['Brand'] = []
    product_data['Name'] = []
    product_data['Size'] = []
    product_data['Color'] = []
    product_data['SKU'] = []
    product_data['Price'] = []
    st.session_state.product_data = product_data

st.set_page_config(page_title="AgoraOps Hub | Products", page_icon="🎛️", layout="wide")
css.hide_streamlit_defualt_menu_footer()

def validate_inputs(inputs:list) -> bool:
    for input in inputs:
        if not input:
            st.toast('Missing information!', icon='❌')
            return False
    return True

def add_device(shop:str, device:str, brand:str, name:str, size:str, color:str, sku:str, price:float):
    if validate_inputs([shop,device,brand,name,size,color,sku,price]):
        st.session_state.product_data['Shop'].append(shop)
        st.session_state.product_data['Device'].append(device)
        st.session_state.product_data['Brand'].append(brand)
        st.session_state.product_data['Name'].append(name)
        st.session_state.product_data['Size'].append(size)
        st.session_state.product_data['Color'].append(color)
        st.session_state.product_data['SKU'].append(sku)
        st.session_state.product_data['Price'].append(price)


def delete_product(index:int):
    st.session_state.product_data.pop(index)

def export_file(file_name:str):
    if file_name:
        pass
    else:
        st.toast("'File name' is empty", icon='❌')


st.write("# Tell us more about this new product")

left_side, right_side = st.columns([0.4, 0.6])

with st.spinner('Searching for available products in AGORA'):
    shops = list(tree.keys())

launch_details = LaunchDetails()

# if st.session_state.product_data['SKU']:
#     right_side.write("## Products")
#     right_side.text("Export to file:")
#     right_side.data_editor(pd.DataFrame(st.session_state.product_data),use_container_width=True, hide_index=True)
#     row12_col1, row12_col2 = right_side.columns(2, vertical_alignment='bottom')
#     export_file_name = row12_col1.text_input("File name:", placeholder='Prepaid Launch')
#     if export_file_name:
#         pdf = export_new_products(pd.DataFrame(st.session_state.product_data), launch_details)

#         row12_col2.download_button(
#                  label="Export PDF",
#                  data=pdf,
#                  file_name=f'{export_file_name}.pdf',
#                  mime='application/octet-stream',
#              )



left_side.write("## Details")
row1_col1,row1_col2 = left_side.columns(2)
shop = row1_col1.selectbox("Shop:",shops)
device_types:dict = tree[shop]['Device Type']
device_type = row1_col2.selectbox("Device Type:", device_types)
row2_col1,row2_col2 = left_side.columns(2)
launch_date = row2_col1.date_input('Lauch Date:')
launch_details.launch_date = launch_date
lauch_time = row2_col2.time_input('Lauch Time:',datetime.time(), step=60)
launch_details.launch_time = lauch_time
stock_notice = left_side.text_area('Stock Notice:',placeholder="Available Now.")
launch_details.stock_notice = stock_notice

row3_col1, row3_col2 = left_side.columns(2)
row4_col1, row4_col2, row4_col3, row4_col4 = left_side.columns(4)

device_brand = row3_col1.text_input("Brand:", placeholder=device_types[device_type]['placeholder_brand'])
device_name = row3_col2.text_input("Device name:", placeholder=device_types[device_type]['placeholder_name'])

if device_type == "Handsets" or device_type == "Tablet" or device_type == 'Mbb':
    
    device_size = row4_col1.selectbox("Size:", ['NA', '64GB', '128GB', '256GB', '512GB', '1TB', '2TB'])
    device_color = row4_col2.text_input("Color:", placeholder='Deep Blue')
    device_sku = row4_col3.text_input("SKU:", placeholder='10002543..')
    device_price = row4_col4.number_input("Price (AUD):")

else:
    device_size = "NA"
    device_color = "NA"
    device_sku = row3_col1.text_input("SKU:", placeholder='10002543..')
    device_price = row3_col2.number_input("Price (AUD):")

left_side.button(
    "Add",
    on_click=add_device,
    args=[
        shop,
        device_type,
        device_brand,
        device_name,
        device_size,
        device_color,
        device_sku,
        device_price
    ]
)

if st.session_state.product_data['SKU']:
    right_side.write("## Products")
    right_side.text("Export to file:")
    right_side.data_editor(pd.DataFrame(st.session_state.product_data),use_container_width=True, hide_index=True)
    row12_col1, row12_col2 = right_side.columns(2, vertical_alignment='bottom')
    export_file_name = row12_col1.text_input("File name:", placeholder='Prepaid Launch')
    if export_file_name:
        pdf = export_new_products(pd.DataFrame(st.session_state.product_data), launch_details)

        row12_col2.download_button(
                 label="Export PDF",
                 data=pdf,
                 file_name=f'{export_file_name}.pdf',
                 mime='application/octet-stream',
             )