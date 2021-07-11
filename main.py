alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

direction = input("Type '1' to encrypt, type '2' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def split(word):
    return [char for char in word]

def encrypt(shift):
    if(direction == 2):
        shift = 0-shift
    word = split(text)
    for i in range(len(text)):
        index_to_change = alphabet.index(word[i]) + shift
        if(index_to_change > 26):
            index_to_change -= 27
        elif(index_to_change < 0):
            index_to_change += 27
        word[i] = alphabet[index_to_change]
    print(''.join(word))
encrypt(shift)
