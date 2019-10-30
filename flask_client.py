#from __future__ import print_function
import requests
import json

#addr = 'http://localhost:5000'
addr = 'http://35.223.146.10:5000'
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
