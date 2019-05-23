import qrspy
import os
import sys
from config import qrs

extensions = None
try:                        
    extensions = os.listdir(sys.argv[1])
except NotADirectoryError:
    print('Please enter a proper path to your extensions!')
    sys.exit()   
if extensions is not None:
    for extension in extensions:
        if '.zip' in extension:
            qrs.import_extension(sys.argv[1] + '/' + extension)         