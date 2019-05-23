import shutil
import os
from config import *
import sys
import shutil


try:
    listdir = os.listdir(sys.argv[1])
except:
    print('Please enter a proper export path for your apps!') 
    sys.exit()
try:
    qliksharedir = os.listdir(qlikShare + '/StaticContent/Extensions')
except:
    print('Please enter a proper qlik share path in the config.py file!')
try:
    for ext in qliksharedir:
        try:
            os.listdir(qlikShare + '/StaticContent/Extensions/' + ext)
            shutil.make_archive(sys.argv[1]+'/'+ext, 'zip', qlikShare + '/StaticContent/Extensions/' + ext)
            print('Successfully exported ' + ext)
        except Exception as e:
            print(e)
            pass   
except:
    pass                  

