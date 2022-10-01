# Stars API

Stars API , get all stars in universe at one place . 

_VERSION-1_

This Stars API is made by [Junaid](https://www.abujuni.dev) . It also includes images .
![demo1](https://i.ibb.co/3fgSsfz/2846f3d21b0c.png)
_Star Data by [Junaid](https://www.abujuni.dev) ._

## Index

- Stars Data API
- Star Data Search API
- Star Images Search API
- Installation

## Star Data Search API

![demo2](https://i.ibb.co/r6dT5SS/49d466e80992.png)

```
http://127.0.0.1:5000/stars?name=Proxima Centauri
```

or

```
http://127.0.0.1:5000/stars?name=sun
```

**Return**

```
{"data":{"Distance":1.5813e-05,"Gravity":274.2691614596,"Mass":1.0,"Radius":1.0,"Star_name":"Sun"},"message":"Success !"}
```

_Note_:_Image URL's not inclued in this api , you want [Star Images Search API](#star-images-search-api) to get images for every star._

## Star Images Search API

![demo3](https://i.ibb.co/cDnL3WT/01ed951737e5.png)

```
http://127.0.0.1:5000/stars-img?name=Proxima Centauri
```

or

```
http://127.0.0.1:5000/stars-img?name=sun
```

**Return**

```
{"img_url":"http://images-assets.nasa.gov/image/PIA18906/PIA18906~thumb.jpg","message":"Success !"}
```

# Installation

- Clone this repo
- Open terminal in that cloned folder and
- Install all requirements using -> `pip install -r requirements.txt`
- Than type -> `flask run`
- You can see Star API is Launched at localhost.
  Star Data API is hosting at http://127.0.0.1:5000/

**Made By [Junaid](https://www.abujuni.dev) .**
