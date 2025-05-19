def caesar_cipher(text, shift, mode='encrypt'):
    result = ""

    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            if mode == 'encrypt':
                result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            elif mode == 'decrypt':
                result += chr((ord(char) - shift_base - shift) % 26 + shift_base)
        else:
            result += char

    return result

# Example usage
message = input("Enter the message: ")
shift_value = int(input("Enter shift value: "))
mode = input("Enter mode (encrypt/decrypt): ").lower()

output = caesar_cipher(message, shift_value, mode)
print(f"Result: {output}")
