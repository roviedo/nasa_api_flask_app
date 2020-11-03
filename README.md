### Python Flask project using NASA's API
##### This is project using mostly vanilla javascript and html and css, only the Masonry library from https://masonry.desandro.com is used as the layout to render the Mars Rover photos. 
##### Also, this project is done making the request for the photos intentionally in the backend as opposed to client side, this causes having to reload the page everytime that new filtering is selected.

##### Make sure you have requested your api key from https://api.nasa.gov/ in the Generate API key section.

#### Requirements
    1. Python 3.X

#### Setup and running this project
    1. cd /path/to/nasa_api_app
    2. python -m venv my_python_env
    3. source /path/to/my_python_env
    4. pip install -r requirements.txt
    5. Create a local_settings.py file
    6. add api_key = 'YOUR_API_KEY' and save file
    5. python main.py
    6. Go to your favorite browser http://localhost:5000