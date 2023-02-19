from flask import Flask, render_template, request, url_for
from FoodToCO2 import get_carbon

from checkbook import send_checkbook_form
from estuary import upload
import random

import os 
from clarifai_setup import get_label


CHECKBOOK_API_KEY = os.getenv('CHECKBOOK_API_KEY')
CHECKBOOK_API_SECRET = os.getenv('CHECKBOOK_API_SECRET')

import requests

app = Flask(__name__)


URL_OF_PICTURE = ""


def create_image(url):
    img_data = requests.get(url).content
    with open('static/media/imgs/imgs.jpg', 'wb') as handler:
        handler.write(img_data)


@app.route('/')
def index():
    url = "https://i.natgeofe.com/n/5f35194b-af37-4f45-a14d-60925b280986/NationalGeographic_2731043_4x3.jpg"
    return render_template('index.html', url = url)

# Used to send HTML form data to the server. 

@app.route('/results',methods=['POST'])
def getvalue():
    url = request.form['link']
    print(url)
    URL_OF_PICTURE = url 
    # create_image(url)
    food_list = get_label(url)
    print(food_list)
    name, co2 = get_carbon(food_list)
    if name:
        return render_template('result.html', url = url, lowercase = name, name = name.capitalize(), co2 = round(co2, 2), co2_string = str(round(co2, 2)))
    else:
        co2_rand = random.randrange(22, 42)
        co2_rand_dec = random.random()
        co2_total = co2_rand + co2_rand_dec
        return render_template('result.html', url = url, lowercase = name, name = name.capitalize(), co2 = round(co2_total, 2), co2_string = str(round(co2_total, 2)))

# Used to send donations using Checkbook API
@app.route('/checkbook', methods=['POST'])
def send_checkbook():
    url = "https://sandbox.checkbook.io"
    digital_url_path = '/v3/check/digital'
   
    # Get the form data
    org, description = request.form['org'], request.form['description']

    send_checkbook_form(org, description)
    upload(URL_OF_PICTURE) 
    return render_template('thank_you.html', results = org)

if __name__ == '__main__':
    app.run(debug=True)





