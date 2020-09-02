# Site está acessível?
from urllib import request
import urllib
try:
    site = request.urlopen('https://github.com/MaksonViini')
except urllib.error.URLError:
    print('O site nao esta funcionando!')
else:
    print('Tudo ok !')
