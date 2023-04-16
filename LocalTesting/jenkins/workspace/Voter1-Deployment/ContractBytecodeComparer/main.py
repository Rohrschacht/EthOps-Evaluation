#!/usr/bin/env python3
import web3
import textwrap


def main(rpc_url: str, contract_address: str, contract_file: str):
    w3 = web3.Web3(web3.HTTPProvider('http://localhost:8545'))
    checksum_address = w3.toChecksumAddress(contract_address)

    # get latest block number
    block_number = w3.eth.block_number

    for i in range(block_number, 0, -1):
        block = w3.eth.getBlock(i)
        if block['transactions']:
            for tx_hash in block['transactions']:
                tx = w3.eth.getTransaction(tx_hash)
                if tx['to'] is None:
                    tx_receipt = w3.eth.getTransactionReceipt(tx_hash)
                    if tx_receipt['contractAddress'] == checksum_address:
                        on_chain_code = tx['input'][2:]
                        break

    with open(contract_file, 'r') as f:
        file_content = f.read()
        off_chain_code = file_content
        if not 'on_chain_code' in locals():
            print('No contract code found on chain')
            return False
        if on_chain_code == off_chain_code:
            print('Contract code matches')
            return True
        else:
            print('Contract code does not match')
            print('On chain code: {}'.format(on_chain_code[:10]))
            print('Off chain code: {}'.format(off_chain_code[:10]))
            with open('on_chain_code.txt', 'w') as f:
                f.write(textwrap.fill(on_chain_code))
            with open('off_chain_code.txt', 'w') as f:
                f.write(textwrap.fill(off_chain_code))
            return False


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('contract_address', type=str, help='contract address')
    parser.add_argument('contract_file', type=str, help='contract file')
    parser.add_argument('--rpc', type=str, help='rpc url', default='http://localhost:8545')
    args = parser.parse_args()
    # return code 0 means success
    exit_code = 0 if main(args.rpc, args.contract_address, args.contract_file) else 1
    exit(exit_code)
