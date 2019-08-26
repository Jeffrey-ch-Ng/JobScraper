import flask

app = flask.Flask("__main__")

@app.route("/")
def my_index():
    return "hello"

app.run(debug=True)