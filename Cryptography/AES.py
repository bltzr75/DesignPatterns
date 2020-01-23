# Key must be in 16, 24, 32 bytes long
# test should be in bultiples of 16 bytes

from Crypto.Cipher import AES
key= "Sexteen byte key"
plain = "Secrets 16 bytes"
Cipher= AES.new(key)
ciphertext = Cipher.encrypt(plain)
plaintext=Cipher.decrypt(ciphertext)

print(" Plain Text is: ", plain, "\n" )
print(" The 16 bytes key will be: ", key, "\n"  )
print(ciphertext, "\n" )
print(" In Hexadecimal would be:", ciphertext.hex(), "\n" )
print(plaintext, "\n" )
print(" Once again we've got: ", plaintext )