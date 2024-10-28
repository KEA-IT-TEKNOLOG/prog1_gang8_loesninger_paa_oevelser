import time

from neopixel_ring import NeoPixelRing
from button import Button
from potentiometer import Potentiometer

"""
Example of code with low coupling and high cohesion

The code reads a potentiometer value to control brightness of a neopixel ring

The program includes 2 pushbuttons that can be pushed to change color on neopixel ring

Each part of the functionality is isolated in a module with a class (High cohesion and low coupling)
By doing this it is easier to reuse each module for other programs
"""

def main():
    np_ring = NeoPixelRing(26, 12)
    pot = Potentiometer(34)

    def button1_handler(pin):
        np_ring.set_color((0, 255, 0))
        time.sleep(1)

    def button2_handler(pin):
        np_ring.set_color((0, 0, 255))
        time.sleep(1)

    button1 = Button(0, button1_handler)
    button2 = Button(4, button2_handler)

    while True:
        pot_value = pot.read_value()
        brightness = pot_value // 4
        np_ring.set_color((brightness, 0, 0))
        time.sleep(0.1)

if __name__ == "__main__":
    main()