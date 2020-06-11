import json

person_dict = {'first':'raghu','last':'channappa','age':45,'role':'architect'}
person_dict['city'] = 'Atlanta'

languages_list = ['Python','C++','C','Java']
person_dict['languages'] = languages_list

manager_dict = {}
manager_dict['AVP'] = person_dict

person_json = json.dumps(person_dict)
manager_json = json.dumps(manager_dict)

print(person_json)
print()
print(manager_json)