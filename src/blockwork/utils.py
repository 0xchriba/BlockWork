import json
from web3 import Web3
import ipfsapi
import time

ipfs_domain = "http://localhost:8080/ipfs/"


ipfs = ipfsapi.connect('127.0.0.1', 5001)


def ipfs_upload(file):
    hash = ipfs.add(file)
    return hash['Hash']


def ipfs_download(hash):
    file = ipfs.cat(hash)
    file = str(file)[2:-1]

    file = file.replace('\\n', '<br>')
    return file


def get_contract():
    ganache_url = "http://127.0.0.1:7545"
    web3 = Web3(Web3.HTTPProvider(ganache_url))
    web3.eth.defaultAccount = web3.eth.accounts[0]

    ''' Test 1'''
    # address = web3.toChecksumAddress('0xfdae4ea9f40fa5c4bebb822714da176950d6a976')
    # raw_abi = '[{"constant":false,"inputs":[{"name":"_c","type":"string"},{"name":"_f","type":"string"},{"name":"_p_title","type":"string"},{"name":"_p_desc","type":"string"},{"name":"_p_amt","type":"int256"},{"name":"_s","type":"string"}],"name":"Generate","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"Project_Status","outputs":[{"name":"c","type":"string"},{"name":"f","type":"string"},{"name":"p_title","type":"string"},{"name":"p_desc","type":"string"},{"name":"s","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"name":"Contractor","type":"string"},{"indexed":false,"name":"Freelancer","type":"string"},{"indexed":false,"name":"Project_Desc","type":"string"},{"indexed":false,"name":"Project_Title","type":"string"},{"indexed":false,"name":"Project_Amount","type":"int256"},{"indexed":false,"name":"Status","type":"string"},{"indexed":false,"name":"Project_Code","type":"string"}],"name":"State","type":"event"}]'
    # abi = json.loads(raw_abi)

    address = web3.toChecksumAddress('0x49f7342c9e62a359d643abce2cbf49d0c7fbc31c')
    raw_abi = '[{"constant":true,"inputs":[],"name":"Project_Info","outputs":[{"name":"c","type":"string"},{"name":"f","type":"string"},{"name":"p_title","type":"string"},{"name":"p_desc","type":"string"},{"name":"p_amt","type":"int256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_s","type":"string"}],"name":"Finish_Project","outputs":[{"name":"p_amt","type":"int256"},{"name":"p_code","type":"string"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_c","type":"string"},{"name":"_p_title","type":"string"},{"name":"_p_desc","type":"string"},{"name":"_p_amt","type":"int256"},{"name":"_s","type":"string"},{"name":"_m_comp","type":"bool[]"},{"name":"_m_desc","type":"bytes32[]"}],"name":"Generate","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"Project_Status","outputs":[{"name":"s","type":"string"},{"name":"p_code","type":"string"},{"name":"m_comp","type":"bool[]"},{"name":"m_desc","type":"bytes32[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_f","type":"string"},{"name":"_s","type":"string"}],"name":"Accept","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_i","type":"int256"},{"name":"_p_code","type":"string"},{"name":"_s","type":"string"}],"name":"Complete_Milestone","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"name":"Status","type":"string"},{"indexed":false,"name":"Project_Code","type":"string"},{"indexed":false,"name":"Milestones_Completed","type":"bool[]"},{"indexed":false,"name":"Milestone_Descriptions","type":"bytes32[]"}],"name":"State","type":"event"}]'
    abi = json.loads(raw_abi)

    contract = web3.eth.contract(address=address, abi=abi)
    return contract

contract = get_contract()

def run_generate_contract(contractor, project_title, project_desc,
project_amount, milestone_descriptions):

    milestones_completed = [False] * len(milestone_descriptions)
    hex_descriptions = []

    print(len(milestones_completed))

    for description in milestone_descriptions:
        hex_descriptions.append(description.encode('utf-8'))


    contract.functions.Generate(contractor, project_title, project_desc,
    int(project_amount), 'Generated new project', milestones_completed, hex_descriptions).transact()

def accept_contract(freelancer):
    status = freelancer + " has accepted the project."
    contract.functions.Accept(freelancer, status).transact()
    print(status)

def get_status():
    return contract.functions.Project_Status().call()

def get_info():
    return contract.functions.Project_Info().call()

def update_milestones(index, file):
    index = int(index)
    state = get_status()
    m_len = len(state[2])
    print("here")
    percent = int((index+1)/m_len)*100
    status = "Project is " + str(percent) + "% complete."
    contract.functions.Complete_Milestone(index, file, status).transact()

    return percent

def finish_project():
    state = get_status()
    # for val in state[2]:
    #     if not val:
    #         print("Project is not complete")
    #         return
    contract.functions.Finish_Project("Project Completed. Dispursing Funds").transact()
    info = get_info()



    #calculate payments NO ARBITRATORS YET
    total = info[-1]
    balance = total
    freelancer_amount = round(0.90 * total,2)
    balance -= freelancer_amount
    arbitrator_count = 3
    arbitrator_amount = round(0.05 * total / arbitrator_count, 2)
    balance -= arbitrator_amount

    # #send money to arbitrators
    # arbitrator_amount = (0.03 * total) - len(self.arbitrators)
    # for arbitrator in self.arbitratiors:
    #     total -= arbitrator_amount


    #send money to US
    return {
        'F Pay' : freelancer_amount,
        'A Pay' : arbitrator_amount,
        'B Pay': round(balance,2),
    }


skills = ['C++', 'C', 'R', 'Java', 'Tensorflow', 'Solidity', 'JavaScript', 'UI', 'CSS', 'HTML',
        'Go', 'Python', 'React', 'Node.js', 'React', 'Flutter', 'Android', 'IOS', 'Unix',
         'Ruby', 'AWS', 'GCP', 'Assembly', 'PHP', 'Swift', 'C#', 'Objectiv-C', 'Scala', 'Firebase',
         'Kotlin', 'Lisp', 'SQL', 'Spark', 'Django', 'Angular', 'jQuery', 'MongoDB', 'Docker', 'Kubernetes']

def get_history():
    return contract.events.State.createFilter(fromBlock=0).get_all_entries()
