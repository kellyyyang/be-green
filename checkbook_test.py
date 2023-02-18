import requests
import os
from dotenv import load_dotenv
load_dotenv()

CHECKBOOK_API_KEY = os.getenv('CHECKBOOK_API_KEY')
CHECKBOOK_API_SECRET = os.getenv('CHECKBOOK_API_SECRET')

url = "https://sandbox.checkbook.io"

payload = {
    "recipient": "testing@checkbook.io",
    "name": "Widgets Inc.",
    "amount": 5,
    "description": "Test Payment"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "Authorization": CHECKBOOK_API_KEY + ':' + CHECKBOOK_API_SECRET
}

response = requests.post(url + '/v3/check/digital', json=payload, headers=headers)

print(response.text)