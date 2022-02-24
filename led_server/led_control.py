from rpi_ws281x import *
from typing import List
from triangle import *
from time import sleep

LED_COUNT = 150
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0

class Killswitch:
        def __init__(self, kill:bool) -> None:
                self.kill = kill
        

def render_loop(triangles:List['TriangleData'], kill:'Killswitch') -> None:
        global LED_COUNT
        LED_COUNT = len(triangles) * 6

        led_lookup = [(0,0,0)]*LED_COUNT

        while not kill:
                render_triangles(triangles, led_lookup)
                sleep(0.1)


def render_triangles(triangles:List['TriangleData'], led_lookup:List[Tuple[int, int, int]]) -> None:
        for triangle in triangles:

                # Get next rgb value from triangle.py
                rgb = triangle.next()
                
                # Each triangle has a corresponding rgb tuple in a list
                for led_id in triangle.leds:
                        set_led(led_id, rgb)

        pass

def set_led(led_id:int, color:Tuple[int, int, int]) -> None:
        r, g, b = color

        strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        strip.begin()

        strip.setPixelColor(led_id, Color(r,g,b))

        strip.show()

def turn_off():
        strip = Adafruit_NeoPixel(150, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
        strip.begin()

        for i in range(150):
                strip.setPixelColor(i, Color(0,0,0))

        strip.show()