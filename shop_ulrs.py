from dataclasses import dataclass

@dataclass
class PublicAPIs:
    PREPAID_MOBILE:str = 'https://tapi.telstra.com/presentation/v1/ecommerce-products/products/mobility/PREPAID/PREPAID_MOBILE/NEW'
    PREPAID_MBB:str = 'https://tapi.telstra.com/presentation/v1/ecommerce-products/products/mobility/PREPAID/PREPAID_MBB/NEW'
    PREPAID_TABLET:str = 'https://tapi.telstra.com/presentation/v1/ecommerce-products/products/mobility/PREPAID/PREPAID_TABLET/NEW'
    BOOST:str = 'https://tapi.telstra.com/presentation/v1/ecommerce-products/products/mobility/BOOST/BOOST/NEW'