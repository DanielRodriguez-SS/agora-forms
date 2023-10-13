import streamlit as st
import io
import pandas as pd
import streamlit.components.v1 as components

def add_product_images(temp_images_data):
    st.session_state.images_data.append(temp_images_data)
    st.session_state.file_uploader_key +=1
    
def delete_product(item):
    st.session_state.images_data.pop(item)

def open_urls(item):
    urls = st.session_state.images_data[item]['Url']
    st.write(urls)
    for url in urls:
         if url != '':
             components.html(f'''<script>window.open("{url}", "_blank");</script>''')
             
@st.cache_data
def export_excel(dataFrame:pd.DataFrame) -> bytes:
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
        dataFrame.to_excel(writer, index=False)
    return buffer.getvalue()

