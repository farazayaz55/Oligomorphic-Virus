#!/usr/bin/env python
# coding: utf-8

# # Depicting Oligomorphic Viruses

# # Ciser Cypher
# 
# in Ciser Cypher we shift each letter by s letter </br>
# for example if you have letter 'a' and 's'=3 then the letter will become 'd' </br>
# so hello world  will become </br>
# khoorzruog
# 

# In[1]:


class CiserCipher:
    def encrypt(text,s):
        result = ""
        for i in range(len(text)):
            char = text[i]
            # Encrypt uppercase characters in plain text

            if (char.isupper()):
                result += chr((ord(char) + s-65) % 26 + 65)
            # Encrypt lowercase characters in plain text
            else:
                result += chr((ord(char) + s - 97) % 26 + 97)
        return result

    #decrypt is same as encrypt just Do the shift as 26-n
    def decrypt(text,s):
        result = ""
        s=26-s
        for i in range(len(text)):
            char = text[i]
            # Encrypt uppercase characters in plain text

            if (char.isupper()):
                result += chr((ord(char) + s-65) % 26 + 65)
            # Encrypt lowercase characters in plain text
            else:
                result += chr((ord(char) + s - 97) % 26 + 97)
        return result


# # Rot13
# ROT13  is also like ciser cypher we rotate(shift) each letter by 'shift' </br>
# if 'a' is letter and shift is of 1 then letter will become b</br>
# you must be wondering then it's ciser cypher what's new in it?</br>
# well the implementation is different in it</br>
# The approach is to use two separate python dictionaries. </br>
# First one to lookup the various letters according to their place in the English alphabets to get the shifted number</br>
# Second one to get the letters which correspond to those shifted numbers.</br>

# In[2]:


dict1 = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5,
        'F' : 6, 'G' : 7, 'H' : 8, 'I' : 9, 'J' : 10,
        'K' : 11, 'L' : 12, 'M' : 13, 'N' : 14, 'O' : 15,
        'P' : 16, 'Q' : 17, 'R' : 18, 'S' : 19, 'T' : 20,
        'U' : 21, 'V' : 22, 'W' : 23, 'X' : 24, 'Y' : 25, 'Z' : 26,
         
         
         'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5,
        'f' : 6, 'g' : 7, 'h' : 8, 'i' : 9, 'j' : 10,
        'k' : 11, 'l' : 12, 'm' : 13, 'n' : 14, 'o' : 15,
        'p' : 16, 'q' : 17, 'r' : 18, 's' : 19, 't' : 20,
        'u' : 21, 'v' : 22, 'w' : 23, 'x' : 24, 'y' : 25, 'z' : 26
        
        
        }


dict2 = {0 : 'Z', 1 : 'A', 2 : 'B', 3 : 'C', 4 : 'D', 5 : 'E',
        6 : 'F', 7 : 'G', 8 : 'H', 9 : 'I', 10 : 'J',
        11 : 'K', 12 : 'L', 13 : 'M', 14 : 'N', 15 : 'O',
        16 : 'P', 17 : 'Q', 18 : 'R', 19 : 'S', 20 : 'T',
        21 : 'U', 22 : 'V', 23 : 'W', 24 : 'X', 25 : 'Y',
        
        0 : 'z', 1 : 'a', 2 : 'b', 3 : 'c', 4 : 'd', 5 : 'e',
        6 : 'f', 7 : 'g', 8 : 'h', 9 : 'i', 10 : 'j',
        11 : 'k', 12 : 'l', 13 : 'm', 14 : 'n', 15 : 'o',
        16 : 'p', 17 : 'q', 18 : 'r', 19 : 's', 20 : 't',
        21 : 'u', 22 : 'v', 23 : 'w', 24 : 'x', 25 : 'y',
        
        }
class Rot13:
  

    # Function to encrypt the string
    # according to the shift provided
    def encrypt(message, shift):
            
        cipher = ''
        for letter in message:
            # checking for space
            if(letter != ' '):
                # looks up the dictionary and
                # adds the shift to the index
                num = ( dict1[letter] + shift ) % 26
                # looks up the second dictionary for
                # the shifted alphabets and adds them
                cipher += dict2[num]
            else:
                # adds space
                cipher += ' '

        return cipher

    # Function to decrypt the string
    # according to the shift provided
    def decrypt(message, shift):
        decipher = ''
        for letter in message:
            # checks for space
            if(letter != ' '):
                # looks up the dictionary and
                # subtracts the shift to the index
                num = ( dict1[letter] - shift + 26) % 26
                # looks up the second dictionary for the
                # shifted alphabets and adds them
                decipher += dict2[num]
            else:
                # adds space
                decipher += ' '

        return decipher
dict1 = {'A' : 1, 'B' : 2, 'C' : 3, 'D' : 4, 'E' : 5,
        'F' : 6, 'G' : 7, 'H' : 8, 'I' : 9, 'J' : 10,
        'K' : 11, 'L' : 12, 'M' : 13, 'N' : 14, 'O' : 15,
        'P' : 16, 'Q' : 17, 'R' : 18, 'S' : 19, 'T' : 20,
        'U' : 21, 'V' : 22, 'W' : 23, 'X' : 24, 'Y' : 25, 'Z' : 26,
         
         
         'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5,
        'f' : 6, 'g' : 7, 'h' : 8, 'i' : 9, 'j' : 10,
        'k' : 11, 'l' : 12, 'm' : 13, 'n' : 14, 'o' : 15,
        'p' : 16, 'q' : 17, 'r' : 18, 's' : 19, 't' : 20,
        'u' : 21, 'v' : 22, 'w' : 23, 'x' : 24, 'y' : 25, 'z' : 26
        
        
        }


