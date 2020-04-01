import PIL
from PIL import Image, ImageDraw, ImageFont
from utils import load_model, generate
import json
font = ImageFont.truetype("Courier New.ttf", 65)


with open('data/samples.json') as f:
    scripts = json.load(f)
string = scripts[10]
print(string)
imsize = font.getsize(string) 
img = Image.open('paper.png')

d = ImageDraw.Draw(img)


d.text((5,5), string,(0,0,0),font= font,)

img.save('script_output.png',quality =100, optimize= True)



