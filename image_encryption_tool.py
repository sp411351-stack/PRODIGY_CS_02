from PIL import Image
import random

def encrypt_image(input_path, output_path, key):
    # Open the image
    img = Image.open(input_path)
    img = img.convert("RGB")  # Ensure image is in RGB mode
    pixels = list(img.getdata())

    # Set random seed for reproducibility
    random.seed(key)

    # Apply XOR operation to each pixel
    encrypted_pixels = [(r ^ key, g ^ key, b ^ key) for (r, g, b) in pixels]

    # Shuffle pixels using key
    random.shuffle(encrypted_pixels)

    # Create a new image and save
    encrypted_img = Image.new(img.mode, img.size)
    encrypted_img.putdata(encrypted_pixels)
    encrypted_img.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

def decrypt_image(input_path, output_path, key):
    # Open the encrypted image
    img = Image.open(input_path)
    img = img.convert("RGB")
    pixels = list(img.getdata())

    # Set random seed again for reproducibility
    random.seed(key)

    # Reverse shuffle
    # To reverse shuffle, we store the original indices after shuffling
    indices = list(range(len(pixels)))
    random.shuffle(indices)
    decrypted_pixels = [0] * len(pixels)
    for i, idx in enumerate(indices):
        decrypted_pixels[idx] = pixels[i]

    # Reverse XOR operation
    decrypted_pixels = [(r ^ key, g ^ key, b ^ key) for (r, g, b) in decrypted_pixels]

    # Create new image and save
    decrypted_img = Image.new(img.mode, img.size)
    decrypted_img.putdata(decrypted_pixels)
    decrypted_img.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

# Example usage:
key = 123  # Secret key (any integer)
encrypt_image("sample_image.jpg", "encrypted_image.png", key)
decrypt_image("encrypted_image.png", "decrypted_image.png", key)