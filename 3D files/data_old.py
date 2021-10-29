from typing import List, Tuple

class point_3d:
    def __init__(self, coords:Tuple[float, float], z:float) -> None:
        self.x = coords[0]
        self.y = coords[1]
        self.z = z

    def __str__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"
    
    def __repr__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"

def definition_to_flat_shape(definition:List[Tuple[float,float]], z:float):
    result = []
    for triangle in definition:
        new_triangle = tuple([point_3d(p, z) for p in triangle])
        result.append(new_triangle)
    return result

A=(-0.5, 14.72)
B=(0.5, 14.72)
C=(8.5, 0.87)
D=(8, 0)
E=(-8, 0)
F=(-8.5, 0.87)

print([point_3d(p, 0) for p in [A,B,C,D,E,F]])

# Z COORD 0
def_floor_underside = [(A,B,D), (C,D,E), (E,F,A), (A,C,E)]
shape_floor_underside = definition_to_flat_shape(def_floor_underside, 0)
# print(shape_floor_underside)

a=(-0.23, 14.4)
b=(0.23, 14.4)
c=(8.08, 0.79)
d=(7.85, 0.4)
e=(-7.85, 0.4)
f=(-8.08, 0.79)
print([point_3d(p, 0.2) for p in [a,b,c,d,e,f]])

# Z COORD 0.2
def_floor_inside = ((a,b,c), (c,d,e), (e,f,a), (a,c,e))
shape_floor_inside = definition_to_flat_shape(def_floor_inside, 0.2)
# print(shape_floor_inside)

# Z COORD 3
def_wall_topside = ((A,a,b), (B,b,c), (C,c,d), (D,d,e), (E,e,f), (F,f,a),
                (A,B,b), (B,C,c), (C,D,d), (D,E,e), (E,F,f), (F,A,a))
shape_wall_topside = definition_to_flat_shape(def_wall_topside, 3)
# print(shape_wall_topside)
