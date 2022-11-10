# echo-server

## Endpoints

Method: Get

`http://localhost:8080/`

Returns

`{"status": "alive"}`

<hr>


Method: Post

`http://localhost:8080/echo`

Returns

`{"received": <JSON payload>}`

<hr>

## To run/test on Mac/Linux

`python -m venv venv`

`source venv/bin/activate`

`pip install -r requirements.txt`

`python app.py`

To test `/` endpoint:

`curl http://localhost:8080/`

To test `/echo` endpoint:

`curl -d '{"data": 1}' -H 'Content-Type: application/json' http://localhost:8080/echo`
