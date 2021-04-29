from caesar_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(plain_text, shift_number, direction):
    result = ""
    max_alphabet_index = len(alphabet) - 1
    if direction in "encode" or direction in "decode":
        for char in plain_text:
            shifted_letter_index = 0
            if char in alphabet:
                if direction == 'encode':
                    shifted_letter_index = alphabet.index(char) + shift_number
                    if shifted_letter_index > max_alphabet_index:
                        shifted_letter_index = shifted_letter_index - max_alphabet_index - 1
                elif direction == 'decode':
                    shifted_letter_index = alphabet.index(char) - shift_number
                    if shifted_letter_index < 0:
                        shifted_letter_index = max_alphabet_index + shifted_letter_index + 1

                result += alphabet[shifted_letter_index]
            else:
                result += char
        print(f"The {direction}d is: [{result}]")

    else:
        print(f"Incorrect choice of the direction: [{direction}]")


try_more = True

while try_more:
    print(logo)
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(plain_text=text, shift_number=shift, direction=direction)

    go_again_answer = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()
    if go_again_answer == "no":
        try_more = False
        print("Goodbye")
