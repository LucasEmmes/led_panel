from dataclasses import dataclass
from typing import List

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