import requests
import json

def post():
    url = "http://127.0.0.1:5000/api/v1.0/results"
    postDict = {
        'postinfo' : 'test',
    }
    headers = {'Content-Type':'application/json'}
    response = requests.post(url, headers = headers, data = json.dumps(postDict))
    print (response.text)

if __name__ == '__main__':
    post()