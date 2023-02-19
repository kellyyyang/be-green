import requests
import os
from dotenv import load_dotenv
load_dotenv()

CHECKBOOK_API_KEY = os.getenv('CHECKBOOK_API_KEY')
CHECKBOOK_API_SECRET = os.getenv('CHECKBOOK_API_SECRET')

ORG_TO_NAME = {'org1': 'International Food Policy Research Institute',
               'org2': 'Food and Agriculture Organization',
               'org3': 'The Land Institute'}

def send_checkbook_form(org, description=''):

       email = 'vsachdev@g.hmc.edu'
       name = ORG_TO_NAME[str(org)]
       amount = 1.0
       description = str(description)

       url = "https://sandbox.checkbook.io"

       payload = {
       "recipient": email,
       "name": name,
       "amount": amount,
       "description": description
       }
       headers = {
       "accept": "application/json",
       "content-type": "application/json",
       "Authorization": CHECKBOOK_API_KEY + ':' + CHECKBOOK_API_SECRET
       }

       response = requests.post(url + '/v3/check/digital', json=payload, headers=headers)

       print(response.text)