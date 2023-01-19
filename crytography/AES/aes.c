#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <openssl/aes.h>

int main(int argc, char *argv[])
{
    // Check if enough arguments were passed
    if (argc != 4) {
        printf("Usage: %s <image_file> <key> <output_file>\n", argv[0]);
        return 1;
    }

    // Open the image file for reading
    FILE *image = fopen(argv[1], "rb");
    if (image == NULL) {
        printf("Error opening image file.\n");
        return 1;
    }

    // Get the size of the image file
    fseek(image, 0, SEEK_END);
    int imageSize = ftell(image);
    rewind(image);

    // Read the image file into a buffer
    unsigned char *imageBuffer = (unsigned char *)malloc(imageSize);
    fread(imageBuffer, 1, imageSize, image);
    fclose(image);

    // Set the key and iv
    unsigned char key[AES_BLOCK_SIZE];
    memset(key, 0, AES_BLOCK_SIZE);
    strncpy((char *)key, argv[2], AES_BLOCK_SIZE);

    unsigned char iv[AES_BLOCK_SIZE];
    memset(iv, 0, AES_BLOCK_SIZE);

    // Open the output file for writing
    FILE *output = fopen(argv[3], "wb");
    if (output == NULL) {
        printf("Error opening output file.\n");
        return 1;
    }

    // Encrypt the image
    AES_KEY aes_key;
    AES_set_encrypt_key(key, 128, &aes_key);
    AES_cbc_encrypt(imageBuffer, imageBuffer, imageSize, &aes_key, iv, AES_ENCRYPT);

    // Write the encrypted image to the output file
    fwrite(imageBuffer, 1, imageSize, output);
    fclose(output);

    // Clean up
    free(imageBuffer);

    return 0;
}
