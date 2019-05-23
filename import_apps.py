import qrspy
import os
import sys
from config import qrs


try:                        
    apps = os.listdir(sys.argv[1])
except NotADirectoryError:
    print('Please enter a proper path to your apps!')

for app in apps:
    if '.qvf' in app:
        try:
            qrs.import_app(app.split('.qvf')[0], sys.argv[1] + '/' + app)
            print('Sucessfully imported ' + app)
        except Exception as e:
            print('There was an error importing ' + app, e)
print('done!')            

        