import requests
import json
import base64
from gtts import gTTS

KEY = "***input your google vision cloud key here***"

#given an image
img = open(r"C:\Users\Administrator\Pictures\honda.jpg", "rb")
def encode_image(image):
  image_content = image.read()
  return base64.b64encode(image_content)


#for the convience of debugging we fetch 3 results#
req = {
	"requests": {
		"image":{
			"content": encode_image(img).decode()
		},
		"features":{
          "type":"LABEL_DETECTION",
          "maxResults":3
        }
	}
}




data = json.dumps(req)
r = requests.post("https://vision.googleapis.com/v1/images:annotate?key="+KEY, data)
print (r.url)
print (r.text)
result = r.json()["responses"][0]["labelAnnotations"][0]["description"]

tts = gTTS(text=result, lang='en', slow=False)
tts.save("result.mp3")

