def translate(data, d):
    faces = data.split(" ")
    faces = [face.split(",") for face in faces]

    new_points = []
    # print(points)
    for face in faces:
        a = []
        for point in face:
            a.append(point[0]+d[point[1]])
        new_points.append(a)
    # print(new_points)

    result = ""
    for face in new_points:
        for point in face:
            result += point+","
        result = result[:-1] + " "
    print(result[:-1])


d = {}
d["i"] = "h"
d["j"] = "g"
d["I"] = "H"
d["J"] = "G"
translate("tI,ti,bi tI,bI,bi bI,bi,bj bI,bJ,bj bJ,bj,tj bJ,tJ,tj tJ,tj,ti tJ,tI,ti", d)