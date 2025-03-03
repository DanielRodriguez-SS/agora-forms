import streamlit as st
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
"""
References:
https://pymongo.readthedocs.io/en/stable/tutorial.html
"""

def connect_to_db()->MongoClient:
    uri = f"mongodb+srv://{st.secrets["database"]["user"]}:{st.secrets["database"]["password"]}@cluster0.av42zfn.mongodb.net/?retryWrites=true&w=majority"
    #uri = "mongodb+srv://agoraops:ylLRaVhJuw0LmNNF@cluster0.av42zfn.mongodb.net/?retryWrites=true&w=majority"
    # Create a new client and connect to the server
    client = MongoClient(uri,tls=True,tlsAllowInvalidCertificates=True,server_api=ServerApi('1'))
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        # print("Pinged your deployment. You successfully connected to MongoDB!")
        return client
    except Exception as e:
        print(e)

def get_collections_names(client:MongoClient, db:str)->list:
     collections_names = client[db].list_collection_names()
     return collections_names

def insert_jira(client:MongoClient, data:dict):
    jiras_collection = client['gtm_trading']['jiras']
    jiras_collection.insert_one(data)

def find_jira(client:MongoClient, data:dict):
    jiras_collection = client['gtm_trading']['jiras']
    return jiras_collection.find_one(data)