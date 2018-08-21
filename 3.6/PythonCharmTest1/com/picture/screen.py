#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      wmzhang
#
# Created:     18/09/2016
# Copyright:   (c) wmzhang 2016
# Licence:     <your licence>

# You should install Pill first,
# http://pillow.readthedocs.io/en/latest/installation.html
#-------------------------------------------------------------------------------
from PIL import Image,ImageGrab

class screen:
    savePath="d:/screenshot.png"
    savePath2="d:/screenshot2.bmp"
    def __init__(self):
        pass
    '''
    Python comments
    line 2
    '''

    """
    Or that this
    line 2
    """

    def FullScreen(self):
        im=ImageGrab.grab()
        #print(self.savePath)
        im.save(self.savePath)

    """
    The region-Image: x-start,y-start,x-end,y-end
    """
    def ScreenCapture(self,region):
        try:
            self.FullScreen()
            im=Image.open(self.savePath)
            reg=im.crop(region)
            #reg.show() # Open the picture
            reg.save(self.savePath2)
        except BaseException:
            print("Exception BaseException")
        else:
            print("Exception Else")
        finally:
            print("Exception Finally")

    def OpenAndPrint(self):
        im=Image.open(self.savePath)
        print(im.size)