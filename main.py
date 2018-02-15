from block_io import BlockIo
import sys
version = 2
PIN = 'r06921078'
label = input('Choose one cryptocurrency:\nBitcoin\nLitecoin\nDogecoin\n---------------------------------------------------\n')
API_Keys = {"Bitcoin":"4b82-48e6-1373-563e", "Litecoin":"c999-6c44-8836-7569", "Dogecoin":"8fb6-1e9e-0ce8-453b"}
block_io = BlockIo(API_Keys[label], PIN, version)
while True:
	Action = input('---------------------------------------------------\n1.Get new address\n2.Get my address\n3.Withdraw\n4.Withdraw from address\n5.Withdraw from label\n6.Exit\n')
	if Action == '1':
		print('---------------------------------------------------\nGenerate a random label\nEnter a label')
		S = input('(Random/Your own label) ')
		if S == 'Random':
			account = block_io.get_new_address()
		else :
			account = block_io.get_new_address(label=S)
		print(account['status'])
		print('Label: ',account['data']['label'],'\nAddress: ',account['data']['address'] )
	elif Action == '2':
		S = input('---------------------------------------------------\n1.List all address\n2.Get address with label\n')
		if S == '1':
			Accounts = block_io.get_my_addresses()
			for i in Accounts['data']['addresses']:
				print('Label: ',i['label'],'\nAddress: ',i['address'],'\nAvailable Balance: ',i['available_balance'],'\n')
		else :
			SS = input('Enter a label: ')
			Accounts = block_io.get_address_by(label=SS)
			print('Label: ',Accounts['data']['label'],'\nAddress: ',Accounts['data']['address'],'\nAvailable Balance: ',Accounts['data']['available_balance'] )
	elif Action == '3':
		amount = input('Amount: ')
		S = input('---------------------------------------------------\n1.Withdraw by address\n2.Withdraw by label\n')
		if S == '1':
			To_address = input('To Address: ')
			result = block_io.withdraw(amounts=amount, to_addresses=To_address, pin=PIN)
			print(result['status'])
			print('TXID: ',result['data']['txid'])
			print('Amount withdraw: ',result['data']['amount_withdrawn'])
			print('Amount Sent: ',result['data']['amount_sent'])
			print('Network Fee: ',result['data']['network_fee'])
			print('BlockIO Fee',result['data']['blockio_fee'],'\n')
		else :
			To_label = input('To label: ')
			To_address = block_io.get_address_by(label=To_label)['data']['address']
			result = block_io.withdraw(amounts=amount, to_addresses=To_address, pin=PIN)
			print(result['status'])
			print('TXID: ',result['data']['txid'])
			print('Amount withdraw: ',result['data']['amount_withdrawn'])
			print('Amount Sent: ',result['data']['amount_sent'])
			print('Network Fee: ',result['data']['network_fee'])
			print('BlockIO Fee',result['data']['blockio_fee'],'\n')
	elif Action == '4':
		amount = input('Amount: ')
		From_address = input('From Address: ')
		To_address = input('To Address: ')
		result = block_io.withdraw_from_addresses(amounts=amount, from_addresses=From_address, to_addresses=To_address, pin=PIN)
		print(result['status'])
		print('TXID: ',result['data']['txid'])
		print('Amount withdraw: ',result['data']['amount_withdrawn'])
		print('Amount Sent: ',result['data']['amount_sent'])
		print('Network Fee: ',result['data']['network_fee'])
		print('BlockIO Fee',result['data']['blockio_fee'],'\n')
	elif Action == '5':
		amount = input('Amount: ')
		From_label = input('From Label: ')
		To_label = input('To Label: ')
		From_address = block_io.get_address_by(label=From_label)['data']['address']
		To_address = block_io.get_address_by(label=To_label)['data']['address']
		result = block_io.withdraw_from_addresses(amounts=amount, from_addresses=From_address, to_addresses=To_address, pin=PIN)
		print(result['status'])
		print('TXID: ',result['data']['txid'])
		print('Amount withdraw: ',result['data']['amount_withdrawn'])
		print('Amount Sent: ',result['data']['amount_sent'])
		print('Network Fee: ',result['data']['network_fee'])
		print('BlockIO Fee',result['data']['blockio_fee'],'\n')
	elif Action == '6':
		break
		
		

