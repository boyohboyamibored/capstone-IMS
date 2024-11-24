"""Import the app so we can run it"""

from noobIMS import app

if __name__ == "__main__":
    """The default port is 5000, I use a different one
    when running another flask app"""
    app.run(debug=True)
