import requests
import json
import pandas as pd


def data():
    df = pd.read_csv('./gravity.csv', encoding='ISO-8859-1')
    a = df.to_json(orient="records")
    b = json.loads(a)
    return b


def star_img(star_name):
    URL = "https://images-api.nasa.gov/search?q=" + str(star_name)
    a = requests.get(URL)
    b = a.json()
    c = dict(b)
    d = c.get("collection")
    
    try :
        e = d["items"][0]
    except IndexError:
        e = ""
    else : 
        pass

    if e != "":
        df = pd.json_normalize(e)
        f = df.get("href")[0]

        g = requests.get(f)
        h = g.json()
        ia = list(h)
        j = len(ia) - 2
        k = ia[j]
        return k
    else :
        return "ImageNotFound"
