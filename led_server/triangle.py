from typing import List, Tuple

class TriangleData:
    def __init__(self, x:int, y:int, pattern:str, rgb:List[int], speed:int, cycle:int, minimum:int, maximum:int, leds:List[int]) -> None:
        self.x = x
        self.y = y
        self.pattern = pattern
        self.rgb = rgb
        self.speed = speed
        self.cycle = cycle
        self.minimum = minimum
        self.maximum = maximum
        self.leds = leds


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