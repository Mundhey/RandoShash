import hashlib
import random


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


    def new_block(self):
        #Create a new block and add to chain
        pass


    def new_transaction(self):
        #add a new transaction to list of transaction
        pass


    @staticmethod
    def hash(block):
        #hashes a block

        pass


    @property
    def last_block(self):
        #returns last block in chain

        pass








