point_dict = {}


class face_c:
    def __init__(self, data_string) -> None:
        # data string is in format "p1,p2,p3"
        data = data_string.split(",")
        self.points = [point_dict[p] for p in data]

    def __repr__(self) -> str:
        result = "\nfacet normal 0 0 0\n\touter loop"
        for point in self.points:
            result += f"\n\t\tvertex {point[0]} {point[1]} {point[2]}"
        result += "\n\tendloop\nendfacet"
        return result

    def __str__(self) -> str:
        return repr(self)

def add_to_dict(point_list, names, prefix=""):
    global point_dict
    names = names.split(",")
    for i in range(len(point_list)):
        point_dict[prefix+names[i]] = point_list[i]

def move_up(point, z):
    return (point[0], point[1], z)

# BASE
points_underside_floor = [(-0.5, 14.72, 0), (0.5, 14.72, 0), (8.5, 0.87, 0), (8, 0, 0), (-8, 0, 0), (-8.5, 0.87, 0)]
add_to_dict(points_underside_floor, "A,B,C,D,E,F", prefix="b")

points_inside_floor = [(-0.23, 14.4, 0.2), (0.23, 14.4, 0.2), (8.08, 0.79, 0.2), (7.85, 0.4, 0.2), (-7.85, 0.4, 0.2), (-8.08, 0.79, 0.2)]
add_to_dict(points_inside_floor, "a,b,c,d,e,f", prefix="b")

# TOP WALLS
points_wall_outside = [move_up(p, 3) for p in points_underside_floor]
add_to_dict(points_wall_outside, "A,B,C,D,E,F", prefix="t")

points_wall_inside = [move_up(p, 3) for p in points_inside_floor]
add_to_dict(points_wall_inside, "a,b,c,d,e,f", prefix="t")

# HOLE1
points_opening_topleft_lower = [(-3.75, 9.09, 0.75), (-3.4, 8.89, 0.75), (-4.9, 6.29, 0.75), (-5.25, 6.49, 0.75)]
add_to_dict(points_opening_topleft_lower, "G,g,h,H", prefix="b")

points_opening_topleft_upper = [move_up(p, 2.25) for p in points_opening_topleft_lower]
add_to_dict(points_opening_topleft_upper, "G,g,h,H", prefix="t")

# HOLE2
points_opening_topright_lower = [(3.4, 8.89, 0.75), (3.75, 9.09, 0.75), (5.25, 6.49, 0.75), (4.9, 6.29, 0.75)]
add_to_dict(points_opening_topright_lower, "i,I,J,j", prefix="b") 

points_opening_topright_upper = [move_up(p, 2.25) for p in points_opening_topright_lower]
add_to_dict(points_opening_topright_upper, "i,I,J,j", prefix="t")

# HOLE3
points_opening_middle_lower = [(-1.5, 0.4, 0.75), (1.5, 0.4, 0.75), (1.5, 0, 0.75), (-1.5, 0, 0.75)]
add_to_dict(points_opening_middle_lower, "l,k,K,L", prefix="b")

points_opening_middle_upper = [move_up(p, 2.25) for p in points_opening_middle_lower]
add_to_dict(points_opening_middle_upper, "l,k,K,L", prefix="t")


face_floor_bottom = "bA,bB,bC bC,bD,bE bE,bF,bA bA,bC,bE"
face_floor_inside = "ba,bb,bc bc,bd,be be,bf,ba ba,bc,be"

face_wall_top = "tA,ta,tb tB,tb,tc tC,tc,td tD,td,te tE,te,tf tF,tf,ta tA,tB,tb tB,tC,tc tC,tD,td tD,tE,te tE,tF,tf tF,tA,ta"

face_pillars_inside = "ta,tb,bb ta,bb,ba tc,td,bd tc,bd,bc te,tf,bf te,bf,be"
face_pillars_outside = "tA,tB,bB tA,bB,bA tC,tD,bD tC,bD,bC tE,tF,bF tE,bF,bE"

face_walls_inside_bc = "tb,tc,ti tc,ti,tj tb,ti,bi tb,bb,bi tc,tj,bj tc,bj,bc bb,bi,bc bi,bj,bc"
face_walls_inside_de = "td,te,tk te,tk,tl td,tk,bk td,bd,bk te,tl,bl te,bl,be bd,bk,be bk,bl,be"
face_walls_inside_fa = "tf,ta,th ta,th,tg tf,th,bh tf,bf,bh ta,tg,bg ta,bg,ba bf,bh,ba bh,bg,ba"

face_walls_outside_bc = "tB,tC,tI tC,tI,tJ tB,tI,bI tB,bB,bI tC,tJ,bJ tC,bJ,bC bB,bI,bC bI,bJ,bC"
face_walls_outside_de = "tD,tE,tK tE,tK,tL tD,tK,bK tD,bD,bK tE,tL,bL tE,bL,bE bD,bK,bE bK,bL,bE"
face_walls_outside_fa = "tF,tA,tH tA,tH,tG tF,tH,bH tF,bF,bH tA,tG,bG tA,bG,bA bF,bH,bA bH,bG,bA"

face_hole_inside_ij = "tI,ti,bi tI,bI,bi bI,bi,bj bI,bJ,bj bJ,bj,tj bJ,tJ,tj tJ,tj,ti tJ,tI,ti"
face_hole_inside_kl = "tK,tk,bk tK,bK,bk bK,bk,bl bK,bL,bl bL,bl,tl bL,tL,tl tL,tl,tk tL,tK,tk"
face_hole_inside_hg = "tH,th,bh tH,bH,bh bH,bh,bg bH,bG,bg bG,bg,tg bG,tG,tg tG,tg,th tG,tH,th"

faces = [face_floor_bottom, face_floor_inside,
face_wall_top,
face_pillars_inside, face_pillars_outside,
face_walls_inside_bc, face_walls_inside_de, face_walls_inside_fa,
face_walls_outside_bc, face_walls_outside_de, face_walls_outside_fa,
face_hole_inside_ij,face_hole_inside_kl,face_hole_inside_hg
]


face_objs = []
for part in faces:
    face_objs += [face_c(d) for d in part.split(" ")]

f = open("data.stl", "w", encoding="ascii")
f.write("solid nanoleaf")
for face in face_objs:
    f.write(str(face))
f.write("\nendsolid nanoleaf")
f.close()