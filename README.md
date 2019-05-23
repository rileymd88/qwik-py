# Qwik Py
Qwik Py is a small library of python scripts which can help automate certain tasks within a Qlik Sense Environment. The solution is based off   
Clint Carr's python wrapper for the Qlik Sense Repository Service found here: https://github.com/clintcarr/qrspy



## Installation
1. These instructions are intended for installing these scripts directly on the Qlik Sense Server
2. If you have not installed python, then download the following file and install it: https://www.python.org/ftp/python/3.7.2/python-3.7.2-amd64.exe 
3. Ensure when installing that you check the box to add Python to PATH and then click on install now
4. Clone or download this repository somewhere on your computer
5. Navigate to the qwik-py folder within a terminal and execute the following command `pip install -r requirements.txt`
6. Edit the config.py folder accordingly
7. You should now be able to run the scripts!

## Running the Scripts
- `Script Name: ` export_apps.py
- `Script Description: ` This script will automatically export ALL Qlik Sense apps and export them to a folder of your choice
- `Paramaters`
 - `filepath: ` Example) C:\Data
 - `exportData` Example) true
- `Full Script Example`: python export_apps.py C:\Data false

- `Script Name: ` export_extensions.py
- `Script Description: ` This script will automatically export ALL Qlik Sense extensions
- `Paramaters`
 - `filepath: ` Example) C:\Data
- `Full Script Example`: python export_extensions.py C:\Data

- `Script Name: ` import_apps.py
- `Script Description: ` This script will automatically import all Qlik sense apps within a folder of your choice
- `Paramaters`
 - `filepath ` Example) C:\Data
- `Full Script Example`: python import_apps.py C:\Data

- `Script Name: ` import_extensions.py
- `Script Description: ` This script will automatically import all Qlik sense extensions within a folder of your choice
- `Paramaters`
 - `filepath ` Example) C:\Data
- `Full Script Example`: python import_extensions.py C:\Data

- `Script Name: ` screenshots.py
- `Script Description: ` This script will automatically take a screenshot of all the sheets within an application of your choice and upload it into the media content of the app. **You will need to have Chrome installed for this to work.**
- `Paramaters`
 - `appId ` Example) 6df2f487-66fa-4b22-9fe5-dda791187a77
- `Full Script Example`: python screenshots.py 6df2f487-66fa-4b22-9fe5-dda791187a77