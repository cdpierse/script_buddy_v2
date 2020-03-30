import PIL
from PIL import Image, ImageDraw, ImageFont
from utils import load_model, generate

img = Image.new('RGB', (500, 650), color = 'white')

d = ImageDraw.Draw(img)
font = ImageFont.truetype("Courier New.ttf", 12)
model, tokenizer = load_model()

string = generate(model,tokenizer,max_length= 400)[0]
d.text((0,0), string, fill=(0,0,0), font= font)

img.save('script_output.png', dpi =(460,460))
