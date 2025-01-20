# Caesar Cipher Program

## Overview
This program implements the Caesar Cipher, a substitution cipher used to encode and decode messages by shifting letters of the alphabet. It supports encoding and decoding based on user input while preserving non-alphabet characters, spaces, and numbers.

---

## Features

- **Encode Messages:** Encrypt text by shifting letters forward by a specified number of positions.
- **Decode Messages:** Decrypt text by reversing the shift applied during encoding.
- **Interactive CLI:** Users can input text, specify a shift value, and choose encoding/decoding.
- **Preserves Non-Alphabet Characters:** Spaces, punctuation, and numbers remain unchanged.

---

## Technologies Used

- **Python:** Utilizes lists, strings, and control flow structures for functionality.

---

## Code Overview

### Alphabet List
The alphabet list contains all lowercase English letters.

```python
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
```

### Caesar Cipher Function
Handles both encoding and decoding by shifting letters based on the user-specified mode.

```python
def caesar_cipher(text, shift, mode):
    result = ""
    for letter in text:
        if letter in alphabet:
            shift_direction = shift if mode == "encode" else -shift
            new_position = (alphabet.index(letter) + shift_direction) % len(alphabet)
            result += alphabet[new_position]
        else:
            result += letter
    print(f"Here is the {mode}d result: {result}")
```

### Main Program
Runs an interactive loop until the user chooses to quit.

```python
while True:
    direction = input("Type 'encode' to encrypt, 'decode' to decrypt, or 'quit' to exit:\n").lower()
    if direction == "quit":
        print("Goodbye!")
        break
    elif direction in ["encode", "decode"]:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n")) % len(alphabet)
        caesar_cipher(text, shift, direction)
    else:
        print("Invalid input. Please type 'encode', 'decode', or 'quit'.")
```

---

## Example Usage

1. **Encode a Message:**
   - Input:
     ```
     Type 'encode' to encrypt, type 'decode' to decrypt, or 'quit' to exit:
     encode
     Type your message:
     hello world
     Type the shift number:
     5
     ```
   - Output:
     ```
     Here is the encoded result: mjqqt btwqi
     ```

2. **Decode a Message:**
   - Input:
     ```
     Type 'encode' to encrypt, type 'decode' to decrypt, or 'quit' to exit:
     decode
     Type your message:
     mjqqt btwqi
     Type the shift number:
     5
     ```
   - Output:
     ```
     Here is the decoded result: hello world
     ```

3. **Exit the Program:**
   - Input:
     ```
     Type 'encode' to encrypt, type 'decode' to decrypt, or 'quit' to exit:
     quit
     ```
   - Output:
     ```
     Goodbye!
     ```

---

## Improvements

- Add support for uppercase letters.
- Support custom alphabets or character sets.
- Create a graphical or web-based interface.

