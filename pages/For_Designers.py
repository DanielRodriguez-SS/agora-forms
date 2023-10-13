import streamlit as st
import frontend.styling as css
import frontend.help.for_designers_page as help_hint
import features.designers as feature
import pandas as pd

if 'images_data' not in st.session_state:
    st.session_state.images_data = []

if 'file_uploader_key' not in st.session_state:
    st.session_state.file_uploader_key = 100

st.set_page_config(page_title="Tools | ForDesigners",
                       page_icon="🧊",layout="wide")
css.hide_streamlit_defualt_menu_footer()

# Define side bar menu
with st.sidebar:
    if st.button('Reset'):
        st.rerun()

# Only for 800X800 Images
REPO_1 = "https://www.telstra.com.au/content/dam/tcom/lego/2022/accessories/products/"
# Other Images Sizes
REPO_2 = "https://www.telstra.com.au/content/dam/tcom/devices/general/hardware/"

image_data_800x800 = {
    "SKU":[],
    "Name":[],
    "Size":[],
    "Color":[],
    "Hex Color":[],
    "Url":[]
}
image_data_900x1200 = {
    "SKU":[],
    "Name":[],
    "Size":[],
    "Color":[],
    "Hex Color":[],
    "Url":[]
}
image_data_1200x900 = {
    "SKU":[],
    "Name":[],
    "Size":[],
    "Color":[],
    "Hex Color":[],
    "Url":[]
}
products_images = []

st.markdown("<h1>🦾 Let's Automate The DAM Thing</h1>",unsafe_allow_html=True)
st.markdown("<h3>Images URLs Builder</h3>",unsafe_allow_html=True)
help_hint.display_help()

col_inputs, col_outputs = st.columns([1,1], gap="medium")

with col_inputs:
    product_sku = st.text_input('Product SKU', placeholder='100252286')
    product_name = st.text_input('Product Name', placeholder='Sprout-AudioPlus TWS Earbuds-Black')
    category = st.text_input('Category', placeholder='earbuds')
    sub_category = st.text_input('Sub-Category (EPC Code)', placeholder='ghdwerb-saptw')
    color = st.text_input('Color', placeholder='black')
    hex_code = st.text_input('Hexcode', placeholder='#000000')

if product_sku and product_name and category and sub_category and color and hex_code:
    files = col_inputs.file_uploader('Slect all images', key=st.session_state.file_uploader_key, accept_multiple_files=True)
    if files:
        for file in files:
            if '800x800' in file.name:
                image_data_800x800['SKU'].append(product_sku)
                image_data_800x800['Name'].append(product_name)
                image_data_800x800['Size'].append('800x800')
                image_data_800x800['Color'].append(color)
                image_data_800x800['Hex Color'].append(hex_code)
                image_data_800x800['Url'].append(f'{REPO_1}{category}/{sub_category}/{color}/{file.name}')
            elif 'landscape' not in file.name:
                image_data_800x800['SKU'].append(product_sku)
                image_data_900x1200['Name'].append(product_name)
                image_data_900x1200['Size'].append('900x1200')
                image_data_800x800['Color'].append(color)
                image_data_900x1200['Hex Color'].append(hex_code)
                image_data_900x1200['Url'].append(f'{REPO_2}{category}/{sub_category}/{color}/{file.name}')
            else:
                image_data_800x800['SKU'].append(product_sku)
                image_data_1200x900['Name'].append(product_name)
                image_data_1200x900['Size'].append('1200x900')
                image_data_800x800['Color'].append(color)
                image_data_1200x900['Hex Color'].append(hex_code)
                image_data_1200x900['Url'].append(f'{REPO_2}{category}/{sub_category}/{color}/{file.name}')
        temp_image_data = {
            "SKU":['']+image_data_800x800['SKU']+image_data_900x1200['SKU']+image_data_1200x900['SKU'],
            "Name":['']+image_data_800x800['Name']+image_data_900x1200['Name']+image_data_1200x900['Name'],
            "Size":['']+image_data_800x800['Size']+image_data_900x1200['Size']+image_data_1200x900['Size'],
            "Color":['']+image_data_800x800['Color']+image_data_900x1200['Color']+image_data_1200x900['Color'],
            'Hex Color':['']+image_data_800x800['Hex Color']+image_data_900x1200['Hex Color']+image_data_1200x900['Hex Color'],
            'Url':['']+image_data_800x800['Url']+image_data_900x1200['Url']+image_data_1200x900['Url']
        }
        save = st.button('Save', on_click=feature.add_product_images, args=[temp_image_data])

with col_outputs:
    number_of_products_saved = len(st.session_state.images_data)
    st.write(f'Products Saved: {number_of_products_saved}')
    col_product_name, col_testButton ,col_deleteButton = st.columns([1,1,1],gap="small")
    for item in range(number_of_products_saved):
        with col_product_name:
            st.write(st.session_state.images_data[item]["Name"][1])
        with col_testButton:
            st.button('Test URLs',key=f'testBt-{item}', on_click=feature.open_urls, args=[item])
        with col_deleteButton:
            st.button('Delete',key=f'deletBt-{item}', on_click=feature.delete_product, args=[item])
    if number_of_products_saved != 0:
        st.divider()
        if number_of_products_saved > 1:
            data_frames = []
            for data_dict in st.session_state.images_data:
                data_frames.append(pd.DataFrame.from_dict(data_dict))
            super_dataFrame = pd.concat(data_frames)
            df_to_export = super_dataFrame   
        else:
            df_to_export = pd.DataFrame.from_dict(st.session_state.images_data[0])
        excel_file_name = st.text_input('File Name:', placeholder='MyURLs')    
        if bool(excel_file_name):
            data_to_export = feature.export_excel(df_to_export)
            st.button('Test URLs', on_click=feature.open_urls)
            st.download_button(
                label="Export .xlsx",
                data=data_to_export,
                file_name=f'{excel_file_name}.xlsx'
            )