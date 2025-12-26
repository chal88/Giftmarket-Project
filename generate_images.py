from PIL import Image
import os

# Folder where product images will go
media_path = 'media/products/'
os.makedirs(media_path, exist_ok=True)

# Define some sample image names
image_names = ['product1.jpg', 'product2.jpg', 'product3.jpg']

# Create small dummy images
for name in image_names:
    img = Image.new('RGB', (200, 200), color=(150, 200, 255))  # light blue
    img.save(os.path.join(media_path, name))

print("Dummy product images created!")
