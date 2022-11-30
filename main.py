from PIL import Image, ImageDraw

image = Image.new('L', (960, 540), 255)

draw = ImageDraw.Draw(image)

with open("DS5.txt") as file:
    for line in file:
        coordArray = line.split()
        draw.line((int(coordArray[1]), 540 - int(coordArray[0]), int(coordArray[1]) + 1, 540 - (int(coordArray[0]) + 1)))

image.show()
del draw
image.save("DS5.jpeg", "JPEG")
