from PIL import Image

def encrypt_image(image_path, key):
    # Open image
    img = Image.open(image_path)
    pixels = img.load()  # Access pixels
    

    print(f"size : {img.size[1]}")

    # Encrypt by manipulating pixels
    for i in range(img.size[0]):  # Width
        for j in range(img.size[1]):  # Height
           
            key = key + 97

            # print("pixel i,j : ", pixels[i, j])
           
            r, g, b ,a = pixels[i, j]

            # Simple encryption: add the key to RGB values and modulo 256
            # print("working on encryption...")
            pixels[i, j] = ((r + key) % 256, (g + key) % 256, (b + key) % 256, 255)
    
    # Save encrypted image
    img.save("encrypted_image.png")
    print("Image encrypted and saved as 'encrypted_image.png'")

def decrypt_image(image_path, key):
    # Open encrypted image
    img = Image.open(image_path)
    pixels = img.load()
    
    # Decrypt by reversing the pixel manipulation
    for i in range(img.size[0]):
        for j in range(img.size[1]):

            key = key + 97 

            r, g, b ,a = pixels[i, j]
            # Subtract the key and modulo 256 to decrypt
            

            pixels[i, j] = ((r - key) % 256,
                             (g - key) % 256, 
                             (b - key) % 256,
                             255)
    
    # Save decrypted image
    img.save("decrypted_image.png")
    print("Image decrypted and saved as 'decrypted_image.png'")

# Example usage
image_path = "image.png"  # Path to your image
key = 3  # Example key (encryption key)
encrypt_image(image_path, key)
decrypt_image("encrypted_image.png", key)
