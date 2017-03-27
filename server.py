from flask import Flask
from geo_get import getJsonFromImage
import os
import io
import Image
from array import array
app = Flask(__name__)
#app.config['SERVER_NAME'] = "0.0.0.0:80"

def readimage(path):
    count = os.stat(path).st_size / 2
    with open(path, "rb") as f:
        return bytearray(f.read())

@app.route("/")
def hello():
    #inputimage = 'img_9657.jpg'
    bytes = readimage(path+extension)
    inputimage = Image.open(io.BytesIO(bytes))
    res = getJsonFromImage(inputimage)
    return res

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80)
