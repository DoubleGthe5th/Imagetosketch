from PIL import Image
img = Image.open('II.jpg')
#img.save(img.pdf) saves image to another spot
"""
MAX = (200,200)
img.thumbnail(MAX)
"""
#edits max size of image
#img.show()
def convert(imga):
    im = Image.new('RGB',(imga.width,imga.height))
    compress = 50
    for x in range(imga.width):
        for y in range(imga.height):
            f = imga.getpixel((x,y))
            g = tuple(int(round(s/compress)*compress) for s in f)
            im.putpixel((x,y),g)
    return im