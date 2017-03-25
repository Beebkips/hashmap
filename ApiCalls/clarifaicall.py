  # Pip install the client:
  # pip install clarifai
  
  
  #The package will be accessible by importing clarifai:
  
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

outputdic = {}
imageinput = '/Users/vikasmohandoss/Documents/hashmap/images/IMG_0953.jpg'
outputdic = getConceptsinImage(imageinput)
concepts = outputdic.keys()
probvals = outputdic.values()
print(concepts)
print(probvals)



