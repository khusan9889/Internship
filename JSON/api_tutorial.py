import json
from urllib.request import urlopen


with urlopen("https://translate.google.com/?hl=ru") as response:
    source = response.read()
    
#print(source)
data = json.loads(source)

print(json.dumps(data, indent=2)) 



'''https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json'''
'''https://translate.google.com/?hl=ru'''