import hashlib
import random
from time import time


#fun_list=[hashlib.sha256,hashlib.sha512,hashlib.md5]

#Hash of Bitcoin block mined on 21/2/2019

#xyz="00000000000000000002a0fa3eb60b3be73ae5715c459384ef5e4de6fdc3a1d7"


#for _ in range(10):

#    xyz_binary=str.encode(xyz)
#    hash_object=random.choice(fun_list)(xyz_binary)
#    print(hash_object.hexdigest())
#    xyz=hash_object.hexdigest()



#Building a Blockchain

#creating blockchain class
class Blockchain(object):





    def __init__(self):

        self.chain=[]
        self.current_transactions=[]

        # Create the genesis block
        self.new_block(previous_hash=1, proof=100)





    def new_block(self, proof, previous_hash=None):
        #Create a new block and add to chain

        """
        Create a new Block in the Blockchain
        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash: (Optional) <str> Hash of previous Block
        :return: <dict> New Block
        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # Reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block





    def new_transaction(self,sender, recipient, amount):
        #add a new transaction to list of transaction

        """
                Creates a new transaction to go into the next mined Block
                :param sender: <str> Address of the Sender
                :param recipient: <str> Address of the Recipient
                :param amount: <int> Amount
                :return: <int> The index of the Block that will hold this transaction
        """

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1








    def proof_of_work(self, last_proof):
        """
        Simple Proof of Work Algorithm:
         - Find a number p' such that hash(pp') contains leading 4 zeroes, where p is the previous p'
         - p is the previous proof, and p' is the new proof
        :param last_proof: <int>
        :return: <int>
        """

        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validates the Proof: Does hash(last_proof, proof) contain 4 leading zeroes?
        :param last_proof: <int> Previous Proof
        :param proof: <int> Current Proof
        :return: <bool> True if correct, False if not.
        """

        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"



    @staticmethod
    def hash(block):
        #hashes a block
        """
                Creates a SHA-256 hash of a Block
                :param block: <dict> Block
                :return: <str>
                """

        # We must make sure that the Dictionary is Ordered, or we'll have inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()


    @property
    def last_block(self):
        #returns last block in chain
        return self.chain[-1]








abc=Blockchain()

