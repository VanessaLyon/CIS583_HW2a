import eth_account
from web3 import Web3
from eth_account.messages import encode_defunct

def sign(m):
    w3 = Web3()

    # create an eth account and recover the address (derived from the public key) and private key
    account = eth_account.Account.create()
    eth_address = account.address
    private_key = account.privateKey

    # generate signature
    message = encode_defunct(text=m)
    signature = eth_account.sign_message(message, private_key)

    assert isinstance(signature, eth_account.datastructures.Signature)

    return eth_address, signature
