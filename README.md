"# cpsc476proj1"

To Initialize the DB with test data:

Powershell:
$env:FLASK_APP = "proj1.py"
clear;python -m flask initdb

Mac Terminal:
export FLASK_APP=proj1.py
clear;python3 -m flask initdb

setup
git clone https://github.com/rauldoe/cpsc476proj1
cd cpsc476proj1
git checkout yash_v2

installation:
python -m pip install flask
python -m pip install Flask-BasicAuth

python3 -m pip install flask
python3 -m pip install Flask-BasicAuth

Powershell:
$env:FLASK_APP = "proj1.py"
clear;python -m flask run

Mac Terminal:
export FLASK_APP=proj3.py
clear;python3 -m flask run

export FLASK_APP=proj1.py
clear;python3 -m flask run


curl:
curl -i -H "Content-Type: application/json" -X POST -d '{"name":"test"}' http://localhost:5000/forums

Postman:
url: http://localhost:5000/forums
method: GET
header-key: Content-Type
header-value: application/json

url: http://localhost:5000/forums
method: POST
header-key: Content-Type
header-value: application/json
body: {"name":"test"}

url: http://localhost:5000/forums/1
method: GET
header-key: Content-Type
header-value: application/json
authorization type: Basic Auth

To run in browser:
http://localhost:5000/forums

execution:
clear;python 
clear;python3

>>> 
from proj1 import forumsGet

>>> 
forumsGet()

>>>
exit()

execution2:
clear;python create_test_data.py

execution1:
clear;python
clear;python3

>>> 
from db import db

>>>
db.executeScriptPath("proj1.db", "init.sql")

>>>
exit()


Query for UUID or GUID
C:\>clear;python query.py
Usage: python3 query.py DBFILE

C:\>clear;python query.py posts0.db
Enter a query or 'q' to quit.
> select * from posts;
[{'guid': UUID('d739b00d-5afa-4c95-8038-f1e97a7c912f'), 'name': 'foo'},
 {'guid': UUID('677de53b-150c-41fe-bf6a-3cc8c55d1e4f'), 'name': 'bar'},
 {'guid': UUID('f85faa42-d2bf-4dc8-9b98-390c5ccca3d1'), 'name': 'baz'}]
> q

C:\>

Reference:
https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
