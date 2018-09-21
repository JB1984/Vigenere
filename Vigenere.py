
# Please watch the video at https://www.youtube.com/watch?v=0Pm2PrxmU38 for a very good explanation of what we are
# doing in this file in terms of decrypting a passage that has been encrypted using Vigenere cipher.

# This function takes the first key string (the "top" key) and then create the top line of our matrix which starts off
# with the key and then ends using all remaining letters of the alphabet. It is required that the key only use
# each letter of the alphabet once.
def createAlphabet(key1string):

    topAlphabet = alphabet
    counter = 0

    for letter in key1string:

        topAlphabet.remove(letter)

        topAlphabet.insert(counter, letter)

        counter += 1

    return topAlphabet

# This function takes the second key and creates each new line "underneath" the previous one, it also modulos through
# the the alphabet created by the createAlphabet function starting with the each letter in the string.
def createLines(key2string, myAlphabet):

    listOfAlphabets = []

    for letter in key2string:

        index = myAlphabet.index(letter)+1

        counter = 0

        lineAlphabet = []

        while counter <= 25:
            lineAlphabet.append(myAlphabet[index % len(myAlphabet)])
            index += 1
            counter += 1

        listOfAlphabets.append(lineAlphabet)

    return listOfAlphabets

# This function decrypts an encrypted passage by taking out "matrix" and the myAlphabet and looping through the matrix
# for each letter in our encrypted passage getting the index of that letter in the appropriate line of the matrix
# and then finding that index in out alphabet which is the decrypted letter.
def decryptPassage(passage, myAlphabet, myLines, key2string):

    decryptedPassage = []

    counter = 0

    for letter in passage:

        ourRow = myLines[counter]

        index = ourRow.index(letter) + 1

        decLetter = myAlphabet[index]

        decryptedPassage.append(decLetter)

        if counter < len(key2string)-1:
            counter += 1
        else:
            counter = 0

    return decryptedPassage


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

key1string = input("Enter first key: ")
key1string = key1string.lower()

myAlphabet = createAlphabet(key1string)

myAlphabetString = ''.join(myAlphabet)

print("Your alphabet line is: " + myAlphabetString)

key2string = input("Enter second key: ")
key2string = key2string.lower()

myLines = createLines(key2string, myAlphabet)

for line in myLines:

    lineSting = ''.join(line)
    print("Your lines are: " + lineSting)

encryptedPassage = input("Enter encrypted passage: ")
encryptedPassage = encryptedPassage.lower()

decryptedPassage = decryptPassage(encryptedPassage, myAlphabet, myLines, key2string)

decryptedPassageString = ''.join(decryptedPassage)

print("Your decrypted passage is: " + decryptedPassageString)