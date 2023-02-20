
import requests


url = 'http://127.0.0.1:7418/static/me.jpg'
r = requests.get(url, allow_redirects=True)


if (r.status_code==200):
    open('me.jpg', 'wb').write(r.content)
else:
    print ('there is no picture')