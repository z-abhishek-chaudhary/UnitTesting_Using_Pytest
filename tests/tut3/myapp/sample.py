from tests.tut3.myapp.dice import roll_dice
import requests

def guess_number(num):
    result = roll_dice()
    if result == num:
        return "You won!"
    else:
        return "You lost!"


def get_ip():
    response = requests.get('https://httpbin.org/ip')
    if response.status_code == 200:
        return response.json()['origin']
