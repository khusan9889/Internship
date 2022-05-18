# a = {i:i**2 for i in range(1,11)}
# print(a)



# #Work with existing dict
# data = {
#     'Джеф Безос': '177',
#     'ИлоН МаСк': '126',
#     'бернар АрнО': '150',
#     'БиЛл ГейтС': '124',
# }
# new_data = {key.title():int(value) for key,value in data.items()}
# new_data= {}
# print(data)
# print(new_data)

users = [
    [0,"BOb", "password"],
    [1,"code", "python"],
    [2, "Stack" , "overflow"],
    [3,"username" , "1234"],
    [51,"qwerty" , "1234"],
]

# print(users[1])

new_users = {user[0]: user for user in users}
print(new_users[51])