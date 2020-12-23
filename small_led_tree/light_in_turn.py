from small_led_tree import SmallLedTree

tree = SmallLedTree({'A': 21, 'B': 19, 'C': 26, 'D': 20})

leds = ['led_0', 'led_1', 'led_2', 'led_3', 'led_4', 'led_5', 'led_6']

for _ in range(5):
    for led in leds:
        tree.leds_on([led], 0.5)

tree.all_leds_off()
