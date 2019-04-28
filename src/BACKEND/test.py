import json
from web3 import Web3

''' SETS UP THE ENVIRONMENT '''

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

web3.eth.defaultAccount = web3.eth.accounts[0]

print(web3.eth.accounts[0])

address = web3.toChecksumAddress('0xfdae4ea9f40fa5c4bebb822714da176950d6a976')
raw_abi = '[{"constant":false,"inputs":[{"name":"_c","type":"string"},{"name":"_f","type":"string"},{"name":"_p_title","type":"string"},{"name":"_p_desc","type":"string"},{"name":"_p_amt","type":"int256"},{"name":"_s","type":"string"}],"name":"Generate","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"Project_Status","outputs":[{"name":"c","type":"string"},{"name":"f","type":"string"},{"name":"p_title","type":"string"},{"name":"p_desc","type":"string"},{"name":"s","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"name":"Contractor","type":"string"},{"indexed":false,"name":"Freelancer","type":"string"},{"indexed":false,"name":"Project_Desc","type":"string"},{"indexed":false,"name":"Project_Title","type":"string"},{"indexed":false,"name":"Project_Amount","type":"int256"},{"indexed":false,"name":"Status","type":"string"},{"indexed":false,"name":"Project_Code","type":"string"}],"name":"State","type":"event"}]'

abi = json.loads(raw_abi)

contract = web3.eth.contract(address=address, abi=abi)

''' -------------------------------- '''



def run_generate_contract(contractor, freelancer, project_title, project_desc,
project_amount):
    if not web3.isConnected():
        return False

    contract.functions.Generate(contractor, freelancer, project_title, project_desc,
    int(project_amount), 'Generated New Project').transact()

def get_status():
    return contract.functions.Project_Status().call()

def get_history():
    return contract.events.State.createFilter(fromBlock=0).get_all_entries()



run_generate_contract("alice", "bob", "proj1", "A cool project", 5)
print(get_status())
