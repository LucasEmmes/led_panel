from flask import Flask, redirect, url_for, render_template, request
import led_control

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def color():
    if request.method == "POST":
        r = request.form["r"]
        g = request.form["g"]
        b = request.form["b"]
        led_control.set_led(int(r), int(g), int(b))
    return render_template("led_controller.html")


if __name__=="__main__":
    app.run(debug=True)