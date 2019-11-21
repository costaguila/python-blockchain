from blockchain import Blockchain

if __name__ == '__main__':
    'Initializing the blockchain(genesis block)'
    print('Initializing blockchain...')
    blockchain =  Blockchain()

    'Operating on the blockchain'
    print("\nAdding 5 blocks...\n")
    blockchain.add_block('id:5125,spent:5105.71,currency:BRL')
    blockchain.add_block('id:55,spent:50015.98,currency:CAD')
    blockchain.add_block('id:25,spent:1500.50,currency:BRL')
    blockchain.add_block('id:775,spent:510005.22,currency:USD')
    blockchain.add_block('id:684,spent:51500.00,currency:BRL')
    'Dump all hashes'
    print("\nBlock hashes from oldest to newest(all hashes must start and end with `00`):\n")
    for hash in blockchain.get_blockchain():
        print(hash)
