from PIL import Image, ImageDraw, ImageFont
import math
from glob import glob



a = 1
file = glob('Image_folder/*')
for i in file:
    chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    # chars = "wom- "[::-1]
    charArray = list(chars)
    charlength = int(len(chars))
    intervel = charlength/256
    scalefactor = 1
    onecharwidth  = 10
    onecharheight =18
    image = Image.open(i)
    fnt = ImageFont.truetype('C:\\Windows\\Fonts\\lucon.ttf',15)
    Width, Height = image.size
    image = image.resize((int(scalefactor * Width) , int(scalefactor * Height*(onecharwidth/onecharheight))), Image.NEAREST)
    Width, Height = image.size
    pix = image.load()
    output_image = Image.new('RGB', (onecharwidth*Width, onecharheight*Height), color=(0,0,0))
    d = ImageDraw.Draw(output_image)
    def getchar(inputint):
        return charArray[math.floor(inputint * intervel)]



    for i in range(Height):
        for j in range(Width):
            r,g,b = pix[j,i]         ######l7d hna 7fz
            h = int(r/3 + g/3 +b/3)
            # h = int(r/3 + g/3 +b/3)
            pix[j, i] = (h,h,h) 
            d.text((j *onecharwidth, i * onecharheight), getchar(h), font = fnt, fill = (r,g,b))

    output_image.save(f'result\\result_{a}.png')
    print(f"Done {a}")
    a +=1






