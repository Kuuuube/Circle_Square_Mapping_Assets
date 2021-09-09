#!/usr/bin/python
from PIL import Image
import os, sys

import warnings
warnings.filterwarnings("ignore")

path = "resize/"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((500,500), Image.ANTIALIAS)
            imResize.save(f + '.png')

resize()
