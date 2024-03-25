import requests
import json

api_data = requests.get('https://rbn3bwlfb1.execute-api.us-east-1.amazonaws.com/getData/Loans')

#print(json.dumps(api_data.json(), indent=2))

pregunta_usuario = input("""
    Selecciona que quieres saber sobre los préstamos en Débita
    1)Loan Address         2)Principle Adress      3)Collateral Address
    4)Principle Amount     5)Collateral Amount     6)Duration
    7)Interes              8)Effective APR         9)Payments cuantity
    10)Status
     """)


for item in api_data.json():
    loanAddress = item['loanAddress']
    principleAddress = item['principleAddress']
    collateralAddress = item['collateralAddress']
    principleAmount = item['principleAmount']
    collateralAmount = item['collateralAmount']
    duration = item['duration']
    interest = item['interest']
    effectiveApr = item['effectiveApr']
    payments = item['payments']
    status = item['status']
    
    if pregunta_usuario == '1':
        print(loanAddress)
    elif pregunta_usuario == '2':
        print(principleAddress)
    elif pregunta_usuario == '3':
        print(collateralAddress)
    elif pregunta_usuario == '4':
        print(principleAmount)
    elif pregunta_usuario == '5':
        print(collateralAmount)
    elif pregunta_usuario == '6':
        print(duration)
    elif pregunta_usuario == '7':
        print(interest)
    elif pregunta_usuario == '8':
        print(effectiveApr)
    elif pregunta_usuario == '9':
        print(payments)
    elif pregunta_usuario == '10':
        print(status)
    
    else:
        print('wrong')