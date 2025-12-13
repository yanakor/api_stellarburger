import requests

def test_get_insult():
    resp = requests.get('https://evilinsult.com/generate_insult.php?lang=en&type=json')

    print(resp.json()['insult'])