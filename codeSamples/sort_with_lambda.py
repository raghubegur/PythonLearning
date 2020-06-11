# sorting using custom key
employees = [
    {'Name': 'Corneel Boysen', 'age': 52, 'salary': 10000},
    {'Name': 'Abel Talbot', 'age': 35, 'salary': 8000},
    {'Name': 'Don Eddleman', 'age': 55, 'salary': 1000},
    {'Name': 'Raghu Channappa', 'age': 45, 'salary': 15000},
]

# sort by name (Ascending order)
employees.sort(key=lambda x: x.get('Name'))
print(employees, end='\n\n')

# sort by Age (Ascending order)
employees.sort(key=lambda x: x.get('age'))
print(employees, end='\n\n')

# sort by salary (Descending order)
employees.sort(key=lambda x: x.get('salary'), reverse=True)
print(employees, end='\n\n')

# sort by length of the name
employees.sort(key=lambda x: len(x['Name']))
print(employees, end='\n\n')
