#from __future__ import print_function
import requests
import json
#import cv2

addr = 'http://localhost:5000'
URL = addr + '/api/test'
headers = {'content-type': "image/jpeg"}

def post_image(img_file):
    """ post image and return the response """
    headers = {'content-type': "image/jpeg"}
    img = open(img_file, 'rb').read()
    response = requests.post(URL, data=img, headers=headers)
    return response

resp = post_image('star-1570225379993-9798.jpg')
print(json.loads(resp.text))
#img = cv2.imread('star-1570225379993-9798.jpg')
# encode image as jpeg
#_, img_encoded = cv2.imencode('.jpg', img)
# send http request with image and receive response
#response = requests.post(test_url, data=img_encoded.tostring(), headers=headers)
# decode response

# expected output: {u'message': u'image received. size=124x124'}
