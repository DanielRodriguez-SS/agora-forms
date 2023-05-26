from products_puller import collect_products_from_shopAPIs

tree =  {
            'Pospaid':{
                        'Segment':['Consumer','Small Business'],
                        'Customer Type':['New','Porting','Upgrade'],
                        'Device Type':{
                                        'Mobile':{'entry_point':'',
                                                  'plans':['Basic','Essential','Premium'],
                                                  'products':collect_products_from_shopAPIs()['CONSUMER_MOBILE']
                                                  },
                                        'Tablet':{'entry_point':'',
                                                  'plans':['Small','Medium','Large'],
                                                  'products':collect_products_from_shopAPIs()['CONSUMER_TABLET']
                                                 },                                        
                                        'Mbb':{'entry_point':'',
                                                  'plans':['Small','Medium','Large'],
                                                  'products':collect_products_from_shopAPIs()['CONSUMER_MBB']
                                                }                                        

                                        }
                      },
            'Prepaid':{
                        'Segment':None,
                        'Customer Type':None,
                        'Device Type':{
                                            'Mobile':{'entry_point':'',
                                                  'plans':None,
                                                  'products':collect_products_from_shopAPIs()['PREPAID_MOBILE']
                                                  },
                                            'Tablet':{'entry_point':'',
                                                  'plans':None,
                                                  'products':collect_products_from_shopAPIs()['PREPAID_TABLET']
                                                  },

                                            'Mbb':{'entry_point':'',
                                                  'plans':None,
                                                  'products':collect_products_from_shopAPIs()['PREPAID_MBB']
                                                  }
                        }
                      },
            'Boost':{
                        'Segment':None,
                        'Customer Type':None,
                        'Device Type':{
                                        'SIMs':{'entry_point':'',
                                                'plans':None,
                                                'products':collect_products_from_shopAPIs()['BOOST']
                                                }
                        }
                    },
            'Consumer Fixed Services':{
                            'Segment':None,
                            'Customer Type':['New','Porting','Recontract'],
                            'Device Type':{
                                            'Internet':{'entry_point':'https://www.telstra.com.au/internet/nbn-plans#plans',
                                                        'plans':['Standard - $80','Standard Plus - $95','Premium - $110','Superfast - $140','Ultrafast - $180'],
                                                        'products':['Telstra Smart modem - Professional installation','International Ultimate','Telstra Smart Wi-Fi Booster']
                                            },
                                            '5G':{'entry_point':'https://www.telstra.com.au/internet/5g-home-internet',
                                                  'plans':['5G Home Internet'],
                                                  'products':[]
                                                  },
                                            'Phone Home':{'entry_point':'https://www.telstra.com.au/home-phone',
                                                        'plans':['Ultimate Voice - $55'],
                                                        'products':['International Ultimate']

                                            },
                                            'Foxtel':{'entry_point':'https://www.telstra.com.au/entertainment/tv-movies/foxtel-from-telstra',
                                                            'plans':['Foxtel Plus','Sports HD','Movies HD','Premium','Platinum Plus'],
                                                            'products':['Netflix','Foxtel IQ4 Multiroom']
                                            }
                                          }
                            },
            'Small Business Fixed Services':{
                            'Segment':None,
                            'Customer Type':['New','Porting','Recontract'],
                            'Device Type':{
                                            'Internet':{'entry_point':'https://www.telstra.com.au/small-business/internet/5g-broadband-plans',
                                                        'plans':['Ultimate Business Internet - $110','Ultimate Business Internet Premium - $140','5G Business Internet'],
                                                        'products':['Telstra Smart modem - Professional installation','International Ultimate','Telstra Smart Wi-Fi Booster']
                                            },
                                            '5G':{'entry_point':'',
                                                       'plans':['5G Business Internet'],
                                                       'products':[]},
                                            'Office Phone':{'entry_point':'https://www.telstra.com.au/small-business/office-phones',
                                                        'plans':['Ultimate Business Voice - $55'],
                                                        'products':['Telstra Smart modem - Professional installation','Business International Calling Pack']

                                            }

                                          }
                            } 
    }