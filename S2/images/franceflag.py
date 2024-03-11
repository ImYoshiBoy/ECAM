#flags
#FRANCE
# Import the library we will use to manipulates images
from PIL import Image, ImageDraw

# Creation of an RGB 300x300 pixels images
img = Image.new("RGB", (300, 200))
draw = ImageDraw.Draw(img)

for x in range(300):
    for y in range(200):

        if x<100:
            img.putpixel((x, y), (0, 0, 255))
        elif x<200 and x>100:
            img.putpixel((x, y), (255, 255, 255))
        else:
            img.putpixel((x, y), (255))



img.show()