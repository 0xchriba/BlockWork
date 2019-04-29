import json
from web3 import Web3
import ipfsapi
import time
from . import setup as s

ipfs_domain = "http://localhost:8080/ipfs/"


ipfs = ipfsapi.connect(s.ipfs_domain, s.ipfs_port)



def ipfs_upload(file):
    hash = ipfs.add(file)
    return hash['Hash']


def ipfs_download(hash):
    file = ipfs.cat(hash)
    file = str(file)[2:-1]

    file = file.replace('\\n', '<br>')
    return file


def get_contract():
    ganache_url = "http://" + s.ganache_domain + ":" + str(s.ganache_port)
    web3 = Web3(Web3.HTTPProvider(ganache_url))
    web3.eth.defaultAccount = web3.eth.accounts[0]

    ''' Test 1'''

    address = web3.toChecksumAddress(s.contract_address)
    abi = json.loads(s.contract_abi)

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
    freelancer_amount = round(0.93 * total,2)
    balance -= freelancer_amount
    arbitrator_count = 3
    arbitrator_amount = round(0.02 * total / arbitrator_count, 2)
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

verif = ['None', 'Self Verification', 'Arbitrators', 'Test Cases']

def get_history():
    return contract.events.State.createFilter(fromBlock=0).get_all_entries()
