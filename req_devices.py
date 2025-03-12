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
    launch_status:str = '_NA'
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

with st.spinner('Searching for available products in AGORA'):
    shops = list(tree.keys())

st.write("# Tell us more about this new product")

# Divide layout in two, left and right
layout_left, layout_right = st.columns([0.4, 0.6])

# Title to left side
layout_left.write("## Details")

layout_right.write("## Products")

launch_details = LaunchDetails()

# Select boxes for "Shop and Device Type"
shop_col1, device_col2 = layout_left.columns(2)
shop = shop_col1.selectbox("Shop:",shops)
device_types:dict = tree[shop]['Device Type']
device_type = device_col2.selectbox("Device Type:", device_types)

# Select boxes for "Launch Date and Launch Time"
launchD_col1, launchT_col2, launchS_col3 = layout_left.columns(3)
launch_date = launchD_col1.date_input('Lauch Date:', format='DD/MM/YYYY')
launch_details.launch_date = launch_date

lauch_time = launchT_col2.time_input('Lauch Time:',datetime.time(), step=60)
launch_details.launch_time = lauch_time

# Provide more initial status for Rewards store
if device_type == 'Mobiles & Plans':
    lauch_status = launchS_col3.selectbox("Status:", ['In Stock', 'Pre Order'])
    
else:
    lauch_status = launchS_col3.selectbox("Status:", ['In Stock'], disabled=True)
launch_details.launch_status = lauch_status

# Text input box for "Stock Notice"
if lauch_status == 'In Stock':
    stock_notice = layout_left.text_area('Stock Notice:',placeholder="Available Now.")
else:
    stock_notice = layout_left.text_area('Stock Notice:',placeholder="Pre-Order Now. Available from next week.")
launch_details.stock_notice = stock_notice

# Text boxes for "Brand and Device name"
brand_col1, deviceN_col2 = layout_left.columns(2)
device_brand = brand_col1.text_input("Brand:", placeholder=device_types[device_type]['placeholder_brand'])
device_name = deviceN_col2.text_input("Device name:", placeholder=device_types[device_type]['placeholder_name'])


