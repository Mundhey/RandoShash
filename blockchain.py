#Blockchain ASIC Resistance


#Previous POW Algorithms
#SHA256 for Bitcoin (Potential ASIC efficiency gain ~ 1000X)
#Scrypt for Litecoin (Potential ASIC efficiency gain ~ 1000X)
#Ethash for Etherium (Potential ASIC efficiency gain ~ 2X)
#X16R   for Ravecoin (Potential ASIC efficiency gain ~ 1000X)
#Equihas for Zcash (Potential ASIC efficiency gain ~ 100X)




#Proposed Algorithm Approach
#use a sequence of hashing algorithms where the output of onebecomes the input to the next
#The fixed order of hashing algorithms lends itself to the construction of ASICs
#While chaining more algorithms together adds difficulty in constructing an ASIC
#We can randomize ordering based on the hash of the previous block


import hashlib


a="Hello world"
byte_encode=str.encode(a)
hashobject=hashlib.sha256(byte_encode)
print(hashobject.hexdigest())
byte_decode=byte_encode.decode()
print(byte_encode)
print(hashlib.algorithms_available)

#Hash of Bitcoin block mined on 21/2/2019

abc="00000000000000000002a0fa3eb60b3be73ae5715c459384ef5e4de6fdc3a1d7"

abc_byte_encode=str.encode(abc)

print(abc_byte_encode)


# SHA512

sha512_hashobject=hashlib.sha512(abc_byte_encode)



# SHA256

sha256_hashobject=hashlib.sha256(str.encode(sha512_hashobject.hexdigest()))

print(sha256_hashobject)



# MD5

md5_hashobject=hashlib.md5(str.encode(sha256_hashobject.hexdigest()))

print("MD5 \n ",md5_hashobject.hexdigest())




