# RPi Xmas

This will document the various christmas trees I own which mount on Raspberry Pis, i.e. how to mount them along with code to use them. May also contain code to run them on various microcontrollers.

# GPIO Xmas Tree

From [pocketmoneytronics.co.uk](https://www.pocketmoneytronics.co.uk), although apparently no longer sold. Some construction instructions are on [raspberrypi-spy.co.uk](https://www.raspberrypi-spy.co.uk/2014/12/raspberry-gpio-xmas-tree-add-on/). The example code files still seem to be hosted at `http://www.pocketmoneytronics.co.uk/downloads/xmas.zip`. Mounts on *physical* pin numbers 21-26 on the model A or B and 35-40 on later models. See picture.

Some description is [here](http://www.pocketmoneytronics.co.uk/?page_id=239).

The LEDS are charlieplexed. 

The example code will live in `small_led_tree/`

Mountimg is like this:

![Small LED Xmas tree on Raspberry Pi](./images/small_led_xmas_tree.jpg)

# SMD Xmas Tree

Also from [pocketmoneytronics.co.uk](http://www.pocketmoneytronics.co.uk), product page is at `http://www.pocketmoneytronics.co.uk/?page_id=540`. The code for a Raspberry Pi is in `xmas_smd.py`. There is also code for Arduino and Pyboard.

The example code will be in `smd_tree/`

Mountimg is like this:

![SMD Xmas tree on Raspberry Pi](./images/smd_tree.jpg)

# GPIO RGB Xmas Tree

Also from [pocketmoneytronics.co.uk](www.pocketmoneytronics.co.uk). Same concept as the previous one but with RGB LEDs. The page is at `http://www.pocketmoneytronics.co.uk/?page_id=423`. Some instructions are also available from [raspberrypi-spy.co.uk](https://www.raspberrypi-spy.co.uk/2016/12/rgb-led-christmas-tree-by-pocketmoneytronics/).

The board uses the `rpi_ws281x` library to communicate with the LEDs. It behaves like Neopixels which I think use SPI?

The example code will be in `small_rgb_tree/`.

Mountimg is like this:

![Small RGB Xmas tree on Raspberry Pi](./images/small_rgb_tree.jpg)

# 3D Xmas tree

From [The Pi Hut](https://thepihut.com/products/3d-xmas-tree-for-raspberry-pi). Soldering kit. Code is on the linked product page.

Example code will be in `3d_tree/`

Mountimg is like this:

![3D Xmas tree on Raspberry Pi](./images/3d_xmas_tree.jpg)

# 3D RGB Xmas tree

From [The Pi Hut](https://thepihut.com/products/3d-rgb-xmas-tree-for-raspberry-pi). Comes mostly assembled. Code from ThePiHut is [available on GitHub](https://github.com/ThePiHut/rgbxmastree)

Example code will be in `3d_rgb_tree/`

Mounting is like this:

![3D RGB Xmas tree on Raspberry Pi](./images/3d_rgb_xmas_tree.jpg)
