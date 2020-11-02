from flask import request, Flask, render_template
import requests
from local_settings import *
app = Flask(
    __name__
)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/mars_rover')
def mars_rover_photos():
    camera_url_arg = request.args.get('camera')
    camera_lst = ['FHAZ', 'RHAZ', 'MAST', 'CHEMCAM', 'MAHLI', 'MARDI', 'NAVCAM', 'PANCAM', 'MINITES']
    camera = 'FHAZ'
    if camera_url_arg and camera_url_arg.upper() in camera_lst:
        camera = camera_url_arg
    print('############ camera', camera)
    url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&camera=%s&api_key=%s' % (camera, api_key)
    r = requests.get(url = url, params = {})
    data = r.json() 
    print('data', data)
    return render_template('index.html', data=data['photos'])

if __name__ == '__main__':
    app.run(debug=True)

