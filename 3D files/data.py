point_dict = {}

def add_to_dict(point_list, names, prefix=""):
    global point_dict
    names = names.split(",")
    for i in range(len(point_list)):
        point_dict[prefix+names[i]] = point_list[i]

def move_up(point, z):
    return (point[0], point[1], z)

points_underside_floor = [(-0.5, 14.72, 0), (0.5, 14.72, 0), (8.5, 0.87, 0), (8, 0, 0), (-8, 0, 0), (-8.5, 0.87, 0)]
add_to_dict(points_underside_floor, "A,B,C,D,E,F", prefix="b")

points_inside_floor = [(-0.23, 14.4, 0.2), (0.23, 14.4, 0.2), (8.08, 0.79, 0.2), (7.85, 0.4, 0.2), (-7.85, 0.4, 0.2), (-8.08, 0.79, 0.2)]
add_to_dict(points_inside_floor, "a,b,c,d,e,f", prefix="b")

points_wall_outside = [move_up(p, 3) for p in points_underside_floor]
add_to_dict(points_wall_outside, "A,B,C,D,E,F", prefix="t")

points_wall_inside = [move_up(p, 3) for p in points_inside_floor]
add_to_dict(points_wall_inside, "a,b,c,d,e,f", prefix="t")

print(point_dict)