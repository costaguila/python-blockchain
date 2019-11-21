from datetime import datetime
import hashlib

class Blockchain:
    "Represents a blockchain with data, timestamp and hash."

    def __init__(self):
        self.blocks = []
        self.generate_genesis_block()

    def get_blockchain(self):
        return self.blocks[:]

    def latest_hash(self):
        return self.blocks[-1]

    def genesis_block(self):
        return self.blocks[0]

    def hash_block(self,data,timestamp,index,prev_hash):
        nonce = 0
        hash = ''
        while not self.validate_hash(hash):
            block = '{}:{}:{}:{}:{}'.format(
                data, timestamp, prev_hash, index, nonce
            )
            hash = hashlib.sha256(block.encode()).hexdigest()
            nonce += 1
        print('[nonce]', nonce)
        self.blocks.append(hash)

    def generate_genesis_block(self):
        data = 'Genesis block'
        timestamp = datetime.utcnow().timestamp()
        prev_hash = 0
        index = 0
        self.hash_block(data,timestamp, prev_hash, index)

    def validate_hash(self, hash):
        # We can increase de dificulty by increasing the number of zeroes
        return hash.startswith('00') & hash.endswith('00')

    def add_block(self,data):
        prev_hash = self.latest_hash()
        index = len(self.blocks) + 1
        timestamp = datetime.utcnow().timestamp()
        self.hash_block(data,timestamp,prev_hash,index)
