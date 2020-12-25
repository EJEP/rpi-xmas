from tree import RGBXmasTree
import random

tree = RGBXmasTree()

def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    yield (r, g, b)


try:
    for led in tree:
        led.source_delay = 0.15
        led.source = random_color()
except KeyboardInterrupt:
    tree.close()
