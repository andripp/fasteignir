import requests

r = requests.get('http://fasteignir.visir.is/api/search?onpage=1000&page=1&zip=103')
r.status_code
r.headers['content-type']
r.encoding
r.text
r.json()