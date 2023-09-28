import streamlit as st
import frontend.styling as css

st.set_page_config(page_title="Tools | ForDesigners",
                       page_icon="🧊",layout="wide")
css.hide_streamlit_defualt_menu_footer()

# Only for 800X800 Images
REPO_1 = "https://www.telstra.com.au/content/dam/tcom/lego/2022/accessories/products/"
# Other Images Sizes
REPO_2 = "https://www.telstra.com.au/content/dam/tcom/devices/general/hardware/"

product_name = st.text_input('Product Name', placeholder='Sprout-AudioPlus TWS Earbuds-Black')
category = st.text_input('Category', placeholder='earbuds')
sub_category = st.text_input('Sub-Category', placeholder='ghdwerb-saptw')
color = st.text_input('Color', placeholder='black')
hex_code = st.text_input('Hexcode', placeholder='#000000')

a = 0
image_data_800x800 = {
    "Name":[],
    "Size":[],
    "Hex Color":[],
    "Url":[]
}
image_data_900x1200 = {
    "Name":[],
    "Size":[],
    "Hex Color":[],
    "Url":[]
}
image_data_1200x900 = {
    "Name":[],
    "Size":[],
    "Hex Color":[],
    "Url":[]
}
products_images = []
if 'images_data' not in st.session_state:
    st.session_state.images_data = []

def add_product_images(temp_images_data):
    st.session_state.images_data.append(temp_images_data)

def delete_product(item):
    st.session_state.images_data.pop(item)



if product_name and category and sub_category and color and hex_code:
    files = st.file_uploader('Slect all images', accept_multiple_files=True)
    if files:

        for file in files:
            if '800x800' in file.name:
                image_data_800x800['Name'].append(product_name)
                image_data_800x800['Size'].append('800x800')
                image_data_800x800['Hex Color'].append(hex_code)
                image_data_800x800['Url'].append(f'{REPO_1}{category}/{sub_category}/{color}{file.name}')

            elif 'landscape' not in file.name:
                image_data_900x1200['Name'].append(product_name)
                image_data_900x1200['Size'].append('900x1200')
                image_data_900x1200['Hex Color'].append(hex_code)
                image_data_900x1200['Url'].append(f'{REPO_1}{category}/{sub_category}/{color}{file.name}')

            else:
                image_data_1200x900['Name'].append(product_name)
                image_data_1200x900['Size'].append('1200x900')
                image_data_1200x900['Hex Color'].append(hex_code)
                image_data_1200x900['Url'].append(f'{REPO_1}{category}/{sub_category}/{color}{file.name}')

        temp_image_data = {
            "Name":image_data_800x800['Name']+image_data_900x1200['Name']+image_data_1200x900['Name'],
            "Size":image_data_800x800['Size']+image_data_900x1200['Size']+image_data_1200x900['Size'],
            'Hex Color': image_data_800x800['Hex Color']+image_data_900x1200['Hex Color']+image_data_1200x900['Hex Color'],
            'Url': image_data_800x800['Url']+image_data_900x1200['Url']+image_data_1200x900['Url']
        }
        save = st.button('Save', on_click=add_product_images, args=[temp_image_data])
#st.write(st.session_state.images_data)
number_of_products_saved = len(st.session_state.images_data)
st.write(f'Products Saved: {number_of_products_saved}')

for item in range(number_of_products_saved):
    st.write(st.session_state.images_data[item]["Name"][0])
    st.button('Delete',key=item, on_click=delete_product, args=[item])