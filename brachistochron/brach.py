import cv2
import math
import numpy as np

world_size = 1024

world = np.ones((world_size, world_size, 3), dtype=np.uint8)
#world = world * 255

# Johannn Bernoulli's solution
divide = 16
const = 32

def getColors(divide):
    colors = []
    for i in range(divide):
        color = round(float(i) / float(divide) * 255)
        colors.append(color)
    return colors[1:]

def getBound(divide):
    bounds = []
    for i in range(divide):
        bound = round(float(i) / float(divide) * float(world_size))
        bounds.append(bound)
    return bounds[1:]

def getInterval(divide):
    return float(world_size) / float(divide)

def calcuDeltaX(bound, const, divide):
    # sqrt(bound) / sin(theta) = const
    sin_theta = math.sqrt(bound) / const
    cos_theta = math.sqrt(1.0 - sin_theta ** 2)
    tan_theta = sin_theta / cos_theta
    interval = getInterval(divide)
    delta_x = tan_theta * interval
    return int(delta_x)

def drawBrach(divide, const):
    colors = getColors(divide)
    bounds = getBound(divide)
    assert len(colors) == len(bounds)
    x_offset = 0
    y_offset = 0
    for i, bound in enumerate(bounds):
        # paint the section with color
        #print int(bound) - y_offset
        for j in range(int(bound) - y_offset):
            for k in range(world_size):
                world[y_offset+j][k][0] = colors[i]
        # Draw curve
        delta_x = calcuDeltaX(bound, const, divide)
        cv2.line(world, (x_offset, y_offset), (x_offset+delta_x, int(bound)), (0, 255, 0))
        # move buffer
        x_offset += delta_x
        y_offset = int(bound)
    print world
    cv2.imshow('test', world)
    cv2.waitKey(0)

drawBrach(divide, const)