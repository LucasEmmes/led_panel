from flask import Flask, redirect, url_for, render_template, request
from triangle import TriangleData
import json
from typing import List
import pickle

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

if __name__=="__main__":
    app.run(debug=True)