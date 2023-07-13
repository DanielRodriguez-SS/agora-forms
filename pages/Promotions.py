import streamlit as st
import frontend.styling as css
from shop_map import tree
from dataclasses import dataclass
from pdf_builder import generate_pdf_file
import datetime

@dataclass
class ProductInfo:
    shop:str = '_NA'
    segments:str = '_NA'
    device_type:str = '_NA'
    plans:str = '_NA'
    products:str = '_NA'

@dataclass
class PromoDetails:
    type:str = '_NA'
    code:str = '_NA'
    apply:str = '_NA'
    elegibility:str = '_NA'
    name:str = '_NA'
    credit:str = '_NA'
    recurring:str = '_NA'
    start_date:str = '_NA'
    start_time:str = '_NA'
    end_date:str = '_NA'
    end_time:str = '_NA'
    email_coms:str = '_NA'

st.set_page_config(page_title="Forms | Promotions",
                       page_icon="🧊")

css.hide_streamlit_defualt_menu_footer()
st.markdown("<h1>Tell us more about your promotion</h1>",unsafe_allow_html=True)
st.markdown("""<div style="background-color:rgb(239,48,57);height:1.5rem;width:1.5rem;border-radius:50%;text-align:center;margin-bottom:.5rem;margin-top:.5rem;">1</div>""", unsafe_allow_html=True)

with st.spinner('Searching for available products in AGORA'):
    shops = list(tree.keys())

product_info = ProductInfo()
with st.expander("Product Information"):
    shop = st.selectbox("Shop:",shops)
    product_info.shop = shop
    #st.write(tree[shop])
    segments = tree[shop]['Segment']
    device_types:dict = tree[shop]['Device Type']
    customer_types = tree[shop]['Customer Type']
    if segments:
        segment = st.multiselect("Choose a segment:",segments)
        product_info.segments = segment
    if device_types:
        device_type_options = list(device_types.keys())
        device_type = st.selectbox('Devices Type:',device_type_options)
        product_info.device_type = device_type
        plan_options = tree[shop]['Device Type'][device_type]['plans']
        product_options = tree[shop]['Device Type'][device_type]['products']
        tcom_link = tree[shop]['Device Type'][device_type]['entry_point']
        if plan_options:
            plan = st.multiselect('On Plans:',plan_options, help=tcom_link)
            product_info.plans = plan
            
            # if product_options:
            #     apply_to_all = st.radio('Looking for specific product?',['No','Yes'])
            #     if apply_to_all == 'Yes':
            #         products = st.multiselect('Products:',product_options)
            #         product_info.products = products
            
            
            apply_to_all = st.radio('Looking for specific product?',['No','Yes'])
            if apply_to_all == 'Yes':
                products = st.text_input('Products',placeholder="Please type product names separated by a ','. ")
                #products = st.multiselect('Products:',product_options)
                product_info.products = products

        else:
            if product_options:
                products = st.multiselect('Products:',product_options)
                product_info.products = products

promo_details = PromoDetails()

st.markdown("""<div style="background-color:rgb(239,48,57);height:1.5rem;width:1.5rem;border-radius:50%;text-align:center;margin-bottom:.5rem;margin-top:.5rem;">2</div>""", unsafe_allow_html=True)
with st.expander("Promotion Details"):
    promotion_type = st.radio("Promotion Type:",['ATL','BTL'])
    promo_details.type = promotion_type
    if promotion_type == 'BTL':
        promo_code = st.text_input('Code:',placeholder='e.g. DOLLARS1X250')
        promo_details.code = promo_code
    apply_by = st.selectbox('Apply by:',['BoH','Auto','Base+'])
    promo_details.apply = apply_by

    if customer_types:
        eligibility = st.multiselect('Customer Type:',customer_types)
        promo_details.elegibility = eligibility
    dysplay_name = st.text_input('Dislay Name:',placeholder='e.g. $200 off your bill.')
    promo_details.name = dysplay_name
    credits = st.number_input('Credit Amount (AUD) :',min_value=0)
    promo_details.credit = f'{credits} AUD'
    if shop == 'Pospaid' and apply_to_all == 'No':
        if plan_options:
            recurring = st.radio('Is this a reccuring discount?',['No','Yes'])

            if recurring == 'Yes':
                recurring_period = st.number_input('Discount Period (mths):',min_value=0)
                promo_details.recurring = recurring_period
                
    if 'Fixed' in shop:
        if plan_options:
            recurring = st.radio('Is this a reccuring discount?',['No','Yes'])
            if recurring == 'Yes':
                recurring_period = st.number_input('Discount Period (mths):',min_value=0)
                promo_details.recurring = f'{recurring_period} mths'
    
    col_start, col_end = st.columns(2)
    with col_start:
        start_date = st.date_input('Start Date:')
        start_time = st.time_input('Start Time:',datetime.time(), step=60)
    with col_end:
        end_date = st.date_input('End Date:')
        end_time = st.time_input('End Time:', datetime.time(23,59), step=60)
    
    promo_details.start_date = str(start_date)
    promo_details.start_time = str(start_time)
    promo_details.end_date = str(end_date)
    promo_details.end_time = str(end_time)

    if 'Fixed' not in shop:
        add_emial_noty = st.radio('Add text to email notification?',['No','Yes'])
        if add_emial_noty == 'Yes':
            email_noty = st.text_area("This text will be added on the email confirmation sent to customers",placeholder='e.g. Get $250 off your bill on Samsung S21+5G.')
            promo_details.email_coms = email_noty

st.markdown("""<div style="background-color:rgb(239,48,57);height:1.5rem;width:1.5rem;border-radius:50%;text-align:center;margin-bottom:.5rem;margin-top:.5rem;">3</div>""", unsafe_allow_html=True)
pdf_file_name = st.text_input('File name:',placeholder='Agora Promo')
col_save, col_download = st.columns(2)
with col_save:
    
    save_button = st.button("Save")
with col_download:
    if save_button: 
        if bool(pdf_file_name):
            pdf = generate_pdf_file(product_info,promo_details)
            st.download_button(
                 label="Export PDF",
                 data=pdf,
                 file_name=f'{pdf_file_name}.pdf',
                 mime='application/octet-stream',
             )
        else:
            st.error('Plese provide a name for the PDF file', icon="🚨")