from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)



# Pages
@app.route("/")
def home():
    # return "Hello homepage<h1>HELLO</h1>"
    # return render_template("index.html", content=name, r=2, l=["tim","jo","bill"])
    return render_template("index.html")

# @app.route("/<name>")
# def user(name):
#     return f"Hello {name}"

# @app.route("/admin")
# def admin():
#     # return redirect(url_for("home"))
#     return redirect(url_for("user", name="Admin"))

if __name__=="__main__":
    app.run(debug=True)