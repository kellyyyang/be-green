from flask import Flask, render_template, request
from FoodToCO2 import get_carbon

from checkbook import send_checkbook_form
from estuary import upload

import os 
from clarifai_setup import get_label

CHECKBOOK_API_KEY = os.getenv('CHECKBOOK_API_KEY')
CHECKBOOK_API_SECRET = os.getenv('CHECKBOOK_API_SECRET')

import requests

app = Flask(__name__)


def create_image(url):
    img_data = requests.get(url).content
    with open('static/media/imgs/imgs.jpg', 'xb') as handler:
        handler.write(img_data)


@app.route('/')
def index():
    return render_template('index.html')

# Used to send HTML form data to the server. 

@app.route('/results',methods=['POST'])
def getvalue():
    url = request.form['link']
    create_image(url)
    food_list = get_label(url)
    name, co2 = get_carbon(food_list)
    return render_template('result.html', lowercase = name, name = name.capitalize(), co2 = round(co2, 3), co2_string = str(round(co2, 3)))

# Used to send donations using Checkbook API
@app.route('/checkbook', methods=['POST'])
def send_checkbook():
    url = "https://sandbox.checkbook.io"
    digital_url_path = '/v3/check/digital'
   
    # Get the form data
    org, description = request.form['org'], request.form['description']

    send_checkbook_form(org, description)
    upload() 
    return render_template('thank_you.html', results = org)

if __name__ == '__main__':
    app.run(debug=False)





