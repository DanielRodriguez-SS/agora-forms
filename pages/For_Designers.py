import streamlit as st
import frontend.styling as css
import frontend.help.for_designers_page as help_hint
import features.f_designers as feature
import data.d_designers as data
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

st.markdown("<h1>🦾 Let's Automate The DAM Thing</h1>",unsafe_allow_html=True)
st.markdown("<h3>Images URLs Builder</h3>",unsafe_allow_html=True)
help_hint.display_help()
segment = st.selectbox('Segment',['Accessories','Mobility'])

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
        if segment == 'Accessories':
            temp_image_data = feature.process_images_names_for_acc_tplus(files,
                                                                     product_sku,
                                                                     product_name,
                                                                     category,
                                                                     sub_category,
                                                                     color,
                                                                     hex_code)
        else:
            temp_image_data = feature.process_images_names_for_mobility(files,
                                                                     product_sku,
                                                                     product_name,
                                                                     category,
                                                                     sub_category,
                                                                     color,
                                                                     hex_code)
        st.button('Save', on_click=feature.add_product_images, args=[temp_image_data])

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
        excel_file_name = st.text_input('File Name',help='To export file, enter a name.', placeholder='MyURLs')    
        if bool(excel_file_name):
            data_to_export = feature.export_excel(df_to_export)
            st.download_button(
                label="Export .xlsx",
                data=data_to_export,
                file_name=f'{excel_file_name}.xlsx'
            )