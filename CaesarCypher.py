def encrypt(text, level):
    encryptedText = " "

    # Visits all letters in the text
    for i in range(len(text)):
        #Check letter by letter
        char = text[i]

        #Check if it is UpperCase or LowerCase
        if(char.isupper()):
            encryptedText += chr((ord(char) + level - 65) % 26 + 65)
        else:
            encryptedText += chr((ord(char) + level - 97) % 26 + 97)
    return encryptedText

# Introducing the text to cypher
text = input("Type the text to encrypt: ")
# Introducing the level of the cypher
level = int(input("Please, state the level of encryption: "))

# Print the text that the user gave
print("The Original Text is: " + text)
# Print the level of encryption (how many movement of letters will be)
print("The level of encryption is: " + str(level))
# Print the encrypted message
print("The encrypted text is: " + encrypt(text,level))
