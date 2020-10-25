from flask import Flask, render_template
import requests
from local_settings import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/mars_rover')
def mars_rover_photos():
    url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=fhaz&api_key=%s' % api_key
    r = requests.get(url = url, params = {})
    data = r.json() 
    print('data', data)
    return render_template('index.html', name=data['photos'])

if __name__ == '__main__':
    app.run(debug=True)

