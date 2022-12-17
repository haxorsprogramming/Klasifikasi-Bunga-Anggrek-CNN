from flask import Flask, redirect, url_for, render_template, request, jsonify, flash
from werkzeug.utils import secure_filename
import pandas as pd
import numpy as np
import uuid
import os
import json
import random

UPLOAD_FOLDER = 'data_upload'
BASE_URL = "http://127.0.0.1:5000/"

anggrek_class = ["Dendrobium_Dindii", "Dendrobium_Startiotes", "Dendrobium_Taurinum"]

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    dr = {'BASE_URL': BASE_URL}
    return render_template('home.html', dRes=dr)

@app.route('/training-data')
def trainingData():
    dr = {'BASE_URL': BASE_URL}
    return render_template('training-data.html', dRes=dr)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)