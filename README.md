![logo](./logo.png)
[![Made with Python](https://img.shields.io/badge/Made%20with-Python-blueviolet.svg)](https://www.python.org/)
[![Version](https://img.shields.io/badge/version-2.2-green.svg)](https://github.com/junaidcodingmaster/Stars-API)
# Stars API ⭐🌟

Get all the stars in the universe at one place with the Stars API. 

This is the latest version of the Stars API :  ![Stars API Version](https://img.shields.io/github/v/release/junaidcodingmaster/Stars-API)

This API was created by [Junaid](https://www.abujuni.dev) and includes images.

Check out a demo:

![Star Data Demo](https://i.ibb.co/3fgSsfz/2846f3d21b0c.png)
_Star Data by [Junaid](https://www.abujuni.dev)_

The API is now live at:
- https://starsapi.abujuni.dev
- https://stars-api.onrender.com

## Table of Contents

- [Star Data API](#star-data-api)
- [Star Data Search API](#star-data-search-api)
- [Star Images Search API](#star-images-search-api)
- [Installation](#installation)

## Star Data API

Get a JSON list of all the stars in the universe by visiting the index page:
```
http://127.0.0.1:5000
```
This API is perfect for creating a flatlist in a React app.

## Star Data Search API

Get specific star data by searching by name:
```
http://127.0.0.1:5000/stars?name=proxima centauri
```
Or
```
http://127.0.0.1:5000/stars?name=sun
```

Example return:
```
{"data":{"Distance":1.5813e-05,"Gravity":274.2691614596,"Mass":1.0,"Radius":1.0,"Star_name":"Sun"},"message":"Success !"}
```

## Star Images Search API

Get an image of a specific star by searching by name:
```
http://127.0.0.1:5000/stars-img?name=proxima centauri
```
Or
```
http://127.0.0.1:5000/stars-img?name=sun
```

Example return:
```
{"img_url":"http://images-assets.nasa.gov/image/PIA18906/PIA18906~thumb.jpg","message":"Success !"}
```


## Installation

To use the Stars API on your local machine, follow these steps:
- Clone this repo
- Open terminal in the cloned folder
- Install requirements using `pip install -r requirements.txt`
- Run the API using `flask run`
- The API will be live at http://127.0.0.1:5000/

Made with ❤️ by [Junaid](https://www.abujuni.dev).
