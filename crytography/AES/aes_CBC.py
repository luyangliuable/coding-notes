import os
import struct
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

def encrypt_image(image_file, key, output_file):
    # Read the image file into a bytes object
    with open(image_file, "rb") as f:
        image_data = f.read()

    # Convert the key to bytes
    key = key.encode()

    # Pad the key to the correct length
    key = key.ljust(32, b'\0')

    # Create a cipher object and encrypt the image
    cipher = Cipher(algorithms.AES(key), modes.CBC(b'\0' * 16), backend=default_backend())
    encryptor = cipher.encryptor()

    # Add padding to the image data
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(image_data) + padder.finalize()

    # Encrypt the padded data
    encrypted_image = encryptor.update(padded_data) + encryptor.finalize()

    # Write the encrypted image to the output file
    with open(output_file, "wb") as f:
        f.write(encrypted_image)

encrypt_image("test_file.txt", "mysecretkey", "output.txt")
