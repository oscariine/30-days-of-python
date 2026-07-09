# Day 2: 30 Days of python programming

first_name = "John"
last_name = "Doe"
full_name = "John Doe"
country = "USA"
city = "New York"
age = 25
year = 2026
is_married = False
is_true = True
is_light_on = True

# Assigning a value means storing data in a variable.
# Example: x = 10 means the variable x now holds the value 10.

# Multiple variables on one line means declaring several variables in a single line.
# Example: a, b, c = 1, 2, 3
first_name, last_name, country = "John", "Doe", "USA"



#excersise 2


type(first_name)  # Output: <class 'str'>
type(age)         # Output: <class 'int'>           
type(is_married)  # Output: <class 'bool'>
type(is_light_on)  # Output: <class 'bool'>
type(year)        # Output: <class 'int'>

len(first_name)  # Output: 4
len(last_name)   # Output: 3
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
modulus = num_one % num_two
power = num_one ** num_two
floor = num_one // num_two

rad_of_circle = 30
area_of_circle = 3.14 * rad_of_circle ** 2
circumference_of_circle = 2 * 3.14 * rad_of_circle
input_radius = input("Enter radius: ")
area_of_circle = 3.14 * float(input_radius) ** 2

first_name = input("What is your name? ")
last_name = input("What is your last name? ")
country = input("What is your country? ")
age = int(input("What is your age? "))