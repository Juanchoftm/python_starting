import mysql.connector
import json
from web3 import Web3
import requests


DEBITA_LOAN_ABI = json.loads('''[
                             {
      "inputs": [],
      "name": "debitaOfferV2",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    },
   {
      "inputs": [],
      "name": "getLoanData",
      "outputs": [
        {
          "components": [
            {
              "internalType": "uint256[2]",
              "name": "IDS",
              "type": "uint256[2]"
            },
            {
              "internalType": "address[2]",
              "name": "assetAddresses",
              "type": "address[2]"
            },
            {
              "internalType": "uint256[2]",
              "name": "assetAmounts",
              "type": "uint256[2]"
            },
            {
              "internalType": "bool[2]",
              "name": "isAssetNFT",
              "type": "bool[2]"
            },
            {
              "internalType": "uint256[3]",
              "name": "nftData",
              "type": "uint256[3]"
            },
            {
              "internalType": "uint32",
              "name": "timelap",
              "type": "uint32"
            },
            {
              "internalType": "address",
              "name": "interestAddress_Lending_NFT",
              "type": "address"
            },
            {
              "internalType": "uint8",
              "name": "paymentCount",
              "type": "uint8"
            },
            {
              "internalType": "uint8",
              "name": "paymentsPaid",
              "type": "uint8"
            },
            {
              "internalType": "uint256",
              "name": "paymentAmount",
              "type": "uint256"
            },
            {
              "internalType": "uint256",
              "name": "deadline",
              "type": "uint256"
            },
            {
              "internalType": "uint256",
              "name": "deadlineNext",
              "type": "uint256"
            },
            {
              "internalType": "bool",
              "name": "executed",
              "type": "bool"
            }
          ],
          "internalType": "struct DebitaV2Loan.LoanData",
          "name": "",
          "type": "tuple"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    }
  ]''')


OFFER_CONTRACT = json.loads(''' [
                            {
      "inputs": [],
      "name": "getOffersData",
      "outputs": [
        {
          "components": [
            {
              "internalType": "address[2]",
              "name": "assetAddresses",
              "type": "address[2]"
            },
            {
              "internalType": "uint256[2]",
              "name": "assetAmounts",
              "type": "uint256[2]"
            },
            {
              "internalType": "bool[2]",
              "name": "isAssetNFT",
              "type": "bool[2]"
            },
            {
              "internalType": "uint16",
              "name": "interestRate",
              "type": "uint16"
            },
            {
              "internalType": "uint256[3]",
              "name": "nftData",
              "type": "uint256[3]"
            },
            {
              "internalType": "uint8",
              "name": "paymentCount",
              "type": "uint8"
            },
            {
              "internalType": "uint32",
              "name": "_timelap",
              "type": "uint32"
            },
            {
              "internalType": "bool",
              "name": "isLending",
              "type": "bool"
            },
            {
              "internalType": "bool",
              "name": "isPerpetual",
              "type": "bool"
            },
            {
              "internalType": "bool",
              "name": "isActive",
              "type": "bool"
            },
            {
              "internalType": "address",
              "name": "interest_address",
              "type": "address"
            }
          ],
          "internalType": "struct IDebitaOffer.OfferInfo",
          "name": "",
          "type": "tuple"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    }
]''')


READ_CONTRACT = json.loads('''

 [
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "_add",
          "type": "address"
        }
      ],
      "name": "getDataFrom",
      "outputs": [
        {
          "components": [
            {
              "internalType": "uint256",
              "name": "id",
              "type": "uint256"
            },
            {
              "internalType": "int128",
              "name": "amount",
              "type": "int128"
            },
            {
              "internalType": "bool",
              "name": "voted",
              "type": "bool"
            }
          ],
          "internalType": "struct ReaderVeNFT.InfoveNFT[]",
          "name": "",
          "type": "tuple[]"
        }
      ],
      "stateMutability": "view",
      "type": "function"
    }
  ]
''')
 

API = "https://rbn3bwlfb1.execute-api.us-east-1.amazonaws.com/getData/Loans"
results3 = requests.get(API).json()

apiFetch = "https://rough-thrilling-voice.fantom.quiknode.pro/08adfc18cdb46fc87e3cf44a6fad0a81975fb6c4/"
w3 = Web3(Web3.HTTPProvider(apiFetch))

def getDecimals(address: str):
  if( address == "0x1B6382DBDEa11d97f24495C9A90b7c88469134a4"):
    return 6
  
  return 18

