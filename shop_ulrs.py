from dataclasses import dataclass

@dataclass
class PublicAPIs:
    CONSUMER_MOBILE:str = 'https://tapi.telstra.com/presentation/v1/ecommerce-products/products/mobility/CON/POSTPAID_MOBILE/NEW'
    CONSUMER_TABLET:str = 'https://tapi.telstra.com/presentation/v1/ecommerce-products/products/mobility/CON/POSTPAID_TABLET/NEW'
    CONSUMER_MBB:str = 'https://tapi.telstra.com/presentation/v1/ecommerce-products/products/mobility/CON/POSTPAID_MBB/NEW'
    STUDENT_MOBILE:str = 'https://tapi.telstra.com/presentation/v1/ecommerce-products/products/mobility/STUDENT/POSTPAID_MOBILE/NEW'
    SMB_MOBILE:str = 'https://tapi.telstra.com/presentation/v1/ecommerce-products/products/mobility/SMB/POSTPAID_MOBILE/NEW'
    SMB_TABLET:str = 'https://tapi.telstra.com/presentation/v1/ecommerce-products/products/mobility/SMB/POSTPAID_TABLET/NEW'
    SMB_MBB:str = 'https://tapi.telstra.com/presentation/v1/ecommerce-products/products/mobility/SMB/POSTPAID_MBB/NEW'
    PREPAID_MOBILE:str = 'https://tapi.telstra.com/presentation/v1/ecommerce-products/products/mobility/PREPAID/PREPAID_MOBILE/NEW'
    PREPAID_MBB:str = 'https://tapi.telstra.com/presentation/v1/ecommerce-products/products/mobility/PREPAID/PREPAID_MBB/NEW'
    PREPAID_TABLET:str = 'https://tapi.telstra.com/presentation/v1/ecommerce-products/products/mobility/PREPAID/PREPAID_TABLET/NEW'
    BOOST:str = 'https://tapi.telstra.com/presentation/v1/ecommerce-products/products/mobility/BOOST/BOOST/NEW'
    GAMING:str = 'https://tapi.telstra.com/presentation/v1/ecommerce-products/products/mobility/GAMING/POSTPAID_XBOX/NEW'
    #REWARDS_CONSUMER:str = 'https://tapi.telstra.com/presentation/v1/ecommerce-products/products/loyalty_con'
    #REWARDS_DAVINCI:str = 'https://tapi.telstra.com/presentation/v1/ecommerce-products/products/loyalty_con_dv'
    #REWARDS_SMB:str = 'https://tapi.telstra.com/presentation/v1/ecommerce-products/products/loyalty_smb'
    #ACCESSORIES_CONSUMER = 'https://tapi.telstra.com/presentation/v1/ecommerce-products/products/accessories_con'
    #ACCESSORIES_DAVINCI = 'https://tapi.telstra.com/presentation/v1/ecommerce-products/products/accessories_con_dv'