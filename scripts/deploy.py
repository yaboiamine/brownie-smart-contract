
from brownie import sellingContract , network , config , accounts
from web3 import Web3

LOCAL_BLOCKCHAIN_ENVIRONMENTS = ['development' , 'ganache-local']

def get_account():
    if(network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS ):
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_contract():
    account = get_account()
    my_contract = sellingContract.deploy({'from':account},publish_source=config["networks"][network.show_active()].get("verify"))   
    print("contract deployed at: ", my_contract.address)

def main():
    deploy_contract()         
