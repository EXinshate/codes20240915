from http.client import responses
from urllib import request, error
try:
    responses = request.urlopen("https://cuiqingcai.com/404")
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')