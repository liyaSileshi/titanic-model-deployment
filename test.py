from flask import request, json
import requests
# local url
url = 'http://127.0.0.1:8888' # change to your url
# docker_url = "http://0.0.0.0:8000"
# heroku_url = 'https://titanic-model-flask.herokuapp.com'
aws_url = "http://titanic-model.us-west-1.elasticbeanstalk.com/"
# sample data
data = {'Pclass': 3
       ,'Age': 2
       ,'SibSp': 1
       ,'Fare': 50}
data = json.dumps(data)

send_request = requests.post(aws_url, data)

print(send_request)
print(send_request.json())
