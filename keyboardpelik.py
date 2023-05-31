def decode_message(text):
    keyboard = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
    decoded_text = ""
    
    for char in text:
        if char == ' ':
            decoded_text += ' '
        elif char.isupper():
            index = keyboard.index(char.lower())
            decoded_text += keyboard[index - 1].upper()
        else:
            index = keyboard.index(char)
            decoded_text += keyboard[index - 1]
    
    return decoded_text

# Example usage
input_text = "O S, GOMR YPFSU/"
decoded_text = decode_message(input_text)
print(decoded_text)