"# cpsc476proj1" 

Terminal:
python3

>>> from yourapplication import init_db
>>> init_db()


Powershell:
$env:FLASK_APP = "proj1.py"
flask run

Mac Terminal:
export FLASK_APP=proj1.py
python3 -m flask run

To run in browser:
http://localhost:5000/forums


curl -i -H "Content-Type: application/json" -X POST -d '{"name":"test"}' http://localhost:5000/forum

Reference:
https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
