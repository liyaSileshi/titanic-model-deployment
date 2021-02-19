from flask import request, json
import requests
# local url
# url = 'http://127.0.0.1:5000' # change to your url
heroku_url = 'https://titanic-model-flask.herokuapp.com'

# heroku_url = "https://git.heroku.com/titanic-model-flask.git"
# sample data
data = {'Pclass': 3
       ,'Age': 2
       ,'SibSp': 1
       ,'Fare': 50}
data = json.dumps(data)

send_request = requests.post(heroku_url, data)

print(send_request)
print(send_request.json())
# requests.get(heroku_url).json()