def getValuedAddress(address: str):
  if(address == "0x8313f3551C4D3984FfbaDFb42f780D0c8763Ce94"):
    return "0x3Fd3A0c85B70754eFc07aC9Ac0cbBDCe664865A6"
  
  return address

print(results3[0])
contractRead = w3.eth.contract(address="0xa0fD9265FAC42EcdfFF494e3dB6466b207D98C6D", abi=READ_CONTRACT)
for address in results3: 
  target_id = address['loanAddress']
  contract = w3.eth.contract(address=target_id, abi=DEBITA_LOAN_ABI)
  data = contract.functions.getLoanData().call()
  offerAddress = contract.functions.debitaOfferV2().call()
  offerContract = w3.eth.contract(address=offerAddress, abi=OFFER_CONTRACT)
  offerContractData = offerContract.functions.getOffersData().call()
  interest = offerContractData[3]
  print(target_id)
  lit = contractRead.functions.getDataFrom(target_id).call()
  print(lit)
  principleToken = data[1][0]
  collateralToken = data[1][1]
  print(collateralToken == "0x8313f3551C4D3984FfbaDFb42f780D0c8763Ce94")
  principleAmount = data[2][0]
  collateralAmount = data[2][1]
  executed = data[12]
  if(collateralToken == "0x8313f3551C4D3984FfbaDFb42f780D0c8763Ce94" and executed == False): 
     collateralAmount = lit[0][1]
  collateralToken = getValuedAddress(collateralToken)
  data_Principle = requests.get(f"https://coins.llama.fi/prices/current/fantom:{principleToken}")
  data_Collateral = requests.get(f"https://coins.llama.fi/prices/current/fantom:{collateralToken}")
  
  priceCollateral = 0
  if(data_Collateral.json()['coins'] == {} and collateralToken == "0x43F9a13675e352154f745d6402E853FECC388aA5"):
      daata = requests.get("https://api.dexscreener.com/latest/dex/pairs/fantom/0x6f60e79e3be2009f1c8b6786b761f8d3ee67d18f")
      priceCollateral = float(daata.json()['pair']['priceUsd'])
      print("$sGOAT")
  else: 
      priceCollateral = (data_Collateral.json()['coins'][f'fantom:{collateralToken}']['price'])

  pricePrinciple = (data_Principle.json()['coins'][f'fantom:{principleToken}']['price'])



  paymentCount = data[7] 
  duration = data[5] * paymentCount
  deadline = data[10]
  ltv = ( pricePrinciple * (principleAmount / 10 ** getDecimals(principleToken))) / (priceCollateral * (collateralAmount / 10 ** getDecimals(collateralToken))) * 100
  if executed:
    ltv = 0 

  update_query = "UPDATE Market_info SET PRINCIPLE = %s WHERE ADDRESS = %s"
  update_query_2 = "UPDATE Market_info SET COLLATERAL = %s WHERE ADDRESS = %s"
  update_query_3 = "UPDATE Market_info SET P_AMOUNT = %s WHERE ADDRESS = %s"
  update_query_4 = "UPDATE Market_info SET C_AMOUNT = %s WHERE ADDRESS = %s"
  update_query_5 = "UPDATE Market_info SET DAYS = %s WHERE ADDRESS = %s"
  update_query_6 = "UPDATE Market_info SET INTEREST = %s WHERE ADDRESS = %s"
  update_query_7 = "UPDATE Market_info SET PAYMENTS = %s WHERE ADDRESS = %s"
  update_query_8 = "UPDATE Market_info SET LTV = %s WHERE ADDRESS = %s"
  update_query_9 = "UPDATE Market_info SET BLOCKEND = %s WHERE ADDRESS = %s"

  ## cursor.execute(update_query, (principleToken, target_id))
  # cursor.execute(update_query_2, (collateralToken, target_id))
  # cursor.execute(update_query_3, (principleAmount, target_id))
  # cursor.execute(update_query_4, (collateralAmount, target_id))
  # cursor.execute(update_query_5, (duration, target_id))
 #  cursor.execute(update_query_6, (interest, target_id))
  #cursor.execute(update_query_7, (paymentCount, target_id))
 # cursor.execute(update_query_8, (ltv, target_id))
  #cursor.execute(update_query_9, (deadline, target_id))


  # cnx.commit()

  print("PUSHED")



