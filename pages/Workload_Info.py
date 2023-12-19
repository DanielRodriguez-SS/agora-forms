import streamlit as st
import frontend.styling as css
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

st.set_page_config(page_title="AgoraOps | Workload",
                       page_icon="🧊")
css.hide_streamlit_defualt_menu_footer()


st.info("Sit tight, this page will be live soon.",icon='😀')

url = "mongodb+srv://agoraops:fuhNsg6185rPF3qs@cluster0.av42zfn.mongodb.net/?retryWrites=true&w=majority"

Client = MongoClient(url, server_api=ServerApi('1'))

try:
    Client.admin.command('ping')
    st.write('You are connected to MongoDB')
except Exception as e:
    print(e)

