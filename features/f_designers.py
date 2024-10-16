import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
import data.d_designers as data
from PIL import Image
from io import BytesIO
import zipfile
import os

# FEATURES FOR IMAGE URLs BUILDER TAB
def process_images_names_for_acc_tplus(files:list,product_sku,product_name,category,sub_category,color,hex_code)->dict:
    image_data_800x800 = {
    "Size":[],
    "SKU":[],
    "Category":[],
    "EPC Code":[],
    "Name":[],
    "Color":[],
    "Hex Color":[],
    "Url":[]
    }
    image_data_900x1200 = {
    "Size":[],
    "SKU":[],
    "Category":[],
    "EPC Code":[],
    "Name":[],
    "Color":[],
    "Hex Color":[],
    "Url":[]
    }
    image_data_1200x900 = {
    "Size":[],
    "SKU":[],
    "Category":[],
    "EPC Code":[],
    "Name":[],
    "Color":[],
    "Hex Color":[],
    "Url":[]
    }
    for file in files:
        if '800x800' in file.name:
            image_data_800x800['Size'].append('800x800')
            image_data_800x800['SKU'].append(product_sku)
            image_data_800x800['Category'].append(category)
            image_data_800x800['EPC Code'].append(sub_category)
            image_data_800x800['Name'].append(product_name)
            image_data_800x800['Color'].append(color)
            image_data_800x800['Hex Color'].append(hex_code)
            image_data_800x800['Url'].append(f'{data.REPO_1}{category}/{sub_category}/{color}/{file.name}')
        elif 'landscape' not in file.name:
            image_data_900x1200['Size'].append('900x1200')
            image_data_900x1200['SKU'].append(product_sku)
            image_data_900x1200['Category'].append(category)
            image_data_900x1200['EPC Code'].append(sub_category)
            image_data_900x1200['Name'].append(product_name)
            image_data_900x1200['Color'].append(color)
            image_data_900x1200['Hex Color'].append(hex_code)
            image_data_900x1200['Url'].append(f'{data.REPO_2}{category}/{sub_category}/{color}/{file.name}')
        else:
            image_data_1200x900['Size'].append('1200x900')
            image_data_1200x900['SKU'].append(product_sku)
            image_data_1200x900['Category'].append(category)
            image_data_1200x900['EPC Code'].append(sub_category)
            image_data_1200x900['Name'].append(product_name)
            image_data_1200x900['Color'].append(color)
            image_data_1200x900['Hex Color'].append(hex_code)
            image_data_1200x900['Url'].append(f'{data.REPO_2}{category}/{sub_category}/{color}/{file.name}')
    temp_image_data = {
        "Size":['']+image_data_800x800['Size']+image_data_900x1200['Size']+image_data_1200x900['Size'],
        "SKU":['']+image_data_800x800['SKU']+image_data_900x1200['SKU']+image_data_1200x900['SKU'],
        "Category":['']+image_data_800x800['Category']+image_data_900x1200['Category']+image_data_1200x900['Category'],
        "EPC Code":['']+image_data_800x800['EPC Code']+image_data_900x1200['EPC Code']+image_data_1200x900['EPC Code'],
        "Name":['']+image_data_800x800['Name']+image_data_900x1200['Name']+image_data_1200x900['Name'],
        "Color":['']+image_data_800x800['Color']+image_data_900x1200['Color']+image_data_1200x900['Color'],
        'Hex Color':['']+image_data_800x800['Hex Color']+image_data_900x1200['Hex Color']+image_data_1200x900['Hex Color'],
        'Url':['']+image_data_800x800['Url']+image_data_900x1200['Url']+image_data_1200x900['Url']
    }
    return temp_image_data

