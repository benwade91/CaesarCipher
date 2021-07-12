alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def start():
    direction = input("Type '1' to encrypt, type '2' to decrypt:\n")
    text = raw_input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    encrypt(shift, direction, text)
    prompt()


def split(word):
    return [char for char in word]

def encrypt(shift, direction, text):
    if shift > 25:
        shift = shift % 25
    if(direction == 2):
        shift *= -1

    letter_arr = split(text)
    for i in range(len(text)):
        if text[i] in alphabet:
            index_to_change = alphabet.index(letter_arr[i]) + shift
            if(index_to_change > 25):
                index_to_change -= 26
            elif(index_to_change < 0):
                index_to_change += 26
            letter_arr[i] = alphabet[index_to_change]
    print(''.join(letter_arr))

def prompt():
    again = str(raw_input("Would you like to keep encrypting? 'yes' or 'no'?\n").lower())
    if again == 'yes':
        start()

start()
