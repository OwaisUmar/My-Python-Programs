import numpy as np
from PIL import Image


img = Image.open(r'D:/owais.jpg')

pixelMap = img.load()
I = np.asanyarray(img)

newImg = Image.new(img.mode, img.size)
pixelNew = newImg.load()

for i in range(img.size[0]):
    for j in range(img.size[0]):
        for x in pixelMap[i, j]:

            pixelNew[i, j] = (x+1) // 32
            print(pixelNew[i, j])