if device_type == "Handsets" or device_type == "Tablet" or device_type == 'Mbb':
    # Select Boxes for "Size Color SKU Price"
    size_col1, color_col2, sku_col3, price_col4 = layout_left.columns(4)
    device_size = size_col1.selectbox("Size:", ['NA', '64GB', '128GB', '256GB', '512GB', '1TB', '2TB'])
    device_color = color_col2.text_input("Color:", placeholder='Deep Blue')
    device_sku = sku_col3.text_input("SKU:", placeholder='10002543..')
    device_price = price_col4.number_input("Price (AUD):")

    layout_left.button(
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

elif device_type == "Mobiles & Plans":
    device_size = "NA"
    device_color = "NA"
    device_sku = "NA"
    device_price = "NA"
    
    # Select Boxes for "Storage and Colors"
    colors_col1, storage_col2 = layout_left.columns(2)
    device_colors_num = colors_col1.number_input("Colors:", min_value=1)
    colors_options = [f'Color {color_index+1}' for color_index in range(device_colors_num)]
    color_tabs = layout_left.tabs(colors_options)
    colors_options_data = {}
    
    for index,color in enumerate(colors_options):
        images_urls = []
        columns = color_tabs[index].columns([0.5, 0.5])
        colors_options_data[index] = {"name":columns[0].text_input(f"Name {index+1}", key=f'name{color}{index}0', placeholder="Deep Blue")}
        colors_options_data[index].update({"hex":columns[1].color_picker(f'HEX {index+1}', key=f'hex{color}{index}0')})
        images_urls.append(color_tabs[index].text_input(f"Image URL 1", key=f'image{color}{index}0', placeholder=f"https://www.telstra.com.au/content/{color}"))
        images_urls.append(color_tabs[index].text_input(f"Image URL 2", key=f'image{color}{index}1', placeholder=f"https://www.telstra.com.au/content/{color}"))
        images_urls.append(color_tabs[index].text_input(f"Image URL 3", key=f'image{color}{index}2', placeholder=f"https://www.telstra.com.au/content/{color}"))
        images_urls.append(color_tabs[index].text_input(f"Image URL 4", key=f'image{color}{index}3', placeholder=f"https://www.telstra.com.au/content/{color}"))
        images_urls.append(color_tabs[index].text_input(f"Image URL 5", key=f'image{color}{index}4', placeholder=f"https://www.telstra.com.au/content/{color}"))

        colors_options_data[index].update({"images":images_urls})
    #layout_right.write(colors_options_data)

    
    layout_left.write('Sizes:')
    size_rpp_list = []
    sizeOp_col1, sizeOp_col2 = layout_left.columns(2)
    
    size64 = sizeOp_col1.checkbox('64GB')
    if size64:
        rpp64 = sizeOp_col1.number_input(f'RPP (AUD)', key='64GB',  min_value=1)
        if rpp64:
            size_rpp_list.append(['64GB',rpp64])

    size128 = sizeOp_col1.checkbox('128GB')
    if size128:
        rpp128 = sizeOp_col1.number_input(f'RPP (AUD)', key='128GB', min_value=1)
        if rpp128:
            size_rpp_list.append(['128GB',rpp128])

    size256 = sizeOp_col1.checkbox('256GB')
    if size256:
        rpp256 = sizeOp_col1.number_input(f'RPP (AUD)', key='256GB', min_value=1)
        if rpp256:
            size_rpp_list.append(['256GB',rpp256])
    
    size512 = sizeOp_col2.checkbox('512GB')
    if size512:
        rpp512 = sizeOp_col2.number_input(f'RPP (AUD)', key='512GB', min_value=1)
        if rpp512:
            size_rpp_list.append(['512GB',rpp512])

    size1T = sizeOp_col2.checkbox('1TB')
    if size1T:
        rpp1T = sizeOp_col2.number_input(f'RPP (AUD)', key='1TB', min_value=1)
        if rpp1T:
            size_rpp_list.append(['1TB',rpp1T])
    
    size2T = sizeOp_col2.checkbox('2TB')
    if size2T:
        rpp2T = sizeOp_col2.number_input(f'RPP (AUD)', key='2TB', min_value=1)
        if rpp2T:
            size_rpp_list.append(['2TB',rpp2T])
    
    #layout_right.write(size_rpp_list)
    #layout_right.write(colors_options)
    colors_filled = 0
    for option in colors_options_data:
        if colors_options_data[option]['name']:
            colors_filled = colors_filled + 1
            #layout_right.write('Empty')
        #if len(colors_options[option]) == 3:
            #layout_right.write('complete')
            # colors_filled = colors_filled + 1
    #layout_right.write(colors_filled)
    if (colors_filled == device_colors_num) and size_rpp_list:
        
        layout_right.write(f'### {device_brand} {device_name}')
        rewards_product_data = {}
        rewards_product_data["Sku"] = []
        rewards_product_data["Family"] = []
        rewards_product_data["Brand"] = []
        rewards_product_data["Category"] = []
        rewards_product_data["Type"] = []
        rewards_product_data["Image URL"] = []
        rewards_product_data["Name"] = []
        rewards_product_data["Launch Date"] = []
        rewards_product_data["End Date"] = []
        rewards_product_data["Shipping"] = []
        rewards_product_data["Features"] = []
        rewards_product_data["Specs"] = []
        rewards_product_data["Details"] = []
        rewards_product_data["Image1"] = []
        rewards_product_data["Image2"] = []
        rewards_product_data["Image3"] = []
        rewards_product_data["Image4"] = []
        rewards_product_data["Image5"] = []
        rewards_product_data["Attributes"] = []
        rewards_product_data["Category2"] = []
        rewards_product_data["Stock"] = []
        rewards_product_data["RPP"] = []
        rewards_product_data["RO Accs"] = []
        rewards_product_data["Price Accs"] = []
        rewards_product_data["RO Loy"] = []
        rewards_product_data["Price Loy"] = []
        #rewards_product_data["Storage"] = []
        
        #rewards_product_data["Color"] = []

        #layout_right.write(size_rpp_list)
        for size_rpp in size_rpp_list:
            for color in colors_options_data:
                rewards_product_data["Sku"].append("")
                rewards_product_data["Family"].append(device_name)
                rewards_product_data["Brand"].append(device_brand)
                rewards_product_data["Category"].append(device_type)
                rewards_product_data["Type"].append('Product')
                rewards_product_data["Image URL"].append(colors_options_data[0]["images"][0])
                rewards_product_data["Name"].append(f"{device_name} {size_rpp[0]} {colors_options_data[color]["name"]}")
                rewards_product_data["Launch Date"].append(f"{launch_date} {lauch_time}")
                rewards_product_data["End Date"].append(f"{launch_date.replace(year=launch_date.year + 10)} {lauch_time}")
                rewards_product_data["Shipping"].append("")
                rewards_product_data["Features"].append("")
                rewards_product_data["Specs"].append("")
                rewards_product_data["Details"].append("")
                if colors_options_data[color]["images"][0]:
                    rewards_product_data["Image1"].append(colors_options_data[color]["images"][0])
                else:
                    rewards_product_data["Image1"].append("")
                if colors_options_data[color]["images"][1]:
                    rewards_product_data["Image2"].append(colors_options_data[color]["images"][1])
                else:
                    rewards_product_data["Image2"].append("")
                if colors_options_data[color]["images"][2]:
                    rewards_product_data["Image3"].append(colors_options_data[color]["images"][2])
                else:
                    rewards_product_data["Image3"].append("")
                
                if colors_options_data[color]["images"][2]:
                    rewards_product_data["Image4"].append(colors_options_data[color]["images"][3])
                else:
                    rewards_product_data["Image4"].append("")

                if colors_options_data[color]["images"][2]:
                    rewards_product_data["Image5"].append(colors_options_data[color]["images"][4])
                else:
                    rewards_product_data["Image5"].append("")

                #rewards_product_data["Storage"].append(size_rpp[0])
                rewards_product_data["Attributes"].append(f"Colour:{colors_options_data[color]["name"]},Memory:{size_rpp[0]},ColourImage:{colors_options_data[color]["name"]} | {colors_options_data[color]["hex"]}")
                rewards_product_data["Category2"].append('Mobiles & Accessories')
                rewards_product_data["Stock"].append("")
                rewards_product_data["RPP"].append(size_rpp[1])
                rewards_product_data["RO Accs"].append("No")
                rewards_product_data["Price Accs"].append("Yes")
                rewards_product_data["RO Loy"].append("No")
                rewards_product_data["Price Loy"].append("Yes")

                #rewards_product_data["Color"].append(colors_options_data[color]["name"])
        
        #layout_right.write(rewards_product_data)
        df_edited = layout_right.data_editor(pd.DataFrame(rewards_product_data),use_container_width=True, hide_index=True)
        if not (df_edited['Sku'] == '').any():
            file_name_col1, button_export_col2, button_export_col3 = layout_right.columns(3, vertical_alignment='bottom')
            export_file_name_rewards = file_name_col1.text_input("File name:", placeholder='Rewards Launch')
            if export_file_name_rewards:
                rewards_pdf = export_new_products(df_edited[["Sku", "Brand", "Name", "RPP"]], launch_details)
                button_export_col2.download_button(

                    label="Export PDF",
                    data=rewards_pdf,
                    file_name=f'{export_file_name_rewards}.pdf',
                    mime='application/octet-stream',
                    icon=":material/download:",
                )
                button_export_col3.download_button(
                    label="Export CSV",
                    data=df_edited.to_csv().encode("utf-8"),
                    file_name=f'{export_file_name_rewards}.csv',
                    mime="text/csv",
                    icon=":material/download:"
                )

            #layout_right.write(df_edited['Sku'])

else:
    device_size = "NA"
    device_color = "NA"
    # Select boxes for "Sku and Price"
    sku_col1, price_col2 = layout_left.columns(2)
    device_sku = sku_col1.text_input("SKU:", placeholder='10002543..')
    device_price = price_col2.number_input("Price (AUD):")

    layout_left.button(
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
    layout_right.write("## Products")
    layout_right.text("Export to file:")
    layout_right.data_editor(pd.DataFrame(st.session_state.product_data),use_container_width=True, hide_index=True)
    row12_col1, row12_col2 = layout_right.columns(2, vertical_alignment='bottom')
    export_file_name = row12_col1.text_input("File name:", placeholder='Prepaid Launch')
    if export_file_name:
        pdf = export_new_products(pd.DataFrame(st.session_state.product_data), launch_details)

        row12_col2.download_button(
                 label="Export PDF",
                 data=pdf,
                 file_name=f'{export_file_name}.pdf',
                 mime='application/octet-stream',
             )