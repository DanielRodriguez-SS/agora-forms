import streamlit as st
import frontend.styling as css

st.set_page_config(page_title="Tools|ForDesigners",
                       page_icon="🧊")
css.hide_streamlit_defualt_menu_footer()

# Only for 800X800 Images
REPO_1 = "https://www.telstra.com.au/content/dam/tcom/lego/2022/accessories/products/"
# Other Images Sizes
REPO_2 = "https://www.telstra.com.au/content/dam/tcom/devices/general/hardware/"

category = st.text_input('Category', placeholder='earbuds')
sub_category = st.text_input('Sub-Category', placeholder='ghdwerb-saptw')
color = st.text_input('Color', placeholder='black')


if category and sub_category and color:
    files = st.file_uploader('Slect all images', accept_multiple_files=True)
    for file in files:
        if '800x800' in file.name:
            st.write(f'{REPO_1}{category}/{sub_category}/{color}{file.name}')
        else:
            st.write(f'{REPO_2}{category}/{sub_category}/{color}{file.name}')
