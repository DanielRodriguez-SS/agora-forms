import requests
from shop_ulrs import PublicAPIs
import json
import asyncio
import streamlit as st
from dataclasses import asdict

session = requests.Session()

def save_json(response:requests.Response, file_path:str) -> None:
    json_obj = json.dumps(response, indent=4)
    with open(f'{file_path}.json', 'w') as file:
        file.write(json_obj)

def fetch(session:requests, url:str) -> requests.Response:
    try:
        result = session.get(url)
        return result.json()
    except Exception as e:
        print(e)
        return None

def get_products_from_shop(shop_url:str, shop_name:str) -> dict[str,list]:
    response = fetch(session, url=shop_url)
    product_families =  response['data']['deviceFamilies']
    devices = []
    if shop_name == 'PREPAID_MOBILE':
        handsets = []
        simsKits = []
        rechargeKits = []
        for family in product_families:
            products = family['devices']
            for product in products:
                if family['name'] == "Prepaid Recharge":
                    rechargeKits.append(f"{product['code']} - {product['name']}")
                elif family['name'] == "SIM KIT":
                    simsKits.append(f"{product['code']} - {product['name']}")
                else:
                    handsets.append(f"{product['code']} - {product['name']}")

        return {"PREPAID_MOBILE":handsets, "PREPAID_SIMs":simsKits, "PREPAID_RECHARGE":rechargeKits}
    else:
        for family in product_families:
            products = family['devices']
            for product in products:
                devices.append(f"{product['code']} - {product['name']}")
        return {shop_name:devices}

async def async_get_products_from_shop(shop_url,shop_name):
    return await asyncio.to_thread(get_products_from_shop,shop_url,shop_name)

async def gather_tasks():
    tasks = []
    shops = asdict(PublicAPIs())
    for key in shops:
        tasks.append(asyncio.create_task(async_get_products_from_shop(shops[key],key)))
    return await asyncio.gather(*tasks)    


@st.cache_data(show_spinner=False,ttl=3600)
def collect_products_from_shopAPIs() -> dict:
    
    results_dicts = asyncio.run(gather_tasks())
    
    #####################################
    # shops = asdict(PublicAPIs())
    # results_dicts = []
    # for key in shops:
    #     results_dicts.append(get_products_from_shop(shops[key],key))
    ###################################
    
    pack_dict = {}
    for dict in results_dicts:
        pack_dict.update(dict)
    return pack_dict



def split_categories_from_mobile() -> dict:
    mobile = collect_products_from_shopAPIs()
    return mobile


# if "__main__" == __name__:
#    print(split_categories_from_mobile())