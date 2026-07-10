##using these exercises to just put my code on here. Will be needing to use different vars for each exercises some vars 
##will have the same var but with different numbers, code isnt meant to combine into one I will be using the test3 to run my code with each exercsie sepreatly 



age = 19
height = 6.7
complex_num = 1 + 2j


input_base = input("Enter base: ")
input_height = input("Enter height: ")
area_of_triangle = 0.5 * float(input_base) * float(input_height)

print('Area of triangle:', area_of_triangle)


#Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
input_side_a = input("Enter side a: ")
input_side_b = input("Enter side b: ")
input_side_c = input("Enter side c: ")
perimeter_of_triangle = float(input_side_a) + float(input_side_b) + float(input_side_c)
print('Perimeter of triangle:', perimeter_of_triangle)

#Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))



input_length1 = input("Length: ")
input_width1 = input("Width: ")

length = float(input_length1)
width = float(input_width1)

area_of_rectangle = length * width

print("The area is " + str(area_of_rectangle))

print("Now that we've found the area, let's find the perimeter!")

perimeter_of_rectangle = 2 * (length + width)

print("The perimeter is " + str(perimeter_of_rectangle))

#Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.

input_rad = input("Radius: ")

rad = float(input_rad)


area_of_circle = float(3.14) * rad * rad

print("The area of the circle is: " + str(area_of_circle))

print("Now that we found the area lets find the Circumfence !!")

circum = 2 * float(3.14) * rad

print(circum)
###circumference (c = 2 x pi x r) where pi = 3.14.




#Calculate the slope, x-intercept and y-intercept of y = 2x -2

m_input = input("input m:")
b_input = input ("input b: ")


x_intercept = (-float(b_input)) / (float(m_input))


print(f"\nThe slope is: {m_input}")
print(f"The y-intercept is: {b_input}")
print(f"The x-intercept is: {x_intercept}")



#Calculate the slope, x-intercept and y-intercept of y = 2x -2


x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

slope_var = (y2 - y1) / (x2 - x1)

distance_var = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

print(f"The slope is: {slope_var}")
print(f"The Euclidean distance is {distance_var}")



#Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.


x = -5
y = x**2 + 6*x + 9
print(y)

x = -4
y = x**2 + 6*x + 9
print(y)

x = -3
y = x**2 + 6*x + 9
print(y)

x = -2
y = x**2 + 6*x + 9
print(y)



#Find the length of 'python' and 'dragon' and make a falsy comparison statement.

print(len('python') != len('dragon'))


##Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')

##I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.

print('jargon' in 'I hope this course is not full of jargon.' )


#There is no 'on' in both dragon and python
print(not('on' in 'dragon' and 'on' in  'python'))


#Find the length of the text python and convert the value to float and convert it to string

python_len = len("python")

python_float = float(python_len)
print(python_float)

python_str = str(python_float)
print(python_str)

#Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?

print(10 % 2 == 0)


#
print(7 // 3 == int(2.7))

## Check if type of '10' is equal to type of 10
print(type("10") == type(10))

##Check if int('9.8') is equal to 10

print(int("9.8") == 10)

##Write a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

hours = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))

earned = hours * rate

print("Your weekly earning is ", earned )

##Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
print("This is a year to secconds converter!!!!")

years_lived = int(input("Enter the amiunt of years you have lived: "))

seconds = years_lived * 365 * 24 * 60 * 60



print("You have lived for", seconds , "seconds.")


print("1 1 1 1 1")
print("2 1 2 48 ")
print("3 1 3 9 27")
print("4 1 4 16 64")
print("5 1 5 25 125")


