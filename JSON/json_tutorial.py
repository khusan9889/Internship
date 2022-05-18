'''DO NOT CREATE A FILE WITH JUST "json.py" NAME AS IT WON't COMPILE because of such heading... XD'''

import json

# json_string = '''
# {
#     "people": [
#         {
#             "name": "John Smith",
#             "phone": "615-555-7164",
#             "emails": ["johnsmith@bogusemail.com", "john.smith@work-place.com"] ,
#             "has licence": false
#         },
#         {
#             "name":"Jane Doe",
#             "phone":"560-555-5153 ",
#             "emails": null,
#             "has licence": true
#         }
#     ]
# }
# '''

# data = json.loads(json_string)

# for person in data['people']:
#     #print(person['name']) print each person's name
#     del person["phone"]

# new_string = json.dumps(data , indent=2,sort_keys=True) #dump() method allows us to convert a python object into an equivalent JSON object and store the result into a JSON file at the working directory

# print(new_string)






# #Manipulations with JSON where there is json in other file

with open('states.json') as f:
    data = json.load(f)

for state in data['states']:
    #print(state['name'], state['abbreviation'])
    del state['area_codes']
with open('new_states.json', 'w') as f:
    json.dump(data, f, indent=2)


