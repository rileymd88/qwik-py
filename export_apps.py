import qrspy
import os
import sys
from config import qrs 

try:
    os.listdir(sys.argv[1])
except NotADirectoryError:
    print('Please enter a proper export path for your apps!') 
    sys.exit()  
apps = qrs.get_app()
for app in apps:
    try:
        qrs.new_export_app(app['id'], sys.argv[1], app['name'] + '.qvf', sys.argv[2])
        print('Sucessfully Exported ' + app['name'])
    except Exception as e:
        print('There was an error exporting ' + app['name'], e)        
print('done!')