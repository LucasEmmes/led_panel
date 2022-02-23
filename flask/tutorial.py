from flask import Flask, redirect, url_for, render_template, request
import led_control

app = Flask(__name__)

size = 200
# x,y,usd,size,color
triangle_data=f"0,0,1,{size},#FF0000;100,0,0,{size},#0000FF"


@app.route("/home/")
def home():
    return render_template("led_controller.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")


@app.route("/test", methods=["POST", "GET"])
def test():
    if request.method == "POST":
        td = request.form["triangle_1"]
        r,g,b = post_string_to_rgb(td)
        # led_control.set_led(r,g,b)
        return render_template("canvas.html", td=td)
    return render_template("canvas.html", td=triangle_data)

@app.route("/color/<c>")
def color(c):
    led_control.set_led(int(c))
    return ""

def post_string_to_rgb(ps:str):
    r,g,b = [int(i, 16) for i in [ps.split(",")[-1][1:][x:x+2] for x in range(0, 6, 2)]]
    return r,g,b

if __name__=="__main__":
    app.run(debug=True)