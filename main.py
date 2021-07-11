alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def split(word):
    return [char for char in word]

def encrypt():
    word = split(text)
    for i in range(len(text)):
        index_to_change = alphabet.index(word[i])
        index_to_change += shift
        if(index_to_change > 25):
            index_to_change -= 26
        elif(index_to_change < 0):
            index_to_change += 26
        word[i] = alphabet[index_to_change]
    print(''.join(word))
encrypt()
