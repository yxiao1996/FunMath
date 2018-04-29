import cv2
import pyximport
pyximport.install()
import numpy as np
from veriPoint import veriPoint_c, veriPoint

world_size = 1024
world = np.zeros((world_size, world_size, 3), dtype=np.uint8)
graph_offset = world_size / 2

def testPoint(re, im, thresh=30):
    x = complex(0, 0)
    c = complex(re, im)
    for i in range(thresh):
        x = x * x + c
    if abs(x.real) > 2.0 or abs(x.imag) > 2.0:
        return False
    else:
        return True


for i in range(graph_offset):
    for j in range(i):
        display_pixel_0 = (j + graph_offset, i-j + graph_offset)
        test_point = (2.0*float(j)/float(graph_offset), 2.0*float(i-j)/float(graph_offset))
        #print test_point
        if veriPoint(test_point[0], test_point[1]):
            world[display_pixel_0[0]][display_pixel_0[1]][0] = 255
        else:
            world[display_pixel_0[0]][display_pixel_0[1]][1] = 255
        display_pixel_1 = (j + graph_offset, j-i + graph_offset)
        test_point = (2.0*float(j)/float(graph_offset), 2.0*float(j-i)/float(graph_offset))
        if veriPoint(test_point[0], test_point[1]):
            world[display_pixel_1[0]][display_pixel_1[1]][0] = 255
        else:
            world[display_pixel_1[0]][display_pixel_1[1]][1] = 255
        display_pixel_2 = (-j + graph_offset, i-j + graph_offset)
        test_point = (2.0*float(-j)/float(graph_offset), 2.0*float(i-j)/float(graph_offset))
        if veriPoint(test_point[0], test_point[1]):
            world[display_pixel_2[0]][display_pixel_2[1]][0] = 255
        else:
            world[display_pixel_2[0]][display_pixel_2[1]][1] = 255
        display_pixel_3 = (-j + graph_offset, j-i + graph_offset)
        test_point = (2.0*float(-j)/float(graph_offset), 2.0*float(j-i)/float(graph_offset))
        if veriPoint(test_point[0], test_point[1]):
            world[display_pixel_3[0]][display_pixel_3[1]][0] = 255
        else:
            world[display_pixel_3[0]][display_pixel_3[1]][1] = 255
    #cv2.imshow("mandelbrot", cv2.resize(world, (2048, 2048)))
    if i % 8 == 0:
        print i / 8
        cv2.imshow("mandelbrot", world)
        cv2.waitKey(1)
#cv2.imwrite("16384.jpg", world)
cv2.waitKey(0)