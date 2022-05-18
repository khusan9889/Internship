import requests

# response = requests.get("http://api.open-notify.org/astros.json")
# print(response)

query = {'lat':'45', 'lon':'180'}
response = requests.get('http://api.open-notify.org/iss-pass.json', params=query)

# Create a new resource
response = requests.post('https://httpbin.org/post', data = {'key':'value'})
# Update an existing resource
requests.put('https://httpbin.org/put', data = {'key':'value'})

#How to Authenticate to a REST API
# requests.get(
#   'https://api.github.com/user', 
#   auth=HTTPBasicAuth('username', 'password')
# )

# #most secure way to authenticate to a REST API with an access token:
# my_headers = {'Authorization' : 'Bearer {access_token}'}
# response = requests.get('http://httpbin.org/headers', headers=my_headers)


#print data
print(response.headers["date"])  