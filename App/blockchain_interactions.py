import subprocess


def test_subprocess():
	"""test_subprocess is code to demonstrate hello world writing commandline commands and reading them"""
	print("running test_subprocess")

	# Windows
	# y = subprocess.call(["dir"], shell=True) 
	# Linux (for raspbery pi)
	y = subprocess.call(["ls"], shell=True) 
	print(y)
	

def setup_anvil():
	"""setup_anvil is code to run commnds for setting up anvil"""
	print("running setup_anvil")

	y = subprocess.call(["anvil"], shell=True) 
	print(y)


def make_blockchain_payment():
	"""make_blockchain_payment is code to make a mock blockchain payment for coworking"""
	print("running make_blockchain_payment")

	from web3 import Web3

	# copy from anvil printout
	local_testnet_url = "http://127.0.0.1:8545"

	web3 = Web3(Web3.HTTPProvider(local_testnet_url))

	if web3.is_connected():
		print("Connected to Anvil")
	else:
		print("Failed to connect to Anvil")

	# getting latest block
	latest_block = web3.eth.get_block('latest')
	print(latest_block)

	# test accounts
	account_1 = web3.eth.accounts[1]
	account_2 = web3.eth.accounts[2]

	# mock transfer of funds
	tx_hash = web3.eth.send_transaction({
		"from": account_1,
		"to": account_2,
		"value": 42,
		"data": "Hello world!"
	})

	tx = web3.eth.get_transaction(tx_hash)
	assert tx["from"] == account_1

	# testing latest block after transaction
	latest_block = web3.eth.get_block('latest')
	print(latest_block)


if __name__ == '__main__':
	test_subprocess()

	setup_anvil()

	make_blockchain_payment()
