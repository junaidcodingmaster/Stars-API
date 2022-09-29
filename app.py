from flask import Flask, jsonify, request
from data import *

db = data()

app = Flask(__name__)


@app.route("/")
def main():
    return jsonify(db), 200


@app.route("/stars", methods=["GET"])
def search():
    args = request.args
    name = args.get("name")
    star_data = next(item for item in db if item["Star_name"] == name)
    return jsonify({"data": star_data, "message": "Success !"})


@app.route("/stars-img", methods=["GET"])
def search_img():
    args = request.args
    name = args.get("name")
    star_data = star_img(name)
    return jsonify({"img_url": star_data, "message": "Success !"})


if __name__ == "__main__":
    app.run(debug=True)
