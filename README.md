"# cpsc476proj1"

installation:
python -m pip install flask
python -m pip install Flask-BasicAuth

python3 -m pip install flask
python3 -m pip install Flask-BasicAuth

Powershell:
$env:FLASK_APP = "proj1.py"
clear;python -m flask run

Mac Terminal:
export FLASK_APP=proj1.py
clear;python3 -m flask run


curl:
curl -i -H "Content-Type: application/json" -X POST -d '{"name":"test"}' http://localhost:5000/forums

Postman:
url: http://localhost:5000/forums
method: POST
header-key: Content-Type
header-value: application/json
body: {"name":"test"}

url: http://localhost:5000/forums/1
method: GET
header-key: Content-Type
header-value: application/json

To run in browser:
http://localhost:5000/forums

execution:
clear;python or clear;python3
>>> 
from proj1 import forumsGet
>>> 
forumsGet()
>>>
exit()

clear;python or clear;python3
>>> 
from db import executeScriptPath
>>>
executeScriptPath("test.db", "init.sql")
>>>
exit()

Reference:
https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
