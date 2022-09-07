from brownie import sellingContract , accounts , config , network
from scripts.deploy import get_account
from web3 import Web3 , HTTPProvider
import json

def set_fun():
    my_contract = sellingContract[-1]
    account = get_account()
    result = my_contract.setItem("ball",10,{'from':account})

def call_fun():
    my_contract = sellingContract[-1]
    account = get_account()
    item = my_contract.newAsset()
    print(f"asset: {item}")

       
def pur_fun():
    my_contract = sellingContract[-1]
   # abi = json.loads('[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"internalType":"address","name":"seller","type":"address"},{"indexed":false,"internalType":"address","name":"buyer","type":"address"},{"indexed":false,"internalType":"string","name":"bought","type":"string"}],"name":"purchaseOp","type":"event"},{"inputs":[{"internalType":"uint256","name":"","type":"uint256"}],"name":"assetList","outputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"string","name":"description","type":"string"},{"internalType":"uint256","name":"price","type":"uint256"},{"internalType":"bool","name":"sold","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"buyer","outputs":[{"internalType":"address payable","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"newAsset","outputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"string","name":"description","type":"string"},{"internalType":"uint256","name":"price","type":"uint256"},{"internalType":"bool","name":"sold","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"parties","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"_buyer","type":"address"},{"internalType":"string","name":"_item","type":"string"}],"name":"purchase","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"seller","outputs":[{"internalType":"address payable","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"_description","type":"string"},{"internalType":"uint256","name":"_price","type":"uint256"}],"name":"setItem","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"nonpayable","type":"function"}]')
   # address = Web3.toChecksumAddress('0xE1419e19E779Bc2830E77e61C0E6eBb16AF328dc')
   # contract_obj = Web3(HTTPProvider('https://rinkeby.infura.io/v3/d563443cfeb44fb1849212fef35c802d')).eth.contract(address=address,abi=abi)
    account = get_account()
    buyer = accounts.add(config["wallets"]["from_key2"])
    
    #nonce = Web3(HTTPProvider('https://rinkeby.infura.io/v3/d563443cfeb44fb1849212fef35c802d')).eth.getTransactionCount('0x8C1EBd5Ea93CF1A896Cf1FF87895c82144e795A6')
    #purchase_function = my_contract.functions.purchase(buyer,"ball").buildTransaction({'gas':250000,'gasPrice': Web3.toWei(1,'gwei'),'from':buyer,'nonce':nonce})
    #signed_tx = Web3.eth.account.signTransaction(purchase_function,private_key= buyer)
    #Web3.eth.sendRawTransaction(signed_tx.rawTransaction)
    
    #txn = purchase_function.buildTransaction({'from':buyer,'nonce':nonce})
    #buyer_address = Web3(HTTPProvider('https://rinkeby.infura.io/v3/d563443cfeb44fb1849212fef35c802d')).eth.account.privateKeyToAccount(Web3.toBytes(buyer))
    
    buyer_address = '0x8C1EBd5Ea93CF1A896Cf1FF87895c82144e795A6'
    # tx_hash = contract_obj.purchase(buyer_address,"ball").send_transaction({'from':buyer_address})
    # Web3.eth.waitForTransactionReceipt(tx_hash)
    purchase = my_contract.purchase(buyer_address,"ball",{'from':buyer,})

    #buy_op = my_contract.purchase(buyer,"ball",{'from':buyer})
    #buy_op = my_contract.purchase.call(buyer,"ball")
    print(f"current owner is {buyer_address}")

def main():
    #set_fun()    
    call_fun()
    pur_fun()