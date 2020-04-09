#!/usr/bin/env python3

from ast import literal_eval as make_tuple
from PIL import Image, ImageDraw

f = open('ps.txt', 'r')
points = [make_tuple(line) for line in f.readlines()]
f.close()

image = Image.new('RGB', (270, 270), '#ffffff')
draw = ImageDraw.Draw(image)

for point in points:
	draw.point(point, fill="#000000")

image.save('qrcode.png')
