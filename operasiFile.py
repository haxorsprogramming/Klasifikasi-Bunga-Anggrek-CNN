import os

def hitungTotalFile(pathDir):
    tFile = 0    
    for path in os.listdir(pathDir):
        # check if current path is a file
        if os.path.isfile(os.path.join(pathDir, path)):
            tFile += 1
    return tFile