import sys
morse_code = {
    'a': '.-',
    'b': '-...', 
    'c': '-.-.', 
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ' ': '/',
    '.': '.-.-.-',
    ',': '--..-- ',
    '!': '-.-.--',
    '?': '..--..'
}

def ask_for_inut():
    choice = input('Do you have a message to translate? (y/n): ')
    if choice == 'n':
        sys.exit()
    elif choice == 'y':
        ask_for_message()
    else:
        print('Invalid input, please try again.')
    ask_for_inut()

def ask_for_message():
    message = input('What is your message? ')
    to_morse_code(message)

def to_morse_code(message):
    characters = list(message)
    try:
        translated_morse_code = [morse_code[char.lower()] for char in characters]
    except KeyError:
        print('Invalid character, please try again')
        ask_for_message()
    else:
        morse_code_message = ' '.join(translated_morse_code)
        print(morse_code_message)

if __name__ == '__main__':
    ask_for_inut()
