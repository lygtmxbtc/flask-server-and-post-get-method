import requests

def get():
    url = "http://127.0.0.1:5000/api/v1.0/results"
    response = requests.get(url)
    print (response.text)

if __name__ == '__main__':
    get()