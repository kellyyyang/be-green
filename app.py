from flask import Flask, render_template, request

import os 
from clarifai_setup import get_label

CHECKBOOK_API_KEY = os.getenv('CHECKBOOK_API_KEY')
CHECKBOOK_API_SECRET = os.getenv('CHECKBOOK_API_SECRET')

import requests

app = Flask(__name__)


def create_image(url):
    img_data = requests.get(url).content
    with open('static/media/imgs/imgs.jpg', 'wb') as handler:
        handler.write(img_data)


@app.route('/')
def index():
    return render_template('index.html') 

# Used to send HTML form data to the server. 

@app.route('/results',methods=['POST'])
def getvalue():
    url = request.form['link']
    create_image(url)
    name, co2 = get_label(url)
    return render_template('result.html', results = name)

# Used to send donations using Checkbook API
@app.route('/', methods=['GET', 'POST'])
def send_checkbook():
    url = "https://sandbox.checkbook.io"
    digital_url_path = '/v3/check/digital'

    if request.method == 'POST':
        # Get the form data
        form_data = request.form

        # Define the headers for the API request
        headers = {
            'Content-Type': 'application/json',
            "accept": "application/json",
            'Authorization': CHECKBOOK_API_KEY + ':' + CHECKBOOK_API_SECRET
        }
        # Define the request body for the API request
        request_body = {
            "recipient": form_data['email'],
            "name": form_data['name'],
            "amount": form_data['amount'],
            "description": form_data['description']
        }

        # Make a post request to the 3rd party API
        response = requests.post(url + digital_url_path, json=request_body, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            # Process the API response
            # ...
            # Return a response
            return 'Form submitted successfully!'
        else:
            # Return an error message
            return 'An error occurred while submitting the form.'
    # If the request is a GET request, render the form template
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=False)





