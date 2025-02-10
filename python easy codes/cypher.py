def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    for char in text:
        if char.isalpha():
            shift_amount = shift if mode == 'encrypt' else -shift
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift_amount) % 26 + start)
        else:
            result += char
    return result

# Example usage
text = input("Enter text: ")
shift = int(input("Enter shift value: "))
mode = input("Enter mode (encrypt/decrypt): ").strip().lower()

output = caesar_cipher(text, shift, mode)
print("Result:", output)
