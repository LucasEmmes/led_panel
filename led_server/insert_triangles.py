from triangle import TriangleData
import pickle

def main():

    # t = TriangleData(x, y, pattern, rgb, speed, cycle, minimum, maximum, leds)

    data = [
        # TriangleData(-1, 0, "static", (255,0,255), 1, 0, 0, 0, [_ for _ in range(6,12)]),
        TriangleData(0, 0, "static", (255,0,0), 1, 0, 0, 0, [_ for _ in range(0,6)]),
        TriangleData(1, 0, "static", (255,0,255), 1, 0, 0, 0, [_ for _ in range(6,12)]),
        TriangleData(1, 1, "static", (255,0,0), 1, 0, 0, 0, [_ for _ in range(12,18)]),
        TriangleData(2, 1, "static", (255,0,255), 1, 0, 0, 0, [_ for _ in range(18,24)]),
        TriangleData(3, 1, "static", (255,0,0), 1, 0, 0, 0, [_ for _ in range(24,30)]),
        TriangleData(4, 1, "static", (255,0,255), 1, 0, 0, 0, [_ for _ in range(30,36)]),
        TriangleData(4, 2, "static", (255,0,0), 1, 0, 0, 0, [_ for _ in range(36,42)]),
    ]
    
    with open('triangle_data.pickle', 'wb') as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

if __name__=="__main__":
    main()
