# dynamic url
# variables rule
# jinja2 template engine

'''
{{ variable }} -> to print variable
{% for item in list %} ... {% endfor %} -> loop, conditions
{#..#} -> comments


'''


from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def welcome():
    return "<h1>Welcome to the Flask app! this is a test</h1>"

@app.route("/index")
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
    # Handle form submission logic here
    name = request.form['name']
    return f"hello!! {name}"

@app.route("/scoreres/<int:score>")
def scoreres(score):
    res = "Pass" if score >= 50 else "Fail"
    exp = {"score":score,"result":res}
    return render_template("result1.html", result=exp)

# vairable rule: restricting variable with a dtype
@app.route("/score/<int:score>")
def score_page(score):
    
    return render_template("result.html", results=score)

if __name__ == "__main__":
    app.run(debug=True)