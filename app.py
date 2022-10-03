from flask import Flask, jsonify, request
from data import *

db = data()

app = Flask(__name__)


@app.route("/")
def main():
    return jsonify(db), 200


@app.route("/stars", methods=["GET"])
def search():
    anyError = False
    
    args = request.args
    name = args.get("name")
    try :
        star_data = next(item for item in db if item["Star_name"] == name)
    except Exception:
        anyError = True
        pass
    else :
        pass
        
    if anyError == True:
        a = (jsonify({"data": "Data Not Found !", "message": "Data Not Found !"}),404)
    else :
        a = (jsonify({"data": star_data, "message": "Success !"}),200)  
          
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


if __name__ == '__main__':
    app.run()