def process_images_names_for_mobility(files:list,product_sku,product_name,category,sub_category,color,hex_code)->dict:
    image_data_270x530 = {
    "Size":[],
    "SKU":[],
    "Category":[],
    "EPC Code":[],
    "Name":[],
    "Color":[],
    "Hex Color":[],
    "Url":[]
    }
    image_data_800x800 = {
    "Size":[],
    "SKU":[],
    "Category":[],
    "EPC Code":[],
    "Name":[],
    "Color":[],
    "Hex Color":[],
    "Url":[]
    }
    image_data_900x1200 = {
    "Size":[],
    "SKU":[],
    "Category":[],
    "EPC Code":[],
    "Name":[],
    "Color":[],
    "Hex Color":[],
    "Url":[]
    }
    image_data_1200x900 = {
    "Size":[],
    "SKU":[],
    "Category":[],
    "EPC Code":[],
    "Name":[],
    "Color":[],
    "Hex Color":[],
    "Url":[]
    }
    for file in files:
        if '270x530' in file.name:
            image_data_270x530['Size'].append('270x530')
            image_data_270x530['SKU'].append(product_sku)
            image_data_270x530['Category'].append(category)
            image_data_270x530['EPC Code'].append(sub_category)
            image_data_270x530['Name'].append(product_name)
            image_data_270x530['Color'].append(color)
            image_data_270x530['Hex Color'].append(hex_code)
            image_data_270x530['Url'].append(f'{data.REPO_3}{file.name}')
        elif '800x800' in file.name:
            image_data_800x800['Size'].append('800x800')
            image_data_800x800['SKU'].append(product_sku)
            image_data_800x800['Category'].append(category)
            image_data_800x800['EPC Code'].append(sub_category)
            image_data_800x800['Name'].append(product_name)
            image_data_800x800['Color'].append(color)
            image_data_800x800['Hex Color'].append(hex_code)
            image_data_800x800['Url'].append(f'{data.REPO_3}{file.name}')
        elif 'landscape' not in file.name:
            image_data_900x1200['Size'].append('900x1200')
            image_data_900x1200['SKU'].append(product_sku)
            image_data_900x1200['Category'].append(category)
            image_data_900x1200['EPC Code'].append(sub_category)
            image_data_900x1200['Name'].append(product_name)
            image_data_900x1200['Color'].append(color)
            image_data_900x1200['Hex Color'].append(hex_code)
            image_data_900x1200['Url'].append(f'{data.REPO_4}{category}/{sub_category}/{color}/{file.name}')
        else:
            image_data_1200x900['Size'].append('1200x900')
            image_data_1200x900['SKU'].append(product_sku)
            image_data_1200x900['Category'].append(category)
            image_data_1200x900['EPC Code'].append(sub_category)
            image_data_1200x900['Name'].append(product_name)
            image_data_1200x900['Color'].append(color)
            image_data_1200x900['Hex Color'].append(hex_code)
            image_data_1200x900['Url'].append(f'{data.REPO_4}{category}/{sub_category}/{color}/{file.name}')
    temp_image_data = {
        "Size":['']+image_data_270x530['Size']+image_data_800x800['Size']+image_data_900x1200['Size']+image_data_1200x900['Size'],
        "Category":['']+image_data_270x530['Category']+image_data_800x800['Category']+image_data_900x1200['Category']+image_data_1200x900['Category'],
        "EPC Code":['']+image_data_270x530['EPC Code']+image_data_800x800['EPC Code']+image_data_900x1200['EPC Code']+image_data_1200x900['EPC Code'],
        "SKU":['']+image_data_270x530['SKU']+image_data_800x800['SKU']+image_data_900x1200['SKU']+image_data_1200x900['SKU'],
        "Name":['']+image_data_270x530['Name']+image_data_800x800['Name']+image_data_900x1200['Name']+image_data_1200x900['Name'],
        "Color":['']+image_data_270x530['Color']+image_data_800x800['Color']+image_data_900x1200['Color']+image_data_1200x900['Color'],
        'Hex Color':['']+image_data_270x530['Hex Color']+image_data_800x800['Hex Color']+image_data_900x1200['Hex Color']+image_data_1200x900['Hex Color'],
        'Url':['']+image_data_270x530['Url']+image_data_800x800['Url']+image_data_900x1200['Url']+image_data_1200x900['Url']
    }
    return temp_image_data

