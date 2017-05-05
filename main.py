import numpy as np
from numpy.linalg import inv

originalMessage = []
encryptKey = []


def get_user_input(value, msg):
    input = raw_input(msg)
    input = input.lower()
    for character in input:
        number = ord(character) - 96
        value.append(number)

get_user_input(originalMessage, 'Enter Message to Encrypt')
get_user_input(encryptKey, 'Enter decryption Key')

# Get the length of input
inputLen = len(originalMessage)
ceilInt = np.int(np.ceil(np.sqrt(inputLen)))**2

# Modulo, this is our n in nXn
modHelper = np.sqrt(ceilInt)
rows, cols = np.int(modHelper), np.int(modHelper)


# Create our empty matrix and fill it with our values
def build_matrix(matrix):
    # Create matrix
    value = np.zeros(shape=(rows, cols))

    # Append our values
    for (i, v) in zip(range(0, len(matrix)), matrix):
        r, c = i / cols, i % cols
        value[r, c] = v

    return value

originalMessage = build_matrix(originalMessage)
encryptKey = build_matrix(encryptKey)

# Multiply our message by our encrypt key
encryptedMessage = np.dot(originalMessage, encryptKey)
print(encryptedMessage)

# Inverse the encryption key for awesomeness
decryptionKey = inv(np.matrix(encryptKey))
print(decryptionKey)

# Our decrypted matrix is
decryptedMessage = np.dot(originalMessage, decryptionKey)
print(decryptedMessage)
