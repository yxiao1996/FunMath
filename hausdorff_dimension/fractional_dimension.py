"""
1024-Sierpinski_triangle
By Beojan Stanislaus, CC BY-SA 3.0, https://commons.wikimedia.org/w/index.php?curid=8862246
"""
"""
calculate fractional dimension
"""
import cv2
import math
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

# Macros
max_scale = 10 # max image size 1024, 1024
world_size = (2**max_scale, 2**max_scale)

def getBinaryImgae(image):
    # Convert BGR image into Binary image
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_bin = np.zeros((world_size[0], world_size[1]), dtype=np.uint8)
    image_hight = image_gray.shape[1]
    image_width = image_gray.shape[0]
    for i in range(image_width):
        for j in range(image_hight):
            if image_gray[i][j] > 0:
                #print "*"
                image_bin[i][j] = 255
    return image_bin

def maxPooling(image):
    # Downsample by scale(2, 2)
    current_size = (image.shape[0]/2, image.shape[1]/2)
    downsampled_image = np.zeros(current_size, dtype=np.uint8)
    neighbour_size = 2
    cell_number = image.shape[0] / neighbour_size
    count_previous = 0
    for i in range(cell_number):
        for j in range(cell_number):
            # Locate into cell
            x_offset = i * neighbour_size
            y_offset = j * neighbour_size
            for m in range(neighbour_size):
                for n in range(neighbour_size):
                    if image[m+x_offset][n+y_offset] > 0:
                        downsampled_image[i][j] = 255
                        count_previous += 1
    return downsampled_image, count_previous

def genData(image, scale):
    max_scale = scale
    scale_data = []
    count_data = []
    for i in range(max_scale-1):
        #new_scale_data = 2 ** (max_scale - i)
        new_scale_data = [max_scale - i]
        scale_data.append(new_scale_data)
        image, count = maxPooling(image)
        count_data.append([math.log(count, 2)])
    data = zip(scale_data, count_data)
    return scale_data, count_data

sierpinski_tri = cv2.imread("1024-Sierpinski_triangle.png")
bin_sierpinski_tri = getBinaryImgae(sierpinski_tri)
scales, counts = genData(bin_sierpinski_tri, max_scale)

# Using linear regression model to estimate fractional dimensoin
regr = linear_model.LinearRegression()
regr.fit(scales, counts)
print regr.coef_
# get model slope
#test = [[2], [3]]
#pred = regr.
#np.save('data.npy', data)
#bin_sierpinski_tri = cv2.imread("bin_sierpinski_triangle.png")
#cv2.imshow('pool0', bin_sierpinski_tri)
#pool1, count0 = maxPooling(bin_sierpinski_tri)
#print count0
#cv2.imshow('pool1', pool1)
#pool2, count1 = maxPooling(pool1)
#print count1
#cv2.imshow('test', pool2)
#cv2.waitKey(0)
