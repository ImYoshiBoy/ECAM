from PIL import Image, ImageDraw

width = 450
height = 300

img = Image.new('RGB', (width, height), color='white')

lgbt_colors = [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 128, 0), (0, 0, 255), (128, 0, 128)]

draw = ImageDraw.Draw(img)

stripe_height = height // len(lgbt_colors)

for i, color in enumerate(lgbt_colors):
    y0 = i * stripe_height
    y1 = (i + 1) * stripe_height
    draw.rectangle([0, y0, width, y1], fill=color)

img.show()
# img.save('lgbt_flag.png')
