import shutil
import os
from config import *
import sys

try:
    os.listdir(sys.argv[1])
    print(sys.argv[1])
except NotADirectoryError:
    print('Please enter a proper export path for your apps!') 
    sys.exit()  
extensions = qrs.get_extension()


