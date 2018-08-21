# For import PIL, you should install first, using the package management tool. PIP
# Cd to Python folder,find the pip.exe, ex: D:\Program Files (x86)\Python34\Scripts
# Run PIP in the command line: pip install PIL
# http://pillow.readthedocs.io/en/latest/installation.html
import PIL
from PIL import Image,ImageGrab
import os

im = ImageGrab.grab()
# or call im.show() to view the image directly
im.save("d:/screenshot.png")
#os.execvp( "mspaint",('mspaint','c:/screenshot.png'))
im1=Image.open("d:/screenshot.png")
print (im1.size)

rec=(400,400,800,800)
region=im1.crop(rec)
region.show()
region.save("d:/123.bmp")