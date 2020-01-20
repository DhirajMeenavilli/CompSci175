"""
Title: Decipher
Date: 01-20-2020
Authour: Dhiraj Meenavilli
"""

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def getInputFile():
    fileName = input("Enter the input filename: ")
    fileGiven = False

    while not fileGiven:
        try:
            file = open(fileName, 'r')
            fileGiven = True
        except:
            fileName = input('Invalid filename extension.  Please re-enter the input filename:')

    file = file.read()
    return file

def decrypt(message):
    letters = []
    placement = []
    decryptedMess = []

    message = message.split()

    key = message[0]

    message.pop(0)
    for i in range(len(message)):
        message[i] = message[i].lower()

    for i in range(len(message)):
        for j in range(len(message[i])):
            letters.append(message[i][j])
        letters.append(" ")

    for i in range(len(letters)):
        try:
            placement.append(alphabet.index(letters[i])-int(key))
        except:
            placement.append(" ")

    for i in range(len(placement)):
        try:
            decryptedMess.append(alphabet[placement[i]])
        except:
            decryptedMess.append(" ")

    decryptedMess = "".join(decryptedMess)
    return  decryptedMess

encryptedMess = getInputFile()
decrypted = decrypt(encryptedMess)
print("The decrypted message is:")
print(decrypted)

