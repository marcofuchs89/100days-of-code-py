from art import logo

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def caesar(message, shift_amount, cipher_method):
    new_message = ""
    if cipher_method == "decode":
        shift_amount *= -1
    for letter in message:
        if letter in alphabet:
            position = alphabet.index(letter)
            shifted_position = (position + shift_amount) % len(alphabet)
            new_message += alphabet[shifted_position]
        else:
            new_message += letter
    print(f"The {cipher_method}d text is: {new_message}")


if __name__ == "__main__":
    print(logo)
    run_again = True
    while run_again is True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))

        caesar(message=text, shift_amount=shift, cipher_method=direction)
        start_over = input("Do you want to start over? (Yes/No)").lower()
        if start_over == 'no':
            run_again = False
