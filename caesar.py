import string

def alphabet_position(letter):
    alphabet = string.ascii_lowercase
    char = letter.lower()
    position = alphabet.index(char)
    return position


def rotate_character(char, rot):
    alphabet = string.ascii_lowercase
    rotated_index = alphabet_position(char) + rot
    if rotated_index < 26:
        rot_char = alphabet[rotated_index]
    else:
        rot_char = alphabet[rotated_index % 26]
    return rot_char

def encrypt(message, rot):
    alphabet = string.ascii_lowercase
    encrypted = ''
    for char in message:
        if char.isalpha() == True:
            if char.isupper() == True:
                encrypted += rotate_character(char, rot).upper()
            else:
                encrypted += rotate_character(char, rot)
        else:
            encrypted += char
    return encrypted