def process_images_names_for_prepaid(files:list,product_sku,product_name,category,sub_category,color,hex_code)->dict:
    image_data_270x530 = {
    "Size":[],
    "SKU":[],
    "Category":[],
    "EPC Code":[],
    "Name":[],
    "Color":[],
    "Hex Color":[],
    "Url":[]
    }
    image_data_800x800 = {
    "Size":[],
    "SKU":[],
    "Category":[],
    "EPC Code":[],
    "Name":[],
    "Color":[],
    "Hex Color":[],
    "Url":[]
    }
    image_data_900x1200 = {
    "Size":[],
    "SKU":[],
    "Category":[],
    "EPC Code":[],
    "Name":[],
    "Color":[],
    "Hex Color":[],
    "Url":[]
    }
    image_data_1200x900 = {
    "Size":[],
    "SKU":[],
    "Category":[],
    "EPC Code":[],
    "Name":[],
    "Color":[],
    "Hex Color":[],
    "Url":[]
    }
    for file in files:
        if '270x530' in file.name:
            image_data_270x530['Size'].append('270x530')
            image_data_270x530['SKU'].append(product_sku)
            image_data_270x530['Category'].append(category)
            image_data_270x530['EPC Code'].append(sub_category)
            image_data_270x530['Name'].append(product_name)
            image_data_270x530['Color'].append(color)
            image_data_270x530['Hex Color'].append(hex_code)
            image_data_270x530['Url'].append(f'{data.REPO_3}{file.name}')
        elif '800x800' in file.name:
            image_data_800x800['Size'].append('800x800')
            image_data_800x800['SKU'].append(product_sku)
            image_data_800x800['Category'].append(category)
            image_data_800x800['EPC Code'].append(sub_category)
            image_data_800x800['Name'].append(product_name)
            image_data_800x800['Color'].append(color)
            image_data_800x800['Hex Color'].append(hex_code)
            image_data_800x800['Url'].append(f'{data.REPO_3}{file.name}')
        elif 'landscape' not in file.name:
            image_data_900x1200['Size'].append('900x1200')
            image_data_900x1200['SKU'].append(product_sku)
            image_data_900x1200['Category'].append(category)
            image_data_900x1200['EPC Code'].append(sub_category)
            image_data_900x1200['Name'].append(product_name)
            image_data_900x1200['Color'].append(color)
            image_data_900x1200['Hex Color'].append(hex_code)
            image_data_900x1200['Url'].append(f'{data.REPO_3}{file.name}')
        else:
            image_data_1200x900['Size'].append('1200x900')
            image_data_1200x900['SKU'].append(product_sku)
            image_data_1200x900['Category'].append(category)
            image_data_1200x900['EPC Code'].append(sub_category)
            image_data_1200x900['Name'].append(product_name)
            image_data_1200x900['Color'].append(color)
            image_data_1200x900['Hex Color'].append(hex_code)
            image_data_1200x900['Url'].append(f'{data.REPO_3}{file.name}')
    temp_image_data = {
        "Size":['']+image_data_270x530['Size']+image_data_800x800['Size']+image_data_900x1200['Size']+image_data_1200x900['Size'],
        "Category":['']+image_data_270x530['Category']+image_data_800x800['Category']+image_data_900x1200['Category']+image_data_1200x900['Category'],
        "EPC Code":['']+image_data_270x530['EPC Code']+image_data_800x800['EPC Code']+image_data_900x1200['EPC Code']+image_data_1200x900['EPC Code'],
        "SKU":['']+image_data_270x530['SKU']+image_data_800x800['SKU']+image_data_900x1200['SKU']+image_data_1200x900['SKU'],
        "Name":['']+image_data_270x530['Name']+image_data_800x800['Name']+image_data_900x1200['Name']+image_data_1200x900['Name'],
        "Color":['']+image_data_270x530['Color']+image_data_800x800['Color']+image_data_900x1200['Color']+image_data_1200x900['Color'],
        'Hex Color':['']+image_data_270x530['Hex Color']+image_data_800x800['Hex Color']+image_data_900x1200['Hex Color']+image_data_1200x900['Hex Color'],
        'Url':['']+image_data_270x530['Url']+image_data_800x800['Url']+image_data_900x1200['Url']+image_data_1200x900['Url']
    }
    return temp_image_data

def add_product_images(temp_images_data):
    st.session_state.images_data.append(temp_images_data)
    st.session_state.file_uploader_key +=1
    
def delete_product(item):
    st.session_state.images_data.pop(item)

def open_urls(item):
    urls = st.session_state.images_data[item]['Url']
    for url in urls:
         if url != '':
             components.html(f'''<script>window.open("{url}", "_blank");</script>''')
             
@st.cache_data
def export_excel(dataFrame:pd.DataFrame) -> bytes:
    buffer = BytesIO()
    with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
        dataFrame.to_excel(writer, index=False)
    return buffer.getvalue()

# FEATURES FOR IMAGES RESIZING TAB
def images_builder(product_id,original_image, size_options:list)->list:
    # Create a list to save the File names
    file_names = []
    # Get the data on bytes from the file uploader widget
    image_bytes = original_image.getvalue()
    # Get the First Character of the Original File Name
    file_id = original_image.name[0]
    # Convert PNG Image to RGB Image and Set a White Background
    with Image.open(BytesIO(image_bytes)) as img:
        new_img =Image.new('RGB',img.size, (255,255,255))
        new_img.paste(img, (0, 0), img)
    # Repeat Process for all Sizes Selected by User
    for size in size_options:
        # Set Canvas Dimentions where New Image will be Pasted
        canvas_width = size[0]
        canvas_height = size[1]
        # Calculate the aspect ratio
        aspect_ratio = new_img.width / new_img.height
        if canvas_width / canvas_height > aspect_ratio:
            new_width = int(canvas_height * aspect_ratio)
            new_height = canvas_height
        else:
            new_width = canvas_width
            new_height = int(canvas_width / aspect_ratio)
        new_img = new_img.resize((new_width,new_height))
        canvas = Image.new("RGB", (canvas_width, canvas_height), (255, 255, 255))
        # Calculate the position to paste the image on the canvas
        left = (canvas_width - new_width) // 2
        top = (canvas_height - new_height) // 2
        # Paste the original image onto the canvas
        canvas.paste(new_img, (left, top))
        file_name = f'temp/{product_id}-{str(canvas_width)}x{str(canvas_height)}.jpg'
        file_names.append(file_name)
        canvas.save(file_name, format='JPEG')
    return file_names

def clean_temp_files(files_names:list):
    for file in files_names:
        #print(file)
        os.remove(file)

def zip_files(files:list):
    data_file_bytes = BytesIO()
    with zipfile.ZipFile(data_file_bytes, 'w') as zipf:
        for file_name in files:
            zipf.write(file_name)
    clean_temp_files(files)
    return data_file_bytes