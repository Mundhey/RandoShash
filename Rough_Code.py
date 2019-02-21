import hashlib
import random

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







def fun1():
    print("function 1")

def fun2():
    print("function 2")

def fun3():
    print("function 3")


my_list=[fun1,fun2,fun3]



random.choice(my_list)()







# Rough code

xyz="00000000000000000002a0fa3eb60b3be73ae5715c459384ef5e4de6fdc3a1d7"

hash_list=[hashlib.md5,hashlib.sha256,hashlib.sha512]

print(random.choice(hash_list)(str.encode(xyz)).hexdigest())

