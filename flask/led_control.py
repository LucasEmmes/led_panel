from rpi_ws281x import *

LED_COUNT = 150
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0

def set_led(r,g,b):
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()

    for i in range(LED_COUNT):
            strip.setPixelColor(i, Color(r,g,b))

    strip.show()