from dataclasses import dataclass

@dataclass
class PublicAPIs:
    PREPAID_MOBILE:str = 'https://tapi.telstra.com/presentation/v1/ecommerce-products/products/mobility/PREPAID/PREPAID_MOBILE/NEW'
    PREPAID_MBB:str = 'https://tapi.telstra.com/presentation/v1/ecommerce-products/products/mobility/PREPAID/PREPAID_MBB/NEW'
    PREPAID_TABLET:str = 'https://tapi.telstra.com/presentation/v1/ecommerce-products/products/mobility/PREPAID/PREPAID_TABLET/NEW'
    BOOST:str = 'https://tapi.telstra.com/presentation/v1/ecommerce-products/products/mobility/BOOST/BOOST/NEW'
    #REWARDS_CONSUMER:str = 'https://tapi.telstra.com/presentation/v1/ecommerce-products/products/loyalty_con'
    #REWARDS_DAVINCI:str = 'https://tapi.telstra.com/presentation/v1/ecommerce-products/products/loyalty_con_dv'
    #REWARDS_SMB:str = 'https://tapi.telstra.com/presentation/v1/ecommerce-products/products/loyalty_smb'