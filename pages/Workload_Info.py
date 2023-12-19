import streamlit as st
import frontend.styling as css
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

st.set_page_config(page_title="AgoraOps | Workload",
                       page_icon="🧊")
css.hide_streamlit_defualt_menu_footer()


st.info("Sit tight, this page will be live soon.",icon='😀')

uri = "mongodb+srv://agoraops:ylLRaVhJuw0LmNNF@cluster0.av42zfn.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri,tls=True,tlsAllowInvalidCertificates=True,server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    #Get a database
    db = client.gtm_trading
    # List all collections on DB
    collections = db.list_collection_names()
    print(collections)
    collection  = client.gtm_trading.jiras
    cursor = collection.find()
    for c in cursor:
        print(c)
        st.write(c)
except Exception as e:
    print(e)

