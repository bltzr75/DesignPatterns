#Cryptography algorithms available

import hashlib, binascii

print("Algorithms Guaranteed Module: \n", hashlib.algorithms_guaranteed, "\n")
print("Algorithms Available Module: \n",  hashlib.algorithms_available, "\n \n")



md5 = hashlib.md5()

md5.update(b'Python') #//accepts bytes string
print(md5.digest())
print(md5.hexdigest())
sha = hashlib.sha1(b'Python').hexdigest()
print(sha)


hash = hashlib.md5(b"Helo Python!!!")
print("Hexadecimal: ", hash.digest(), "\n")
print("Byte String: ", hash.hexdigest(), "\n")
print("Block Size:", hash.block_size) #//Shows the block size of the algorithm
print("Digest Size:", hash.digest_size) #//Shows the block size of the algorithm
hash1 = hashlib.sha512(b'Hello World')
print(hash1.block_size)
print("Block Size:",hash1.digest_size,  "\n \n")



print('SHA', "\n")
hashed_string = hashlib.sha512(b'Hello World!')
hex_digest = hashed_string.hexdigest()
print("Hexadecimal: ", hex_digest, "\n")
digest= hashed_string.digest()
print("Byte String: ", digest,  "\n \n")


print('blake2s256', "\n")
hash1 = hashlib.new('blake2s256')
hash1.update(b'Python is the best!')
(hash1.digest_size)


print('sha512', "\n")
hash = hashlib.pbkdf2_hmac('sha512', b'Super secret', b'saltthepassword', 10000) #//password based key derivated function
binascii.hexlify(hash)
print(hash,  "\n \n")


print('RPMD', "\n")
hash = hashlib.new('ripemd160') #Right PMD
hash.update(b'Python is the best!')
print("Hexadecimal: ", hash.digest(), "\n")
print("Byte String: ", hash.hexdigest(), "\n")
print("Block Size:", hash.block_size, "\n") #//Shows the block size of the algorithm
print("Digest Size:", hash.digest_size, "\n") #//Shows the block size of the algorithm
