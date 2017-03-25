import os
import time
import datetime
import json
import requests
import exifread

if __name__ == "__main__":
    # call = requests.get('http://api.openweathermap.org/data/2.5/weather?lat=47&lon=-122&APPID=045d20e4a83f4fe580531981ca805215')
    # data = json.loads(call.text)
    # print data

    f = open('geotest2.jpg', 'rb')
    tags = exifread.process_file(f)
    print tags.keys()

    lon = tags['GPS GPSLongitude'].values[0].num
    lonRef = tags['GPS GPSLongitudeRef'].values.encode('ascii', 'ingore')
    lat = tags['GPS GPSLatitude'].values[0].num
    latRef = tags['GPS GPSLatitudeRef'].values.encode('ascii', 'ingore')


    if latRef == 'S':
        lat = lat * -1
    if lonRef == 'W':
        lon = lon * -1

    requrl = 'http://api.openweathermap.org/data/2.5/weather?lat=' + `lat` + '&lon=' + `lon` + '&APPID=045d20e4a83f4fe580531981ca805215'
    call2 = requests.get(requrl)
    data2 = json.loads(call2.text)
    print data2

    # date = tags['Image DateTime'].values.encode('ascii', 'ignore')
    # print date
    # utime = time.mktime(datetime.datetime.strptime(date, "%Y:%m:%d %H:%M:%S").timetuple())
    # print utime

    # print tags.keys()

    # for tag in tags.keys():
    #     if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
    #         print "Key: %s, value %s" % (tag, tags[tag])
