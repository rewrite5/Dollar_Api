from flask import Flask
from scrapper import Scrapper
import json

app = Flask(__name__)


@app.route('/')
def index():
    
    dollar = Scrapper()
    return json.dumps(dollar.get_dictionary())


app.run(host='0.0.0.0', port=5000)
