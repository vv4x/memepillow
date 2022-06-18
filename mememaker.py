#bottomtext3
from PIL import Image, ImageFilter, ImageOps, ImageDraw, ImageFont
from io import BytesIO

#rawtext = input('what bottomtext: ')
rawtext_top = input("toptext: ")
rawtext_bottom = input("bottomtext: ")
path = input("path: ")
path_s = input("save path: ")

text_t = rawtext_top.upper()
text_b = rawtext_bottom.upper()


image = Image.open(path)
draw = ImageDraw.Draw(image)

with Image.open(path) as img:
    width, height = img.size

textsize = (height // 10)
strokesize = (height // 200)

font = ImageFont.truetype('impact.ttf', size = textsize)

draw.text((width // 2, height / 35),text_t, font = font, fill = (0,0,0), align = 'center', anchor = 'mt', stroke_width = strokesize, stroke_fill = (255,255,255))
draw.text((width // 2, height - textsize ),text_b, font = font, fill = (0,0,0), align = 'center', anchor = 'mt', stroke_width = strokesize, stroke_fill = (255,255,255))

image.save(path_s)

