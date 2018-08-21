#!usr/bin/env python
# coding:utf-8

import os
from PIL import Image

sourceFile = u"kegcDRPe.ttf"

source = open(sourceFile,'r').read()

def makeImage():
	pass

image = Image.open(sourceFile)

#展示图片
image.show()

#
imageCover = image.convert('RGB')

imageCover.show()