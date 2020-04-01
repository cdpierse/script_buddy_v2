import PIL
from PIL import Image, ImageDraw, ImageFont
from utils import load_model, generate
import json


def generate_media(sample):
    font = ImageFont.truetype("Courier New.ttf", 60)
    img = Image.open('images/paper.png')

    d = ImageDraw.Draw(img)


    d.text((0,0), sample,(0,0,0),font= font,quality =20)

    img.save('images/script_output.jpeg',quality =90, optimize= True)




