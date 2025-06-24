# Write your code here :-)
from adafruit_circuitplayground import cp
import time


def scale_light_to_index(lightValue):
    MAX = 320
    maxIndex = 9
    index = int(lightValue / MAX * maxIndex)


    if index < 0:
        index = 0
    elif index > maxIndex:
        index = maxIndex

    return index


def clear_pixels():
    for i in range(10):
        cp.pixels[i] = (0, 0, 0)


while True:
    light = cp.light
    print((light,))

    index = scale_light_to_index(light)
    clear_pixels()
    cp.pixels[index] = (255, 0, 0)

    time.sleep(0.05)

