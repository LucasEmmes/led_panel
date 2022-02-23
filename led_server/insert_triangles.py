from triangle import TriangleData
import pickle

def main():

    # t = TriangleData(x, y, pattern, rgb, speed, cycle, minimum, maximum, leds)
    t1 = TriangleData(0, 0, "static", (255,0,0), 1, 0, 0, 100, [0,1,2,3,4,5])
    t2 = TriangleData(1, 0, "static", (0,0,255), 1, 0, 0, 100, [6,7,8,9,10,11])
    t3 = TriangleData(2, 0, "static", (0,255,0), 1, 0, 0, 100, [12,13,14,15,16,17])

    data = [t1,t2,t3]
    with open('triangle_data.pickle', 'wb') as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

if __name__=="__main__":
    main()