from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class TriangleData:
    x:int
    y:int
    pattern:str
    rgb:List[int]
    speed:int
    cycle:int
    minimum:int
    maximum:int
    leds:List[int]

def next(triangle:'TriangleData') -> Tuple[int, int, int]:

    if triangle.pattern == "static":
        # NOP
        return triangle.rgb
    
    elif triangle.pattern == "breathe":
        # Advance cycle
        triangle.cycle = (triangle.cycle + triangle.speed) % 512
        # Get the cycle percentage (how far are we into the cycle)
        cycle_percentage = triangle.cycle / 512
        # How many percent of maximum light are we supposed to give
        light_fraction = math.sin(cycle_percentage * 2 * math.pi) / 2 + 0.5
        # With regards to min/max how many ACTUAL percent of light to we need
        light_percentage = (light_fraction * (triangle.maximum - triangle.minimum) + triangle.minimum) / 255
        
        # Apply and return
        next_rgb = [int(color * light_percentage) for color in triangle.rgb]
        return next_rgb

    elif triangle.pattern ==  "rainbow":
        # Advance cycle
        triangle.cycle = (triangle.cycle + triangle.speed) % 768
        # Find out where we are in the r cycle, g cycle, and b cycle
        rgb_cycle_percentages = [((triangle.cycle + i)%768)/256 for i in [0,85, 170]]
        # Calculate percentage of each color needed
        rgb_light_percentage = [(math.sin(cycle_percentage * 2 * math.pi) / 2 + 0.5) for cycle_percentage in rgb_cycle_percentages]
        
        # Apply and return
        next_rgb = []
        for i in range(3):
            next_rgb.append(int(triangle.rgb[i] * rgb_light_percentage[i]))
        return next_rgb

    else:
        return triangle.rgb