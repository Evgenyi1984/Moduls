from requests import *
r = get('https://google.com')
print(r.status_code)