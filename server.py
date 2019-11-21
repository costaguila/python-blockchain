from flask import Flask, jsonify
from uuid import uuid4

#My blockchain class
from blockchain import Blockchain

#Initiate server
app = Flask(__name__)
# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')
# Instantiate the Blockchain
blockchain = Blockchain()

@app.route('/mine',methods=['GET'])
def mine():
    return "Mining..."

@app.route('/chain',methods=['GET'])
def allblocks():
    response = {
        'chain': blockchain.blocks,
        'length': len(blockchain.blocks)
    }
    return jsonify(response)

@app.route('/transaction',methods=['POST'])
def new_transaction():
    return "new transaction..."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
