from flask import Flask, redirect, url_for, render_template, request, jsonify, flash
from werkzeug.utils import secure_filename
from operasiFile import hitungTotalFile

import pandas as pd
import numpy as np
import os
import uuid
import base64

import cekDataset as cd
import systemTraining as st
import systemTesting as uji

BASE_DIR = os.getenv("BASE_DIR")

UPLOAD_FOLDER = "data_upload"
BASE_URL = os.getenv("SERVER_URL")

anggrek_class = ["Dendrobium_Dindii", "Dendrobium_Startiotes", "Dendrobium_Taurinum"]

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# route index
@app.route("/")
def index():
    return render_template("home.html", dr=BASE_URL)

# route dataset 
@app.route("/dataset")
def dataset():
    dataset = cd.getInformasiDataset()
    return render_template("dataset.html", mData=BASE_URL, fileDindii=dataset['dataBunga'])

# route cara tambahkan dataset 
@app.route('/cara-tambahkan-dataset')
def caraTambahkanDataset():
    return render_template('cara-tambah-dataset.html', mData=BASE_URL)

# route training data 
@app.route('/training-data')
def trainingData():
    return render_template('training-data.html', mData=BASE_URL)

@app.route('/proses-cek-dataset', methods=('GET','POST'))
def prosesCekDataset():
    dataset = cd.getInformasiDataset()
    dr = {'status' : 'success', 'dataset':dataset['dataKuantitas']}
    return jsonify(dr)

@app.route('/proses-training-data', methods=('GET','POST'))
def prosesTrainingData():
    kdPengujian = uuid.uuid4()
    st.trainingProcess(kdPengujian)
    dr = {'status' : 'success', 'kdPengujian':kdPengujian}
    return jsonify(dr)

@app.route('/hasil-training/<kdPengujian>')
def hasilTraining(kdPengujian):
    return render_template('hasil-training.html', mData=BASE_URL, kdUji=kdPengujian)

@app.route('/klasifikasi')
def klasifikasi():
    return render_template('klasifikasi.html', mData=BASE_URL)

@app.route('/proses-klasifikasi', methods=('GET','POST'))
def prosesKlasifikasi():
    kdPengujian = uuid.uuid4()
    dataGambar = request.form.get("gambar")
    format, imgstr = dataGambar.split(";base64,")
    decoded_img = base64.b64decode((imgstr))
    img_file = open(str(BASE_DIR)+'/static/upload_data_uji/'+str(kdPengujian)+'.png', 'wb')
    img_file.write(decoded_img)
    img_file.close()

    hasilKlasifikaasi = uji.testingDataUji(anggrek_class, kdPengujian)

    dr = {'status' : 'success', 'hasil' : hasilKlasifikaasi}
    
    return jsonify(dr)

@app.route('/tentang-project')
def tentangProject():
    return render_template('tentang-project.html', mData=BASE_URL)

# jalankan server 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6001)