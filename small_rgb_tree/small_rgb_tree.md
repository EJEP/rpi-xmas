# Circuit

From the kickstarter page the tree uses PL9823 or APA106 LEDs. These use the same protocal as ws281x LEDS.

ws281x LEDs use three pins, +5V, ground and data. The tree takes 12 pins on the Pi, but only uses four of them (the two 5V pins are both used.

| Physical pin | Use     |
|--------------|---------|
| 2            | +5V     |
| 4            | +5V     |
| 6            | Ground  |
| 12           | GPIO 18 |

TODO: Circuit diagram.

Looks like the diode is to drop the power down a bit from 5V so that the LEDs can communicate with the pi over 3.3V logic. Need to see if this works with Arduino.

# How to use
## Raspberry Pi

The Raspberry Pi requires the `rpi_ws281x` library to use with ws281x LEDs as the Pi does not have real time control of the GPIO pins due to having a multi-tasking operating system. The library does clever things to get around this.

## Microcontroller

TODO
