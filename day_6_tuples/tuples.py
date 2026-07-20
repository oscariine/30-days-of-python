'''
Exercises: Level 1
Create an empty tuple
Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
Join brothers and sisters tuples and assign it to siblings
How many siblings do you have?
Modify the siblings tuple and add the name of your father and mother and assign it to family_members
'''


empty_tuple = ()

siblings_boy = ('john', 'atom', 'jake')
sibling_girl = ('stacey', 'jess', 'olivia')

siblings = siblings_boy + sibling_girl

print(siblings)
print(len(siblings))


parents = ('dad', 'mom')

family_members = siblings + parents

print(family_members)

sib_1, sib_2, sib_3, sib_4, sib_5, sib_6, *rest = family_members

print(sib_1)
print(sib_2)
print(sib_3)
print(sib_4)
print(sib_5)
print(rest)
'''
Exercises: Level 2
Unpack siblings and parents from family_members
Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
Change the about food_stuff_tp tuple to a food_stuff_lt list
Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
Slice out the first three items and the last three items from food_stuff_lt list
Delete the food_stuff_tp tuple completely
Check if an item exists in tuple:
Check if 'Estonia' is a nordic country

Check if 'Iceland' is a nordic country

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')


'''
fruits = ('orange', 'apple')
veggies = ('pickle', 'tomato')
animal_p = ('litterbox', 'bed')

food_stuff_tp = fruits + veggies + animal_p
print(food_stuff_tp)

food_stuff_tp = list(food_stuff_tp)

print(food_stuff_tp)

middle = food_stuff_tp[2:3]
print(middle)

first_th = food_stuff_tp[0:3]
print(first_th)

last_th = food_stuff_tp[-3:]
print(last_th)

del food_stuff_tp


nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)