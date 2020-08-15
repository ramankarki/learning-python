# caesar cipher
symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz 1234567890!@#$%^&*()"
max_key_size = len(symbols) 


def get_mode():
    while True:
        print("Do you wish to encrypt or decrypt a message?")
        mode = input().lower()
        if mode in ["e", "encrypt", "d", "decrypt"]:
            return mode
        else:
            print("Enter either 'encrypt' or 'decrypt (e/d)")


def get_message():
    print("Enter your message:")
    return input()


def get_key():
    key = 0
    while True:
        print(f"Enter the max key number up to {max_key_size}")
        key = int(input())
        if key >= 1 and key <= max_key_size:
            return key


def get_translatd_message(mode, message, key):
    if mode[0] == "d":
        key = -key
    translated = ""

    for symbol in message:
        symbol_index = symbols.find(symbol)
        if symbol_index == -1:
            translated += symbol
        else:
            # encrypt or decrypt
            symbol_index += key
            if symbol_index > len(symbols):
                symbol_index -= len(symbols)
            elif symbol_index < 0:
                symbol_index += len(symbols)
            
            translated += symbols[symbol_index]

    return translated


mode = get_mode()
message = get_message()
key = get_key()
print("Your translated message:")
translated_message = get_translatd_message(mode, message, key)
print(translated_message)
