from flask import Flask, redirect, url_for, render_template, request
import led_control

app = Flask(__name__)



# Pages
@app.route("/")
def home():
    # return "Hello homepage<h1>HELLO</h1>"
    # return render_template("index.html", content=name, r=2, l=["tim","jo","bill"])
    return render_template("index.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["nm"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

@app.route("/color/<c>")
def color(c):
    led_control.set_led(int(c))
    return ""

if __name__=="__main__":
    app.run(debug=True)