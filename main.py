import numpy as np
from numpy.linalg import inv

# Get the users Input

input = raw_input('Message to Encrypt:')
input = input.lower()
originalMessage = []
for character in input:
  number = ord(character) - 96
  originalMessage.append(number)

input = raw_input('Establish your decryption Key:')
input = input.lower()
encryptKey = []
for elements in  input:
	intermediate = ord(elements) - 96
	encryptKey.append(intermediate)

# Get the length of input
inputLen = len(originalMessage)

ceilInt = np.int(np.ceil(np.sqrt(inputLen)))**2

# Modulo, this is our n in nXn
modHelper = np.sqrt(ceilInt)

rows, cols = np.int(modHelper), np.int(modHelper)
messageEncrypt = np.zeros(shape=(rows, cols))
encryptMatrix = np.zeros(shape=(rows, cols)) 

# Append our values in our created matrix
for (i, v) in zip(range(0, len(originalMessage)), originalMessage):
	r, c = i / cols, i % cols
	messageEncrypt[r, c] = v

# Create our encryptionKey Matrix
for (i, v) in zip(range(0, len(encryptKey)), encryptKey):
	r, c = i / cols, i % cols
	encryptMatrix[r, c] = v

# Calculate the inverse matrix for our decrypt key
print 'Our initial matrix is:'
print messageEncrypt
print 'Our encrypt matrix is:'
print encryptMatrix

# Multiply our message by our encrypt key
encryptedMessage = np.dot(messageEncrypt, encryptMatrix)
print 'Our encrypted message is:'
print encryptedMessage

# Inverse the encryption key for awesomeness
decryptionKey = inv(np.matrix(encryptMatrix))
print 'Our decryption key is:'
print decryptionKey

# Our decrypted matrix is
decryptedMessage = np.dot(encryptedMessage, decryptionKey)
print 'Our decrypted message is:'
print decryptedMessage