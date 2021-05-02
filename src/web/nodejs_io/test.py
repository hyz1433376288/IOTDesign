import requests
import time
url = "http://localhost:5000//"
data = {"key":"value"}
while True:
    res = requests.post(url=url,data=data)
    print(res.text)
    time.sleep(1)
