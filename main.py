import numpy as np
# from numpy.linalg import inv

# Get the users Input

input = raw_input('Message to Encrypt:')
input = input.lower()
originalMessage = []
for character in input:
  number = ord(character) - 96
  originalMessage.append(number)

print originalMessage

input = raw_input('Establish your decryption Key:')
input = input.lower()
encryptKey = []
for elements in  input:
	intermediate = ord(elements) - 96
	encryptKey.append(intermediate)

print encryptKey

# Get the length of input
inputLen = len(originalMessage)

ceilInt = np.int(np.ceil(np.sqrt(inputLen)))**2
print ceilInt

# Modulo, this is our n in nXn
modHelper = np.sqrt(ceilInt)

rows, cols = np.int(modHelper), np.int(modHelper)
matrix = np.zeros(shape=(rows, cols))
encryptMatrix = np.zeros(shape=(rows, cols)) 

# Append our values in our created matrix
for (i, v) in zip(range(0, len(originalMessage)), originalMessage):
	r, c = i / cols, i % cols
	matrix[r, c] = v
	encryptMatrix[r, c] = v

# Create our encryptionKey Matrix
for (i, v) in zip(range(0, len(encryptKey)), encryptKey):
	r, c = i / cols, i % cols
	encryptMatrix[r, c] = v
# Multiply our message by our encrypt key


# Calculate the inverse matrix for our decrypt key
print 'Our initial matrix is:'
print matrix
print 'Our encrypt matrix is:'
print encryptMatrix
