from PIL import Image
from itertools import cycle

def xor(a, b):
    return [i ^ j for i, j in zip(a, cycle(b))]

def decrypt_image(encrypted_data, key_path):
    try:
        # Read the key from the "enc.txt" file
        with open(key_path, "rb") as key_file:
            key = key_file.read()

        # Perform XOR operation with the key
        decrypted_data = bytearray(xor(encrypted_data, key))

        # Create a new image from the decrypted data
        decrypted_image = Image.frombytes("RGB", (encrypted_data[16], encrypted_data[20]), bytes(decrypted_data))

        # Save the decrypted image
        decrypted_image.save("decrypted_image.png")
        print("Decrypted image saved as decrypted_image.png")
    except Exception as e:
        print(f"Error decrypting the image: {e}")

# Read the encrypted data from the "enc.txt" file
with open("enc.txt", "rb") as enc_file:
    encrypted_data = enc_file.read()

# Specify the path to the key file (if different from "enc.txt")
key_path = "enc.txt"

# Decrypt the image
decrypt_image(encrypted_data, key_path)
