from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
max_position = len(alphabet) - 1

def caesar(start_text, shift_amount, cipher_direction):
    """
    Function which encode / decode input text by shifting their letters.
    Numbers and blank spaces in text won't be changed.
    """
    end_text = ""
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            if direction == 'encode':
                diff = (position + shift_amount) - max_position
                if diff > 0:
                    new_position = diff - 1
                else:
                    new_position = position + shift_amount
            elif direction == 'decode':
                new_position = position - shift_amount

            end_text += alphabet[new_position]

        else:
            end_text += char

    print(f"Here's the {cipher_direction}d result: {end_text}")

print(logo)

should_continue = True
while should_continue:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # correct shift amount if it's greater than the length of the alphabet
    shift = shift % len(alphabet)

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    result = input("\nType 'yes' if you want to go again. Otherwise type 'no':\n")
    if result == 'no':
        should_continue = False
        print("Goodbye!")