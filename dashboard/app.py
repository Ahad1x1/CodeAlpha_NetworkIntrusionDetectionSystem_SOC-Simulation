from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

FILE = "data/events.json"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/events")
def events():
    try:
        with open(FILE, "r") as f:
            data = json.load(f)
    except:
        data = []

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True, port=5000)