from PIL import Image

# Create a 300x300 gray placeholder image
img = Image.new('RGB', (300, 300), color=(200, 200, 200))

# Save the image to the static/images folder
img.save('static/images/default.png')

print("Default placeholder image created at static/images/default.png")
