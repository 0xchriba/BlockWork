import json
from web3 import Web3
import time
# infura_url ="https://mainnet.infura.io/v3/05174d91c4304bf99de421c9f29a8442"
# web3 = Web3(Web3.HTTPProvider(infura_url))
# print(web3.isConnected())
# print(web3.eth.blockNumber)
#
# contract_abi = '[{"constant":true,"inputs":[],"name":"mintingFinished","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"unpause","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"}],"name":"mint","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"paused","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"finishMinting","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":false,"inputs":[],"name":"pause","outputs":[{"name":"","type":"bool"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"_to","type":"address"},{"name":"_amount","type":"uint256"},{"name":"_releaseTime","type":"uint256"}],"name":"mintTimelocked","outputs":[{"name":"","type":"address"}],"payable":false,"type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":false,"type":"function"},{"constant":false,"inputs":[{"name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":false,"inputs":[],"name":"MintFinished","type":"event"},{"anonymous":false,"inputs":[],"name":"Pause","type":"event"},{"anonymous":false,"inputs":[],"name":"Unpause","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"owner","type":"address"},{"indexed":true,"name":"spender","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"name":"from","type":"address"},{"indexed":true,"name":"to","type":"address"},{"indexed":false,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"}]'
#
# abi = json.loads(contract_abi)
#
# address = "0xd26114cd6EE289AccF82350c8d8487fedB8A0C07"
#
# contract = web3.eth.contract(address=address, abi=abi)
#
# totalSupply = contract.functions.totalSupply().call()
# print(web3.fromWei(totalSupply, "ether"))
#
# print(contract.functions.name().call())
# print(contract.functions.symbol().call())

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
print(web3.isConnected())

class User:
    def __init__(self, public_key, private_key):
        self.public_key = public_key
        self.private_key = private_key
        #TODO add rating
        self.rating = 10

    def send_ether(self, receiver_public_key, amount):
        nonce = web3.eth.getTransactionCount(self.public_key)
        tx = {
            'nonce': nonce,
            'to' : receiver_public_key,
            'value' : web3.toWei(amount, 'ether'),
            'gas' : 2000000,
            'gasPrice' : web3.toWei('50', 'gwei')
        }

        signed_tx = web3.eth.account.signTransaction(tx, self.private_key)
        tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)


        #gets transaction receipt
        tx_receipt = None
        count = 0
        while tx_receipt is None and (count < 30):
            tx_receipt = web3.eth.getTransactionReceipt(tx_hash)
            time.sleep(10)
            print(count)
            count += 1

        if tx_receipt is None:
            return {'status': 'failed', 'error': 'timeout'}
        return {'status': 'success', 'txn_receipt': tx_receipt}


alice_pub_key = "0x506042c1aEFA6742e16d1679B0f0c5e627F62E54"
alice_priv_key = "82b00464c40f5ebe2a0c66844fc7a9fd6ab8d5b1fdac2aba994343b673e60550"
alice = User(alice_pub_key, alice_priv_key)

bob_pub_key = "0x782d9642406cb6869F06A480a682ef829C0CC981"
bob_priv_key = "76a7a256881e1be774f30e619b104134e57e58e4aec1d8dd8c69a9c5959f1f19"
bob = User(bob_pub_key, bob_priv_key)


print(bob.send_ether(alice.public_key, 4))


#  import ipfsapi
# >>> api = ipfsapi.connect('127.0.0.1', 5001)
# >>> res = api.add('test.txt')
# >>> res
# {'Hash': 'QmWxS5aNTFEc9XbMX1ASvLET1zrqEaTssqt33rVZQCQb22', 'Name': 'test.txt'}
# >>> api.cat(res['Hash'])
# 'fdsafkljdskafjaksdjf\n'




class Project:
    __init__(self, project_description, milestone_descriptions, milestones_met, cost):
        assert verification_method == "Arbitrator Review" or verification_method == "Test Cases" or verification_method == "Self Review"
        self.contractor = ""
        self.freelancer = ""
        self.skills_needed = ""
        self.project_description = project_description
        self.milestone_descriptions = milestone_descriptions
        self.milestones_met = milestones_met
        self.arbitrators = []
        self.cost = cost

    def find_freelancer():
        #for all users
            #find user with max related score defned as: 1/n * factors
            #factors = rating/10 + skills_met/len(skills_needed)

    def project_status():
        count = 0
        incomplete = []
        for name, status in milestones_met:
            if status:
                count += 1
            else:
                incomplete.append(name)
        return {
            "status" : count / len(milestones_met,
            "incomplete" : incomplete
            }

    def raise_dispute():
        return None

    def find_arbitrators():
        #mixture of people familiar with skills and both contractors and freelancers
        return None

    def resolve_dispute():
        return None

    def complete_project():
        #if there were arbitrators send them 2%
        #update ratings
        #send 1% of
        return "Code to the contractor"

    def dispurse_funds():
        #send money to freelancer
        freelancer_amount = 0.98 * self.total
        send_ether(self, self.freelancer, freelancer_amount)
        self.total -= freelancer_amount

        #send money to arbitrators
        arbitrator_amount = (0.02 * self.total) - len(self.arbitrators)
        for arbitrator in self.arbitratiors:
            send_ether(self, arbitrator, arbitrator_amount)
            self.total -= arbitrator_amount

        #send money to US
        send_ether(self, '''BlockWork PubK''', self.total)
        self.total = 0

        return '''status code'''
