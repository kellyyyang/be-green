from flask import Flask, render_template, request

from clarifai_setup import get_label

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 

# Used to send HTML form data to the server. 

@app.route('/results',methods=['POST'])
def getvalue():
    url = request.form['link']
    results = get_label(url)
    return render_template('result.html', results = results)

if __name__ == '__main__':
    app.run(debug=False)



