from Imagechanger import convert
from PIL import Image
#img = Image.open('II.jpg')
#im = convert(img)
#im.show()
def outline(imga):
    sketch = Image.new('RGBA',(imga.width,imga.height))
    for x in range(imga.width):
        for y in range(imga.height):
            online = False
            for x1 in range(-1,2):
                if not online:
                    for y1 in range(-1,2):
                        try:
                            if imga.getpixel((x+x1,y+y1)) != imga.getpixel((x,y)):
                                online = True
                                break
                        except:
                            print(" ",end="")
            if online:
                sketch.putpixel((x,y),(255,255,255,255))
    return sketch
#outline(im).show()

