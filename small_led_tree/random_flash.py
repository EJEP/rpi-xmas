from random import randint
from small_led_tree import SmallLedTree

tree = SmallLedTree({'A': 21, 'B': 19, 'C': 26, 'D': 20})

leds = ['led_0', 'led_1', 'led_2', 'led_3', 'led_4', 'led_5', 'led_6']
on_set = set()

while True:
    # Select a random LED
    random_led = leds[randint(0, 6)]
    # Toggle state
    if random_led in on_set:
        on_set.remove(random_led)
    else:
        on_set.add(random_led)

    tree.leds_on(on_set, 0.03)
