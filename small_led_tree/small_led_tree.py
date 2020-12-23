# Code to control the tree, adapted from the example code provided. This omits
# the code for the kit with a bicolour LED as I don't have one of those to test
# with.

import RPi.GPIO as GPIO
import time


class SmallLedTree:
    def __init__(self, pins, illumination_time=0.001):
        self.pins = pins
        self.illumination_time = illumination_time

        self.led_node_mapping = {'led_0': {'anode': 'C', 'cathode': 'A'},
                                 'led_1': {'anode': 'C', 'cathode': 'D'},
                                 'led_2': {'anode': 'D', 'cathode': 'C'},
                                 'led_3': {'anode': 'D', 'cathode': 'B'},
                                 'led_4': {'anode': 'B', 'cathode': 'D'},
                                 'led_5': {'anode': 'A', 'cathode': 'B'},
                                 'led_6': {'anode': 'B', 'cathode': 'A'},
                                 }

        GPIO.setmode(GPIO.BCM)

    def __del__(self):
        GPIO.cleanup()

    def single_led_on(self, led_number):
        GPIO.setup(self.pins['A'], GPIO.IN)
        GPIO.setup(self.pins['B'], GPIO.IN)
        GPIO.setup(self.pins['C'], GPIO.IN)
        GPIO.setup(self.pins['D'], GPIO.IN)

        # Set anode and cathode for the LED selected
        GPIO.setup(self.pins[self.led_node_mapping[led_number]['anode']],
                   GPIO.OUT)
        GPIO.setup(self.pins[self.led_node_mapping[led_number]['cathode']],
                   GPIO.OUT)

        GPIO.output(self.pins[self.led_node_mapping[led_number]['anode']],
                   GPIO.HIGH)
        GPIO.output(self.pins[self.led_node_mapping[led_number]['cathode']],
                   GPIO.LOW)

    def leds_on(self, leds, wait_time):
        for _ in range(int(wait_time / self.illumination_time)):
            for led in leds:
                self.single_led_on(led)
                time.sleep(self.illumination_time)

    def all_leds_off(self):
        GPIO.setup(self.pins['A'], GPIO.IN)
        GPIO.setup(self.pins['B'], GPIO.IN)
        GPIO.setup(self.pins['C'], GPIO.IN)
        GPIO.setup(self.pins['D'], GPIO.IN)
