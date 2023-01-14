import base64

def encrypt(text):
    encoded_text = base64.b64encode(text.encode())
    decoded_text = base64.b64decode(encoded_text).decode()
    return encoded_text.decode(), decoded_text

text = "Hello World"
encoded_text, decoded_text = encrypt(text)
print("Encrypted text: ", encoded_text)
print("Decrypted text: ", decoded_text)
