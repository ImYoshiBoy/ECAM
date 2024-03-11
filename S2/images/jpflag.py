from PIL import Image, ImageDraw

# Creation of an RGB 300x300 pixels images
img = Image.new("RGB", (300, 200))
draw = ImageDraw.Draw(img)

for x in range(300):
    for y in range(200):
            img.putpixel((x, y), (255, 255, 255))
    
            if (x - 150)**2 + (y - 100)**2 <= 60**2:
                img.putpixel((x, y), (255))


img.show()