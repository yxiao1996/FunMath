import cv2
import math
import numpy as np

num_step = 1000
world_size = 1024
world = np.zeros((world_size, world_size, 3), dtype=np.uint8)
dtft_world = np.zeros((256, num_step, 3), dtype=np.uint8)
offset = 1.0

data = [0.0, 0.1, 0.2, 0.3, 1.0, 1.0, 1.0, 1.0, 0.3, 0.2, 0.1, 0.0]
#data = np.random.normal(0.0, 1.0, 50)

def Roll(data, omega):
    roll_data = []
    # Roll data point on unit circle
    for i, datum in enumerate(data):
        # e^(-j*w*n)
        re_ = math.cos(omega * i)
        im_ = math.sin(omega * i)
        roll_datum = (re_*datum, im_*datum)
        roll_data.append(roll_datum)
    return roll_data

def drawUnitCircel(world):
    # Draw unit circle in the world
    origin = (world_size/2, world_size/2)
    unit_cirle_scalar = world_size / 8
    cv2.circle(world, origin, unit_cirle_scalar, (255, 0, 0))

def drawCenter(data, world):
    origin = (world_size/2, world_size/2)
    unit_cirle_scalar = world_size / 8
    # Draw the "center of mass" of all data points
    sum_re = 0.0
    sum_im = 0.0
    for datum in data:
        sum_re += datum[0]
        sum_im += datum[1]
    center_re = sum_re / float(len(data))
    center_im = sum_im / float(len(data))
    plot_center = (int(origin[0]+center_re*unit_cirle_scalar), int(origin[1]+center_im*unit_cirle_scalar))
    cv2.circle(world, plot_center, 4, (0, 0, 255))
    # return norm
    return math.sqrt(center_re ** 2 + center_im ** 2)

def drawData(data, world):
    origin = (world_size/2, world_size/2)
    unit_cirle_scalar = world_size / 8
    for datum in data:
        re_ = datum[0]
        im_ = datum[1]
        plot_datum = (int(origin[0]+re_*unit_cirle_scalar), int(origin[1]+im_*unit_cirle_scalar))
        cv2.circle(world, plot_datum, 4, (0, 255, 0))

def drawDTFT(norm, step, world):
    cv2.line(world, (step, 256-int(norm*128)), (step, 256), (255, 0, 0))

def VisualizeDTFT(data):
    for i in range(len(data)):
        data[i] += offset
    omega_step_size = 4.0 * np.pi / num_step
    for i in range(num_step+1):
        world = np.zeros((world_size, world_size, 3), dtype=np.uint8)
        omega = i * omega_step_size
        data_roll = Roll(data, omega)
        #print data_roll
        drawUnitCircel(world)
        drawData(data_roll, world)
        norm = drawCenter(data_roll, world)
        drawDTFT(norm, i, dtft_world)
        cv2.imshow('viz', world)
        cv2.imshow('dtft', dtft_world)
        cv2.waitKey(50)

VisualizeDTFT(data)
cv2.waitKey(0)
