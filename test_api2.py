# -*- coding: utf-8 -*-
import base64
import json
import requests
import os
from PIL import Image

host = "http://10.108.4.161:9898"

path = os.path.abspath(os.path.dirname(__file__))
fileList = os.listdir(path + '/auth')
for i in fileList:
    #convert file to jpeg file
    im = Image.open(path + '/auth/' + i)
    new_filename = i.split('.')[0] + '.jpg'
    im.save(path + '/auth/' + new_filename)

    #test ocr
    file = open(path + '/auth/' + new_filename, 'rb').read()
    api_url = f"{host}/ocr/b64/json"
    resp = requests.post(api_url, data=base64.b64encode(file).decode())
    ocr = json.loads(resp.text)['result']
    print(f"filename={new_filename},ocr={ocr} {api_url=}, {resp.text=}")
