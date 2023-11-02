import streamlit as st
import frontend.styling as css
import pandas as pd
import features.f_designers as feature

st.set_page_config(page_title="Tools | For Ops",
                       page_icon="🧊",layout="wide")
css.hide_streamlit_defualt_menu_footer()

st.markdown("<h1>🎛️ File Merger for Porduct Creation</h1>",unsafe_allow_html=True)

uploader_1, uploader_2 = st.columns(2)    
with uploader_1:
    dv_file = st.file_uploader("Choose a DV File")
with uploader_2:
    trading_file = st.file_uploader("Choose a Trading File")

if dv_file:
    if st.button("Merge"):
        # Get Excel into a DataFrame
        df_dv = pd.read_excel(dv_file)
        # Drop all Rows with None Value
        df_dv = df_dv.dropna()
        # Filer DataFrame by Columns
        df_dv:pd.DataFrame = df_dv.get(['SKU','Size','Url'])
        # Filter DataFrame by Values on Column
        df_for_accessories:pd.DataFrame = df_dv.loc[(df_dv['Size'].str.contains('800x800'))]
        df_for_accessories = df_for_accessories.reset_index(drop=True)
        st.write(df_for_accessories)
        # Dictionary for new excel file creation
        product_dict = {
            'SKU':[],
            'Family':[],
            'Brand':[],
            'Category':[],
            'Name':[],
            'Image URL':[],
            'Launch Date':[],
            'End Date':[],
            'Shipping':[],
            'Features':[],
            'Specs':[],
            'Details':[],
            'Image1':[],
            'Image2':[],
            'Image3':[],
            'Image4':[],
            'Image5':[],
            'Attributes':[],
            'Category':[],
            'Stock':[],
            'RRP':[],
            'RO Accs':[],
            'Price Accs':[],
            'RO Loy':[],
            'Price Loy':[]
        }
        # Create a Dictionary 'SKU':[Images]
        sku_images= {}
        # Create a Key for Each SKU and append images into a list
        for index, row in df_for_accessories.iterrows():
            # Make sure sku is a str
            sku = str(int(row['SKU']))
            # If Key does not exist yet, create it and assign it to list to storage images
            if sku_images.get(sku) == None:
                # Creates the key for sku
                sku_images[sku] = []
                # Append first image into list
                sku_images[sku].append(row['Url'])
            else:
                # Append the rest if the images into the same sku key
                sku_images[sku].append(row['Url'])


            # if sku not in product_dict['SKU']:
            #     product_dict['SKU'].append(sku)
            #     product_dict["Image URL"].append(row['Url'])
            #     images_temp.append(row['Url'])
            # else:
            #     images_temp.append(row['Url'])
        st.write(sku_images)

        for key in sku_images:
            st.write(key)
            st.write(len(sku_images[key]))
            product_dict['SKU'].append(key)
            product_dict['Family'].append("")
            product_dict['Brand'].append("")
            product_dict['Category'].append("")
            product_dict['Name'].append("")
            try:
                product_dict['Image URL'].append(sku_images[key][0])
                product_dict['Image1'].append(sku_images[key][0])
            except:
                product_dict['Image URL'].append('')
                product_dict['Image1'].append('')
            product_dict['Launch Date'].append("")
            product_dict['End Date'].append("")
            product_dict['Shipping'].append("")
            product_dict['Features'].append("")
            product_dict['Specs'].append("")
            product_dict['Details'].append("")
            try:
                product_dict['Image2'].append(sku_images[key][1])
            except:
                product_dict['Image2'].append('')

            try:
                product_dict['Image3'].append(sku_images[key][2])
            except:
                product_dict['Image3'].append('')

            try:
                product_dict['Image4'].append(sku_images[key][4])
            except:
                product_dict['Image4'].append('')
            try:
                product_dict['Image5'].append(sku_images[key][5])
            except:
                product_dict['Image5'].append('')
            product_dict['Attributes'].append("")
            product_dict['Stock'].append("")
            product_dict['RRP'].append("")
            product_dict['RO Accs'].append("")
            product_dict['Price Accs'].append("")
            product_dict['RO Loy'].append("")
            product_dict['Price Loy'].append("")

        st.write(product_dict)
        df_to_export = pd.DataFrame.from_dict(product_dict)
        data_to_export = feature.export_excel(df_to_export)
        st.download_button(
            label="Export .xlsx",
            data=data_to_export,
            file_name=f'Product_Launch.xlsx'
                )