import machine
import neopixel
import time

"""
Example of code with high coupling and low cohesion

The code reads a potentiometer value to control brightness of a neopixel ring

The program includes 2 pushbuttons that can be pushed to change color on neopixel ring

In this example the cohesion is improved by making a seperate class for each functionality
of the program but it is all still in the same module (high coupling)
"""

class NeoPixelRing:
    def __init__(self, pin, num_pixels):
        self.np = neopixel.NeoPixel(machine.Pin(pin), num_pixels)
        self.num_pixels = num_pixels

    def set_color(self, color):
        for i in range(self.num_pixels):
            self.np[i] = color
        self.np.write()

class Potentiometer:
    def __init__(self, pin):
        self.adc = machine.ADC(machine.Pin(pin))
        self.adc.atten(machine.ADC.ATTN_11DB)
        self.adc.width(machine.ADC.WIDTH_10BIT)

    def read_value(self):
        return self.adc.read()

class Button:
    def __init__(self, pin, callback):
        self.button = machine.Pin(pin, machine.Pin.IN, machine.Pin.PULL_UP)
        self.button.irq(trigger=machine.Pin.IRQ_FALLING, handler=callback)

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