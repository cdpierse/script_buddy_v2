import PIL
from PIL import Image, ImageDraw, ImageFont
import json
import os
def generate_media(sample):
    font = ImageFont.truetype("fonts/cour.ttf", 60)
    img = Image.open(os.path.join("images","paper.png"))

    d = ImageDraw.Draw(img)


    d.text((0,0), sample,(0,0,0),font= font,quality =20)

    img.save(os.path.join('images','script_output.jpeg'),quality =90, optimize= True)



generate_media("test")
