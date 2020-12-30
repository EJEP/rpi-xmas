# Circuit

ws281x LEDs use three pins, +5V, ground and data. The tree takes 12 pins on the Pi, but only uses four of them (the two 5V pins are both used.

| Physical pin | Use     |
|--------------|---------|
| 2            | +5V     |
| 4            | +5V     |
| 6            | Ground  |
| 12           | GPIO 18 |

# How to use
## Raspberry Pi

The Raspberry Pi requires the `rpi_ws281x` library to use with ws281x LEDs as the Pi does not have real time control of the GPIO pins due to having a multi-tasking operating system. The library does clever things to get around this.

## Microcontroller

TODO
