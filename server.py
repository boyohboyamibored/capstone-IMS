from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


if __name__ == "__main__":
    """The default port is 5000, I used a different one
    when running another flask app"""
    app.run(debug=True)
