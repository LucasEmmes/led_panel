from flask import Flask, redirect, url_for, render_template, request
from triangle import TriangleData
import json
from typing import List
import pickle
import threading
import led_control

thread_running = led_control.Killswitch(False)

app = Flask(__name__)


@app.route("/home/", methods=["POST", "GET"])
def home():
    if request.method=="GET":
        triangle_list = load_pickle_data()
    else:
        # parse data from post request
        # save to pickle file
        # render to leds
        pass
    # start rendering
    t = threading.Thread(target=led_control.render_loop, args=(triangle_list, thread_running))
    t.start()

    # convert data to json and send to app.html
    triangle_dict_list = [element.__dict__ for element in triangle_list]
    json_string = json.dumps(triangle_dict_list)
    return render_template("app.html", triangle_JSON = json_string)


# Load list of triangles from file
def load_pickle_data() -> List['TriangleData']:
    with open('triangle_data.pickle', 'rb') as f:
        result = pickle.load(f)
    return result

# Save list of triangles to file
def save_pickle_data(data:List['TriangleData']) -> None:
    with open('triangle_data.pickle', 'wb') as f:
        pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

@app.route("/stop")
def stop():
    global thread_running
    thread_running.kill = True
    return "Stopped"

if __name__=="__main__":
    app.run(debug=True, host="185.71.210.203")
