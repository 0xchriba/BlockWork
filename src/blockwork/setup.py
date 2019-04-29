ipfs_domain = '127.0.0.1'
ipfs_port = 5001

ganache_domain = "127.0.0.1"
ganache_port = 7545


contract_address = '0x49f7342c9e62a359d643abce2cbf49d0c7fbc31c'
contract_abi = '[{"constant":true,"inputs":[],"name":"Project_Info","outputs":[{"name":"c","type":"string"},{"name":"f","type":"string"},{"name":"p_title","type":"string"},{"name":"p_desc","type":"string"},{"name":"p_amt","type":"int256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_s","type":"string"}],"name":"Finish_Project","outputs":[{"name":"p_amt","type":"int256"},{"name":"p_code","type":"string"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_c","type":"string"},{"name":"_p_title","type":"string"},{"name":"_p_desc","type":"string"},{"name":"_p_amt","type":"int256"},{"name":"_s","type":"string"},{"name":"_m_comp","type":"bool[]"},{"name":"_m_desc","type":"bytes32[]"}],"name":"Generate","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"Project_Status","outputs":[{"name":"s","type":"string"},{"name":"p_code","type":"string"},{"name":"m_comp","type":"bool[]"},{"name":"m_desc","type":"bytes32[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"_f","type":"string"},{"name":"_s","type":"string"}],"name":"Accept","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"_i","type":"int256"},{"name":"_p_code","type":"string"},{"name":"_s","type":"string"}],"name":"Complete_Milestone","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":false,"name":"Status","type":"string"},{"indexed":false,"name":"Project_Code","type":"string"},{"indexed":false,"name":"Milestones_Completed","type":"bool[]"},{"indexed":false,"name":"Milestone_Descriptions","type":"bytes32[]"}],"name":"State","type":"event"}]'