dict2 = {0 : 'Z', 1 : 'A', 2 : 'B', 3 : 'C', 4 : 'D', 5 : 'E',
        6 : 'F', 7 : 'G', 8 : 'H', 9 : 'I', 10 : 'J',
        11 : 'K', 12 : 'L', 13 : 'M', 14 : 'N', 15 : 'O',
        16 : 'P', 17 : 'Q', 18 : 'R', 19 : 'S', 20 : 'T',
        21 : 'U', 22 : 'V', 23 : 'W', 24 : 'X', 25 : 'Y',
        
        0 : 'z', 1 : 'a', 2 : 'b', 3 : 'c', 4 : 'd', 5 : 'e',
        6 : 'f', 7 : 'g', 8 : 'h', 9 : 'i', 10 : 'j',
        11 : 'k', 12 : 'l', 13 : 'm', 14 : 'n', 15 : 'o',
        16 : 'p', 17 : 'q', 18 : 'r', 19 : 's', 20 : 't',
        21 : 'u', 22 : 'v', 23 : 'w', 24 : 'x', 25 : 'y',
        
        }


# # Tranposition Cipher
# https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_transposition_cipher.htm </br>
# in tranposition Cipher (columnar), we make matrix with now of columns=key </br>
# and no of rows=Ceiling(length of message/column) </br>
# so if you have hello world  </br>
# [ H e l l] </br>
# [o w o r] </br>
# [l d | |"] will look like this </br>

# In[3]:


class TranspositionCypher:
    def encrypt(key, message):
        ciphertext = [''] * key

        for col in range(key):
            position = col
            while position < len(message):
                ciphertext[col] += message[position]
                position += key
        return ''.join(ciphertext) #Cipher text

    def decrypt(key, message):
        numOfRows = math.ceil(len(message) / key)
        numOfColumns = key
        numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)
        plaintext = [''] * numOfRows
        col = 0
        row = 0

        for symbol in message:
            plaintext[row] += symbol
            col += 1
            if (col == numOfColumns) or (row == numOfRows - 1 and col >= numOfColumns - numOfShadedBoxes):
                col = 0 
                row += 1 
        return ''.join(plaintext)


# # Using sha-256 for Hashing

# In[4]:


import math
import hashlib
import random
import base64
import datetime
current_date = datetime.datetime.now()
current_time_in_seconds=int(current_date.strftime("%Y%m%d%H%M%S"))
transactionId = "07643622"
APIKey = "13f1fd1b-ab2d-4c1f-8e2c-ca61878f2a44"


# # Passing current time in Sha 256 to make hash unique Every time

# In[5]:


hash256 = bytes(str(current_time_in_seconds) + transactionId + APIKey,'utf-8')

def virus():
    return "HelloWorld";
    



# # we will have 3 encrpytor and decryptors

# we will generate a random number between 0 and 3  and decide which Encryptor / Decryptor to use this time </br>
# if rand num is 0 we will use ciser cypher  </br>
# if rand num is 1 we will use rot13 </br>
# if rand num is 2 we will TranspositionCypher  </br>

# In[6]:


if __name__ == "__main__":
    rand=random.randint(0,2) #random number
    print(rand)
    if(rand==0):
        encrypt=CiserCipher.encrypt(virus(),3)#Putting shift of ciser cypher to 3 always
        print("Encryption of ciser Cypher is ",encrypt)
        decrypt=CiserCipher.decrypt(encrypt,3)
        print("Decryption of Ciser Cypher is ",decrypt)

    if(rand==1):
        encrypt=Rot13.encrypt(virus(),3)
        print("Encryption of Rot-13 is ",encrypt)
        decrypt=Rot13.decrypt(encrypt,3)
        print("Decryption of Rot13 is ",decrypt)
        
    if(rand==2):
        encrypt=TranspositionCypher.encrypt(4,virus())
        print("Encryption of TranspositionCypher is ",encrypt)
        decrypt=TranspositionCypher.decrypt(4,virus())
        print("Decryption of TranspositionCypher is ",decrypt)
        
    #signaturing 
    #generate a hash based on sha-256 on the basis of current time so that hash is always unique
    #then generate a signature based on the hash


# # for Better depiction let's just show all cases when number is 0,1,2 of all algorithms

# In[7]:


encrypt=CiserCipher.encrypt(virus(),3)#Putting shift of ciser cypher to 3 always
print("Encryption of ciser Cypher is ",encrypt)
decrypt=CiserCipher.decrypt(encrypt,3)
print("Decryption of Ciser Cypher is ",decrypt)


# In[8]:


encrypt=Rot13.encrypt(virus(),3)
print("Encryption of Rot-13 is ",encrypt)
decrypt=Rot13.decrypt(encrypt,3)
print("Decryption of Rot13 is ",decrypt)


# In[9]:


encrypt=TranspositionCypher.encrypt(4,virus())
print("Encryption of TranspositionCypher is ",encrypt)
decrypt=TranspositionCypher.decrypt(4,virus())
print("Decryption of TranspositionCypher is ",decrypt)


# # signaturing

# generate a hash based on sha-256 on the basis of current time so that hash is always unique </br>
# then generate a signature based on the hash

# In[10]:


print("Hash is ",hash256)
signature =  base64.b64encode(hashlib.sha256(hash256).digest())
print("Signature is ",signature)

