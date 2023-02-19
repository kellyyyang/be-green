import requests
import os
from dotenv import load_dotenv
load_dotenv()

ESTUARY_API_KEY = os.getenv('ESTUARY_API_KEY')

import requests

def upload():

    url = "https://api.estuary.tech/content/add"

    payload={}
    files=[
    ('data',('file',open('static/media/imgs/imgs.jpg','rb'),'application/octet-stream'))
    ]
    headers = {
    'Accept': 'application/json',
    'Authorization': ESTUARY_API_KEY
    }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)

upload()