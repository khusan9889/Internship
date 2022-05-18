'''response.json() returns a JSON object of the result (if the result was written in JSON format, if not it raises an error). '''
import requests
 
# Making a get request
response = requests.get('https://api.github.com')
 
# print response
print(response)
 
# print json content
print(response.json())