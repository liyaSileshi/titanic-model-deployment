# Titanic Model

## To test this app
- **Option 1**
    - 🍴 Fork this repo!

- **Option 2**
    - 👯 Clone this repo to your local machine using `https://github.com/liyaSileshi/titanic-model-deployment.git`

### Quick Start

Get up and running with Titanic model:

1. Once you have the repo cloned and met all the requirements above 
```
python3 test.py
```
* ```test.py``` file has both the AWS and Heroku deployed url to test the prediction of the model against a mock data.

##########################################################
# For development only ###
## Docker run command
docker run -p 8888:8000 lstilahun/titanic-model

once it runs open:
localhost:8888
localhost:8888/hello

AWS url - http://titanic-model.us-west-1.elasticbeanstalk.com/
Heroku url - https://titanic-model-flask.herokuapp.com
