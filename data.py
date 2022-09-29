import requests
import json
import pandas as pd


def data():
    df = pd.read_csv("./gravity.csv")
    a = df.to_json(orient="records")
    b = json.loads(a)
    return b


def star_img(star_name):
    URL = "https://images-api.nasa.gov/search?q=" + str(star_name)
    a = requests.get(URL)
    b = a.json()
    c = dict(b)
    d = c.get("collection")
    e = d["items"][0]

    df = pd.json_normalize(e)
    f = df.get("href")[0]

    g = requests.get(f)
    h = g.json()
    ia = list(h)
    j = len(ia) - 2
    k = ia[j]
    return k
