from flask import request, Flask, render_template
import requests
from local_settings import *
app = Flask(
    __name__
)

@app.route('/')
def mars_rover_photos():
    camera_url_arg = request.args.get('camera')
    sol_url_arg = request.args.get('sol')
    camera_lst = ['FHAZ', 'RHAZ', 'MAST', 'CHEMCAM', 'MAHLI', 'MARDI', 'NAVCAM', 'PANCAM', 'MINITES']
    camera = 'FHAZ'
    sol = 1000
    if camera_url_arg and camera_url_arg.upper() in camera_lst:
        camera = camera_url_arg
    if sol_url_arg and int(sol_url_arg) <= 1000:
        sol = sol_url_arg
    url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=%s&camera=%s&api_key=%s' % (sol, camera, api_key)
    r = requests.get(url = url, params = {})
    data = r.json()
    return render_template('index.html', data=data['photos'])

if __name__ == '__main__':
    app.run(debug=True)

