from products_puller import collect_products_from_shopAPIs

tree = {
    'Prepaid': {
        
        'Device Type': {
            'Handsets': {
                'placeholder_brand': 'Samsung',
                'placeholder_name': 'Galaxy A16 4G',
                'entry_point':'',
                'products':collect_products_from_shopAPIs()['PREPAID_MOBILE']
            },
            'Tablet': {
                'placeholder_brand': 'Apple',
                'placeholder_name': 'iPad Air 10Gen',
                'entry_point':'',
                'products':collect_products_from_shopAPIs()['PREPAID_TABLET']
            },
            'Mbb': {
                'placeholder_brand': 'Telstra',
                'placeholder_name': 'Pre-Paid 4GX Wi-Fi Plus 2',
                'entry_point':'',
                'products':collect_products_from_shopAPIs()['PREPAID_MBB']
            },
            'SIMs Kits': {
                'placeholder_brand': 'Telstra',
                'placeholder_name': '$39 Pre-Paid SIM Starter Kit',
                'entry_point':'',
                'products':collect_products_from_shopAPIs()['PREPAID_SIMs']
            },
            'Prepaid Recharge': {
                'placeholder_brand': 'Telstra',
                'placeholder_name': '$69 Pre-Paid Recharge',
                'entry_point':'',
                'products':collect_products_from_shopAPIs()['PREPAID_RECHARGE']
            }
        }
     },
     'Boost': {
         'Device Type': {
             'SIMs': {
                'placeholder_brand': 'Boost',
                'placeholder_name': '$300 Boost Prepaid SIM',
                 'entry_point':'',
                 'products':collect_products_from_shopAPIs()['BOOST']
             }
          }
      },
     'Rewards': {
         'Device Type': {
             'Mobiles & Plans': {
                'placeholder_brand': 'Apple',
                'placeholder_name': 'iPhone 15',
                 'entry_point':'',
                 'products':collect_products_from_shopAPIs()['BOOST']
             }
          }
      }
}