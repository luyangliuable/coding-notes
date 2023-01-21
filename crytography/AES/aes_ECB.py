import os
import struct
import sys
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding


def encrypt_image_ecb(image_file, key, output_file):
    # Read the image file into a bytes object
    with open(image_file, "rb") as f:
        image_data = f.read()

    # Convert the key to bytes and pad it to the correct length
    key = key.encode()
    key = key.ljust(32, b'\0')

    # Create a cipher object and encrypt the image
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()

    # Add padding to the image data
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(image_data) + padder.finalize()

    # Encrypt the padded data
    encrypted_image = encryptor.update(padded_data) + encryptor.finalize()

    # Write the encrypted image to the output file
    with open(output_file, "wb") as f:
        f.write(encrypted_image)

def decrypt_file_ecb(file, key, output):
    # Read the file
    with open(file, 'rb') as f:
        image_data = f.read()

    # Convert key to bytes
    key = key.encode()
    key = key.ljust(32, b'\0');

    # Create block cipher to decrypt
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    descryptor = cipher.decryptor()

    # Descrupt
    decrypted_file_content = descryptor.update(image_data) + descryptor.finalize()

    # Save file
    with open(output, 'wb') as f:
        f.write(decrypted_file_content);

if __name__ == '__main__':
    mode = sys.argv[1]
    file = sys.argv[2]
    output = sys.argv[3]

    if mode == 'encrypt':
        encrypt_image_ecb(file, "mysecretkey", output)
    elif mode == 'decrypt':
        decrypt_file_ecb(file, "mysecretkey", output)
