from Imagechanger import convert
from Outliner import outline
from PIL import Image
from datetime import datetime
s = datetime.now()
from moviepy.editor import *
framerate = 24
clip = VideoFileClip("intro.mp4")
t = 367
while True:
    clip.save_frame("frame.jpg", t/framerate)
    im = Image.open('frame.jpg')
    h = outline(convert(im))
    h.save(f'sequence/frame{t+1}.png')
    print(f'Frame {t+1} done')
    print(f' Time took: {datetime.now() - s}')
    s = datetime.now()
    t+=1



