from Crypto.Cipher import AES

def paddedKey(key):
    while len(key) % 16 != 0:
        key+=' '
    return key

def paddedText(text):
    while len(text)% 16 != 0:
        text += ' '
    return text
            
plain_input = input("Enter in the text to be encrypted: ")
plain = paddedText(plain_input)

key_input = input("Enter in a key between 16 and 32 characters: ")
key = paddedKey(key_input)

if(len(key_input)<=16 & len(key_input)>=32):
       print("Key must be between 16 and 32 characters")
cipher = AES.new(key) 
ciphertext = cipher.encrypt(plain)
print("Encrypted textplain: ", ciphertext)
print("Hexadecimal: ", ciphertext.hex())
print("Cipher decrypted: ", cipher.decrypt(ciphertext))
