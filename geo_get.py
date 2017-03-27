import os
import time
import datetime
import json
import requests
import exifread
from clarifai import rest
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

  # The client takes the `APP_ID` and `APP_SECRET` you created in your Clarifai
  # account. You can set these variables in your environment as:
def getConceptsinImage( imageinput ):
	CLARIFAI_APP_ID = 'Re11ornY9K5Hd06foa9uCknPoaEY9y0w0MpHcGTa'
	CLARIFAI_APP_SECRET = 'XMEAHfXNyfA8TM1x76F1jQKJWcl7zBLRdFJuIdSN'
	app = ClarifaiApp(app_id=CLARIFAI_APP_ID,app_secret=CLARIFAI_APP_SECRET)
	model = app.models.get('general-v1.3')
	res = app.tag_files([imageinput])

	probconcept = {}
	for output in res['outputs']:
		for data in output['data']['concepts']:
			probconcept[data['name']] = data['value']
	return probconcept
#print(res['outputs'][0]['data']['concepts'][0]['name'])

def getJsonFromImage( imageinput ):
    # call = requests.get('http://api.openweathermap.org/data/2.5/weather?lat=47&lon=-122&APPID=045d20e4a83f4fe580531981ca805215')
    # data = json.loads(call.text)
    # print data

    """f = open(imageinput, 'rb')
    tags = exifread.process_file(f)
    # print tags.keys()

    print tags['GPS GPSLongitude'].values[0].num, tags['GPS GPSLongitude'].values[1].num, tags['GPS GPSLongitude'].values[2]
    a = `tags['GPS GPSLongitude'].values[2]`
    b = a.split("/")
    c = float(b[0])/float(b[1])
    lon = tags['GPS GPSLongitude'].values[0].num + (tags['GPS GPSLongitude'].values[1].num + (c/60))/60
    lonRef = tags['GPS GPSLongitudeRef'].values.encode('ascii', 'ingore')
    a = `tags['GPS GPSLatitude'].values[2]`
    b = a.split("/")
    c = float(b[0])/float(b[1])
    lat = tags['GPS GPSLatitude'].values[0].num + (tags['GPS GPSLatitude'].values[1].num + (c/60))/60
    latRef = tags['GPS GPSLatitudeRef'].values.encode('ascii', 'ingore')
    print lat, lon

    if latRef == 'S':
        lat = lat * -1
    if lonRef == 'W':
        lon = lon * -1

    outputdic = {}

    requrl = 'http://api.openweathermap.org/data/2.5/weather?lat=' + `lat` + '&lon=' + `lon` + '&APPID=045d20e4a83f4fe580531981ca805215'
    call2 = requests.get(requrl)
    data2 = json.loads(call2.text)
    # print data2"""

    outputdic = getConceptsinImage(imageinput)

    """date = tags['EXIF DateTimeOriginal'].values.encode('ascii', 'ignore')
    print date
    utime = time.mktime(datetime.datetime.strptime(date, "%Y:%m:%d %H:%M:%S").timetuple())

    outputdic[data2['weather'][0]['main']] = 1
    outputdic[data2['weather'][0]['description']] = 1
    if data2['wind']['speed'] > 4.5:
        outputdic['windy'] = 1
    if data2['sys']['sunset'] - utime < 1800 and data2['sys']['sunset'] - utime > -1800:
        outputdic['sunset'] = 1
    if data2['sys']['sunrise'] - utime < 1800 and data2['sys']['sunrise'] - utime > -1800:
        outputdic['sunrise'] = 1
    avgTemp = (data2['main']['temp_max'] + data2['main']['temp_min'])/2
    if avgTemp < 273.15:
        outputdic['freezing'] = 1
    if avgTemp < 283.15:
        outputdic['cold'] = 1
    if avgTemp > 293.15:
        outputdic['warm'] = 1
    if avgTemp > 303.15:
        outputdic['hot'] = 1

    API_KEY = 'AIzaSyBa-6RYXtajgQ9vL2f-Y6cOP5q_mFsOSeM'

    radius_search_json = 'https://maps.googleapis.com/maps/api/place/radarsearch/json?location='+ `lat` +','+ `lon` +'&radius=100&type=type&key=' + API_KEY
    # print radius_search_json
    rsj = requests.get(radius_search_json)
    rsjt = json.loads(rsj.text)

    # print rsjt

    for place in rsjt['results']:
        place_id = place['place_id']
        place_search_json = 'https://maps.googleapis.com/maps/api/place/details/json?placeid=' + place_id + '&key=' + API_KEY
        psj = requests.get(place_search_json)
        psjt = json.loads(psj.text)
        outputdic[psjt['result']['name']] = 1
        # print psjt['result']['name']
    """
    concepts = outputdic.keys()
    probvals = outputdic.values()
    print(concepts)
    print(probvals)

    with open('hashes.json', 'w') as fp:
        json_string = json.dumps(outputdic)
        fp.write(json_string)
    
    return json_string
