# Import the library we will use to manipulates images
from PIL import Image, ImageDraw

# Creation of an RGB 300x300 pixels images
img = Image.new("RGB", (300, 300))
draw = ImageDraw.Draw(img)

# Loop over each pixel to initialize the colour of each of them
for x in range(300):
    for y in range(300):
        # gray_value = int(255 * (1 - y / 300))
        # img.putpixel((x, y), (gray_value, gray_value, gray_value))
        if ((x>=125 and x<=175) and (y>=125 and y<=175)):
            img.putpixel((x, y), (255))

        if (y<=3 or y>=297) or (x<=3 or x>=297):
            img.putpixel((x, y), (0, 0, 255))

img.show()
# We prefer images woth format .png which are less heavy than .jpg for what we are doing
# The difference is for transparent backgrounds, which we won't have.
