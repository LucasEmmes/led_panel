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
        print("AAAA")
        print(list(request.form.keys()))
        print(list(request.form.values()))
        return render_template("canvas.html", td=td)
    return render_template("canvas.html", td=triangle_data)

@app.route("/console_test")
def color():
    book = {}
    book["title"] = "Dune"
    book["author"] = "Unknown"
    # return "<html><body><script>var book = "+str(book)+";\nconsole.log(book['title']);</script></body></html>"
    return render_template("console_test.html", x="var book = 12;\n")

def post_string_to_rgb(ps:str):
    r,g,b = [int(i, 16) for i in [ps.split(",")[-1][1:][x:x+2] for x in range(0, 6, 2)]]
    return r,g,b

if __name__=="__main__":
    app.run(debug=True)