from flask import Flask, redirect, url_for, render_template, request, jsonify, flash
from werkzeug.utils import secure_filename
from operasiFile import hitungTotalFile
import pandas as pd
import numpy as np
import uuid
import os
import json
import random

UPLOAD_FOLDER = 'data_upload'
BASE_URL = os.getenv('SERVER_URL')

anggrek_class = ["Dendrobium_Dindii", "Dendrobium_Startiotes", "Dendrobium_Taurinum"]

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# route index
@app.route('/')
def index():
    return render_template('home.html', mData=BASE_URL)

# route dataset 
@app.route('/dataset')
def dataset():
    tFile = {
        'dindii' : 0,
        'startiotes' : 0,
        'taurinum' : 0
    }
    path_dindi = r'static\dataset\Dendrobium_Dindii'
    path_startiotes = r'static\dataset\Dendrobium_Startiotes'
    path_taurinum = r'static\dataset\Dendrobium_Taurinum'

    all_file_dindii = os.listdir(path_dindi)
    all_file_startioes = os.listdir(path_startiotes)
    all_file_taurinum = os.listdir(path_taurinum)

    fData = []
    ord = 1
    # mapping final data ninddi 
    for x in all_file_dindii:
        tempData = {
            'filename' : x,
            'class' : 'Dendrobium_Dindii',
            'ord' : ord,
            'filename' : 'dataset/Dendrobium_Dindii/'+x
        }
        fData.append(tempData)
        ord += 1
    # mapping final data startiotes 
    for j in all_file_startioes:
        tempData = {
            'filename' : j,
            'class' : 'Dendrobium_Startiotes',
            'ord' : ord,
            'filename' : 'dataset/Dendrobium_Startiotes/'+j
        }
        fData.append(tempData)
        ord += 1
    for k in all_file_taurinum:
        tempData = {
            'filename' : k,
            'class' : 'Dendrobium_Taurinum',
            'ord' : ord,
            'filename' : 'dataset/Dendrobium_Taurinum/'+k
        }
        fData.append(tempData)
        ord += 1

    tFile['dindii'] = len(all_file_dindii)
    tFile['startiotes'] = len(all_file_startioes)
    tFile['taurinum'] = len(all_file_taurinum)

    dr = {'BASE_URL': BASE_URL}
    return render_template('dataset.html', dRes=dr, fileDindii=fData)

# route cara tambahkan dataset 
@app.route('/cara-tambahkan-dataset')
def caraTambahkanDataset():
    return render_template('cara-tambah-dataset.html')

# route training data 
@app.route('/training-data')
def trainingData():
    return render_template('training-data.html')

# jalankan server 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)