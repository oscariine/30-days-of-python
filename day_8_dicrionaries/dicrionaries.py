'''
Create an empty dictionary called dog
Add name, color, breed, legs, age to the dog dictionary
Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
Get the length of the student dictionary
Get the value of skills and check the data type, it should be a list
Modify the skills values by adding one or two skills
Get the dictionary keys as a list
Get the dictionary values as a list
Change the dictionary to a list of tuples using items() method
Delete one of the items in the dictionary
Delete one of the dictionaries
'''


dog_dict = {}

dog_dict['Name'] = 'Jose'
dog_dict['Color'] = 'Black'
dog_dict['Breed'] = 'Poodle'
dog_dict['legs'] = '4'
dog_dict['age'] = '2'


print(dog_dict)

student_dic = {
    'first_name':'Oscar',
    'last_name':'jay',
    'gender':'Male',
    'age':'21',
    'starus':'Taken',
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'addy':{
        'street':'Gay Street',
        'zipcode':'6969'
    }
}

print(student_dic)
print(len(student_dic))
print(len(student_dic['skills']))
print(type(student_dic['skills']))

student_dic['skills'].append('java')

keys = list(student_dic.keys())
print(keys)

values = list (student_dic.values())
print(values)

student_items = list(student_dic.items())
print(student_items)
student_dic.pop('age')
print(student_dic)

del dog_dict