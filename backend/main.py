from flask import Flask, render_template
#from data_scrapes import

app = Flask("__main__")

@app.route("/")
def index():
    return render_template("index.html", token="token")

app.run(debug=True)