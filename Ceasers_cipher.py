alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar_cipher(text, shift, mode):
    result = ""
    for letter in text:
        if letter in alphabet:
            shift_direction = shift if mode == "encode" else -shift
            new_position = (alphabet.index(letter) + shift_direction) % len(alphabet)
            result += alphabet[new_position]
        else:
            # Keep spaces, punctuation, or numbers unchanged
            result += letter
    print(f"Here is the {mode}d result: {result}")

# Main program
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, or 'quit' to exit:\n").lower()
    if direction == "quit":
        print("Goodbye!")
        break
    elif direction in ["encode", "decode"]:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift %= len(alphabet)  # Ensure shift is within range of the alphabet
        caesar_cipher(text, shift, direction)
    else:
        print("Invalid input. Please type 'encode', 'decode', or 'quit'.")
