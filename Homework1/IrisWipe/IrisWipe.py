from PIL import Image
import math
import numpy as np
import matplotlib.pyplot as plt

# load the images and keep its data in np.array type
img1 = Image.open('../img/诺贝尔.jpg')
img2 = Image.open('../img/lena.jpg')

'''
#only show in red channel
r1, g1, b1 = img1.split()
r2, g2, b2 = img2.split()
img1 = r1
img2 = r2
'''

im1 = np.array(img1)
im2 = np.array(img2)

#rows, cols = im1.shape  #for red channel only
rows, cols, dims = im1.shape #for three channels

# initial the counting time
t = 0
while t < 500:
    # check each pixel by orws and cols
    for x in range(rows):
        for y in range(cols):
            # the radius decide by the time
            if (pow(x-rows//2,2)+pow(y-cols//2,2)<=pow(t,2)):
                # change the circle region to lena
                im1[x,y] = im2[x,y]
    t += 40
    plt.imshow(im1)
    plt.axis('off') # 去除坐标系

    # keep a while show the changing process
    plt.pause(0.03)
plt.close()