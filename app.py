from flask import Flask, jsonify, request
from flask_cors import CORS
from data import *
import sys

db = data()

app = Flask(__name__)
CORS(app)


@app.route("/")
def main():
    return jsonify(db), 200


@app.route("/stars", methods=["GET"])
def search():
    anyError = False
    
    args = request.args
    name = args.get("name")
    try :
        star_data = next(item for item in db if item["star_name"] == name)
    except Exception:
        anyError = True
        pass
    else :
        pass
        
    if anyError == True:
        a = (jsonify({"data": {"distance":"Data Not Found !","gravity":"Data Not Found !","mass":"Data Not Found !","radius":"Data Not Found !","star_name":"Data Not Found !"}),404)
    else :
        a = (jsonify({"data": star_data),200)  
          
    return a


@app.route("/stars-img", methods=["GET"])
def search_img():
    args = request.args
    name = args.get("name")
    star_data = star_img(name)
    
    if star_data == "ImageNotFound":
        b = (jsonify({"img_url": star_data, "message": "Image Not Found !"}),404)
    else :
        b = (jsonify({"img_url": star_data, "message": "Success !"}),200)
    
    return b

SERVER_USE = True  # keep `False` for running it on localhost.

if SERVER_USE == True:
    if __name__ == "__main__":
        app.run(host='0.0.0.0', port=int(sys.argv[1]))
else:
    if __name__ == '__main__':
        app.run()
