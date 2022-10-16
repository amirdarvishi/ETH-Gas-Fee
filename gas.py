from web3 import Web3,HTTPProvider
import time
from datetime import datetime
to_address = "0xD9E303df7a0Ba9cE6D041D192f7D69ea69860d7a"


erc20_simplified_abi = [{'constant': True,
                         'inputs': [],
                         'name': 'name',
                         'outputs': [{'name': '', 'type': 'string'}],
                         'payable': False,
                         'stateMutability': 'view',
                         'type': 'function'},
                        {'constant': False,
                         'inputs': [{'name': '_spender', 'type': 'address'},
                                    {'name': '_value', 'type': 'uint256'}],
                         'name': 'approve',
                         'outputs': [{'name': '', 'type': 'bool'}],
                         'payable': False,
                         'stateMutability': 'nonpayable',
                         'type': 'function'},
                        {'constant': True,
                         'inputs': [],
                         'name': 'totalSupply',
                         'outputs': [{'name': '', 'type': 'uint256'}],
                         'payable': False,
                         'stateMutability': 'view',
                         'type': 'function'},
                        {'constant': False,
                         'inputs': [{'name': '_from', 'type': 'address'},
                                    {'name': '_to', 'type': 'address'},
                                    {'name': '_value', 'type': 'uint256'}],
                         'name': 'transferFrom',
                         'outputs': [{'name': '', 'type': 'bool'}],
                         'payable': False,
                         'stateMutability': 'nonpayable',
                         'type': 'function'},
                        {'constant': True,
                         'inputs': [],
                         'name': 'decimals',
                         'outputs': [{'name': '', 'type': 'uint8'}],
                         'payable': False,
                         'stateMutability': 'view',
                         'type': 'function'},
                        {'constant': True,
                         'inputs': [{'name': '_owner', 'type': 'address'}],
                         'name': 'balanceOf',
                         'outputs': [{'name': '', 'type': 'uint256'}],
                         'payable': False,
                         'stateMutability': 'view',
                         'type': 'function'},
                        {'constant': True,
                         'inputs': [],
                         'name': 'symbol',
                         'outputs': [{'name': '', 'type': 'string'}],
                         'payable': False,
                         'stateMutability': 'view',
                         'type': 'function'},
                        {'constant': False,
                         'inputs': [{'name': '_to', 'type': 'address'},
                                    {'name': '_value', 'type': 'uint256'}],
                         'name': 'transfer',
                         'outputs': [{'name': '', 'type': 'bool'}],
                         'payable': False,
                         'stateMutability': 'nonpayable',
                         'type': 'function'},
                        {'constant': True,
                         'inputs': [{'name': '_owner', 'type': 'address'},
                                    {'name': '_spender', 'type': 'address'}],
                         'name': 'allowance',
                         'outputs': [{'name': '', 'type': 'uint256'}],
                         'payable': False,
                         'stateMutability': 'view',
                         'type': 'function'},
                        {'anonymous': False,
                         'inputs': [{'indexed': True, 'name': '_from', 'type': 'address'},
                                    {'indexed': True, 'name': '_to', 'type': 'address'},
                                    {'indexed': False, 'name': '_value', 'type': 'uint256'}],
                         'name': 'Transfer',
                         'type': 'event'},
                        {'anonymous': False,
                         'inputs': [{'indexed': True, 'name': '_owner', 'type': 'address'},
                                    {'indexed': True, 'name': '_spender', 'type': 'address'},
                                    {'indexed': False, 'name': '_value', 'type': 'uint256'}],
                         'name': 'Approval',
                         'type': 'event'}]



from_address = "0x8097a508636686391520bF87DBFC12F556E7a68C"



full_node_connection = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/5df6a6f5ac5840e3b452355cd87f930d"))

smart_contract = full_node_connection.eth.contract(
    address=full_node_connection.toChecksumAddress("0xdac17f958d2ee523a2206206994597c13d831ec7"),
    abi=erc20_simplified_abi)



while True:
	with open("t.txt","a+") as file:
		gas = smart_contract.functions.transfer(from_address, 5000000).estimateGas({'from': to_address})
		file.write("\n")
		file.write(str(gas))
		file.write(",")
		file.write(str(datetime.now()))
		
		time.sleep(30)
		file.close()