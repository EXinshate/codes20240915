from http.client import responses
from urllib.parse import urlsplit

result = urlsplit('https://www.baidu.com/index.html;user?id=5#commment')
print(result)