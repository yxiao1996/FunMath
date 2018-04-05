import cv2
import time
import numpy as np

cell_size = (10, 10)
world_size = (1024, 1024)
scale = 9

init_data = [(0, 0), (1, 0), (1, 1), (0, 1)]
data = [(0, 0), (0, 1), (1, 1), (1, 0),
        (2, 0), (3, 0), (3, 1), (2, 1),
        (2, 2), (3, 2), (3, 3), (2, 3),
        (1, 3), (1, 2), (0, 2), (0, 3)]

def drawGridworld(scale=1):
    image_size = (world_size[0], world_size[1], 3)
    world = np.zeros(image_size, dtype=np.int8)
    step_size = world_size[0] / 2**scale
    for i in range(world_size[0] / step_size):
        cv2.line(world, (i*step_size, 0), (i*step_size, world_size[0]), (255, 0, 0))
        cv2.line(world, (0, i*step_size), (world_size[0], i*step_size), (255, 0, 0))
    return world

def genData(scale):
    data = init_data
    for i in range(scale-1):
        new_data = []
        for j in range(len(data)):
            new_element = (data[j][1], data[j][0])
            new_data.append(new_element)
        for j in range(len(data)): 
            new_element = (data[j][0]+2**(i+1), data[j][1])
            new_data.append(new_element)
        for j in range(len(data)):
            new_element = (data[j][0]+2**(i+1), data[j][1]+2**(i+1))
            new_data.append(new_element)
        tmp_list = []
        for j in range(len(data)):
            new_element = (data[j][1], 2**(i+2)-data[j][0]-1)
            tmp_list.append(new_element)
        for j in range(len(tmp_list)):
            new_data.append(tmp_list[len(tmp_list)-1-j])
        data = new_data
    return data

def drawCurve(data, scale, world):
    step_size = world_size[0] / 2**scale
    for i in range(len(data) - 1):
        start_point = data[i]
        end_point = data[i+1]
        start_coord = (start_point[1]*step_size+step_size/2, start_point[0]*step_size+step_size/2)
        end_coord = (end_point[1]*step_size+step_size/2, end_point[0]*step_size+step_size/2)
        cv2.line(world, start_coord, end_coord, (0, 255, 0))
    return world

for i in range(9):
    scale = i+1
    world = drawGridworld(scale)
    data = genData(scale)
    world = drawCurve(data, scale, world)
    cv2.imshow('test', world)
    cv2.waitKey(0)
