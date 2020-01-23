#Shift Cypher set to 13 by default / Caesar's Cypher

abc="abcdefghijklmnopqrstuvwxyz"

def encrypt(s, shift=13): #Loop every char from the word  shifted
    encrypted_str=""
    for c in s: 
        index = abc.index(c) 
        shifted_index =(index + shift) % len(abc)
        encrypted_str += abc[shifted_index]
    return encrypted_str   


def decrypt(e, shift=13):
    decrypted_str=""
    for c in e:
        index = abc.index(c)
        shifted_index = (index-  shift) % len(abc)
        decrypted_str += abc[(shifted_index)]
    return decrypted_str    


encrypted_value=encrypt("helloworld")
decrypted_value=decrypt(encrypted_value)

print(encrypted_value)
print(decrypted_value)