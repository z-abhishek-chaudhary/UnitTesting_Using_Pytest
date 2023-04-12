import requests, random
import time

def silly():
    params = {
        "timestamp" : time.time(),
        "number" : random.randint(1,6)
    }
    response = requests.get('https://httpbin.org/get', params)
    if response.status_code == 200:
        return response.json()['args']
    

print(silly())