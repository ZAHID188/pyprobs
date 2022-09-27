"""
pillow(PIL)
Opencv
skimage
"""

from PIL import Image
im1 = Image.open('1.png')
print(im1.size, im1.format, im1.mode)
Image.open('1.png').save('2.png')
im2 = Image.open('2.png')
size = (288, 180)
im2.thumbnail(size)
out = im2.rotate(45)
im1.paste(out, (50,50))
im1.show()