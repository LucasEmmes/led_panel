from typing import Dict, List, Tuple, Optional
import math
import cv2
import numpy as np
from time import sleep


class Pattern:
    def __init__(self, pattern:str, rgb:Tuple[int, int, int], speed:float, cycle_counter:int, minimum:int, maximum:int) -> None:
        """Responsible for keeping track of the original and current color as well as advance the animation.  
        pattern: "static" | "breathe" | "rainbow"
        rgb: three integers in the range [0, 255] both inclusive
        speed: float for speed to advance animation (default 1)
        cycle_counter: where we are in the cycle (default 0), can use different values to offset cells
        minimum: lower bound for intensity in range [0, 255] both inclusive (default 0)
        maximum: upper bound for intensity in range [0, 255] both inclusive (default 255)
        """
        # TODO: check input

        self.pattern = pattern
        self.rgb = rgb
        self.speed = speed
        self.cycle_counter = cycle_counter
        self.minimum = minimum
        self.maximum = maximum

    def next(self) -> Tuple[int, int, int]:

        if self.pattern == "static":
            # NOP
            return self.rgb
        
        elif self.pattern == "breathe":
            # Advance cycle
            self.cycle_counter = (self.cycle_counter + self.speed) % 512
            # Get the cycle percentage (how far are we into the cycle)
            cycle_percentage = self.cycle_counter / 512
            # How many percent of maximum light are we supposed to give
            light_fraction = math.sin(cycle_percentage * 2 * math.pi) / 2 + 0.5
            # With regards to min/max how many ACTUAL percent of light to we need
            light_percentage = (light_fraction * (self.maximum - self.minimum) + self.minimum) / 255
            
            # Apply and return
            next_rgb = [int(color * light_percentage) for color in self.rgb]
            return next_rgb

        elif self.pattern ==  "rainbow":
            # Advance cycle
            self.cycle_counter = (self.cycle_counter + self.speed) % 768
            # Find out where we are in the r cycle, g cycle, and b cycle
            rgb_cycle_percentages = [((self.cycle_counter + i)%768)/256 for i in [0,85, 170]]
            # Calculate percentage of each color needed
            rgb_light_percentage = [(math.sin(cycle_percentage * 2 * math.pi) / 2 + 0.5) for cycle_percentage in rgb_cycle_percentages]
            
            # Apply and return
            next_rgb = []
            for i in range(3):
                next_rgb.append(int(self.rgb[i] * rgb_light_percentage[i]))
            return next_rgb

        else:
            return self.rgb

class Panel:
    def __init__(self, ids:List[int]) -> None:
        self.ids = ids
        self.rgb = [0,0,0]
        self.pattern = None
    
    def set_pattern(self, pattern:Pattern) -> None:
        self.pattern = pattern

    def next(self) -> Tuple[int, int, int]:
        self.rgb = self.pattern.next()
        return self.rgb


def parse_pattern_data(pattern_data):
    # ...;x,y,pattern,rgb,speed,cycle,min,max;...
    # pattern 0: only rgb
    # pattern 1: all
    # pattern 2: no min/max (for now)
    raw_panel_data = pattern_data.split(";")



def main():

    p = Panel([0])
    pat = Pattern("rainbow", (255,255,255), 1, 0, 0, 255)
    p.set_pattern(pat)

    img = np.zeros((100,100,3), np.uint8)
    while True:
        sleep(0.01)
        c = p.next()
        cv2.rectangle(img, (0,0), (100,100), c, thickness=-1)
        cv2.imshow("", img)

        if cv2.waitKey(1) == ord('q'):
            break

    cv2.destroyAllWindows()

main()