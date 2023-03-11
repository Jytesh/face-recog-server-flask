import requests


url = "http://127.0.0.1:5000/verify"
with open('test.jpg', 'rb') as fobj:
    response = requests.post(
        url, headers={'Token': '|n/>JOGt]5,:P4Bd?RO2Ep%'}, files={'file': fobj})
    print(response.text)
