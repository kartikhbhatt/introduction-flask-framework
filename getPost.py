from flask import Flask, render_template, request

app= Flask(__name__)

@app.route("/")
def welcome():
    return "<h1>Welcome to the Flask app! this is a test</h1>"

@app.route("/index", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/form", methods=["GET"])
def form():
    return render_template("form.html")
    
@app.route("/submit", methods=["POST"])
def submit():
    name=request.form['name']
    return f"Hello, {name}!"

if __name__ == "__main__":
    app.run(debug=True)