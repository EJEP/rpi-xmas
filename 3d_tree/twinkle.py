from gpiozero import PiHutXmasTree
from gpiozero.tools import random_values
from signal import pause

tree = PiHutXmasTree(pwm=True)

tree.star.on()
tree.star.value = 0.5

for led in tree[1:]:
    led.source_delay = 0.15
    led.source = random_values()

pause()
