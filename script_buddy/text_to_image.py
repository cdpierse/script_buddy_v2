import PIL
from PIL import Image, ImageDraw, ImageFont
from utils import load_model, generate

model, tokenizer = load_model()
font = ImageFont.truetype("Courier New.ttf", 65)
string = generate(model,tokenizer,input_text="       He pulls his loaded gun out", max_length=1000)[0]
imsize = font.getsize(string) 
img = Image.open('paper.png')

d = ImageDraw.Draw(img)


d.text((5,5), string,(0,0,0),font= font,)

img.save('script_output.png',quality =100, optimize= True)


# def encode(sample : string) -> PIL.Image():
#     img = Image.new()

