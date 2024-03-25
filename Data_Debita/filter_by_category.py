import requests
import json
from categories import APR, APR_filter, ltv_calculator, ltv_filter, name

api_data = requests.get('https://rbn3bwlfb1.execute-api.us-east-1.amazonaws.com/getData/Loans')

data = api_data.json()

#----------- filtros de data --------------------

APR_loans = APR(data)

apr_loans_filter = APR_filter(data, 50)

#def data_with_ltv(datos):
    #for item in datos:
        #principleAmount = item.get('principleAmount', 0)
        #collateralAmount = item.get('collateralAmount', 0)
        #names = item.get('principleAddress', 0)
        #if names == '0x1B6382DBDEa11d97f24495C9A90b7c88469134a4':
            #names = 'axlUSDC'
        #elif names == '0x21be370D5312f44cB42ce377BC9b8a0cEF1A4C83':
            #names = 'WFTM'
        #elif names == '0x3Fd3A0c85B70754eFc07aC9Ac0cbBDCe664865A6':
            #names = 'EQUAL'
        #elif names == '0xE53aFA646d48E9EF68fCd559F2a598880a3f1370':
            #names = 'TOMB+'
        #else:
            #names = item.get('principleAddress', 0)
        #ltv = ltv_calculator(principleAmount, collateralAmount)
        #print("LTV:", ltv, "Token:", names)
        #print()

ltv_loans_filter = ltv_filter(data)

token_names = name(data)

for item in ltv_loans_filter:
    print("LTV:", ltv_calculator(item.get('principleAmount'), item.get('collateralAmount')), "%")
    print("Token:", name(item.get('principleAddress')))
    print()
    
    

#----------- impresión de filtros de data --------------------

#print("Loans filtrados por APR:", apr_loans_filter)
#print(APR_loans)
#data_with_ltv(data)
