from dotenv import load_dotenv
import os

load_dotenv()

BASE_DIR = os.getenv("BASE_DIR")

print(BASE_DIR)
def getInformasiDataset():
    tFile = {
        'dindii' : 0,
        'startiotes' : 0,
        'taurinum' : 0
    }
    path_dindi = str(BASE_DIR)+'/static/dataset/Dendrobium_Dindii'
    path_startiotes = str(BASE_DIR)+'/static/dataset/Dendrobium_Startiotes'
    path_taurinum = str(BASE_DIR)+'/static/dataset/Dendrobium_Taurinum'

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

    dr = {
        'dataKuantitas' : tFile,
        'dataBunga' : fData
    }

    return dr