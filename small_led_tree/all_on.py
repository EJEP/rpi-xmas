from small_led_tree import SmallLedTree

tree = SmallLedTree({'A': 21, 'B': 19, 'C': 26, 'D': 20})

tree.leds_on(['led_0', 'led_1', 'led_2', 'led_3', 'led_4', 'led_5', 'led_6'],
             10)

tree.all_leds_off()
