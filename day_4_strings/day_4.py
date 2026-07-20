#Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
space = " "


def exercise_1():
    one = 'Thrity'
    two = 'Days'
    thr = 'of'
    quatro = 'Python'

    
    total = one +  space  + two +  space + thr + space + quatro
    print(total)


#Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
def exercise_2():
    yo = 'Coding'
    que = 'For'
    lo = 'All'

    total2 = yo + space + que + space + lo

    print(total2)
    
    
#Change all the characters to uppercase letters using upper() method.
#Change all the characters to lowercase letters using lower() method.   
#Declare a variable named company and assign it to an initial value "Coding For All".
#Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
#Cut(slice) out the first word of Coding For All string.
#Check if Coding For All string contains a word Coding using the method index, find or other methods.
#Replace the word coding in the string 'Coding For All' to Python.
'''''
Replace the word coding in the string 'Coding For All' to Python.
Change "Python for Everyone" to "Python for All" using the replace method or other methods.
Split the string 'Coding For All' using space as the separator (split()) .
"Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
'''




def exercise_3():
    company = 'Coding For All'
    print(company)
    print(len(company))
    print(company.upper())
    print(company.lower())
    print(company.capitalize().title().swapcase)
    cut_first = company[0:7]
    print(cut_first)
    
    
    sub_string = 'Coding'
    print(company.index(sub_string))
    
    print(company.replace('Coding', 'Python'))
    print(company.replace('Python','Everyone'))
    print(company.split( ))

    
    '''''
    "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
What is the character at index 0 in the string Coding For All.
What is the last index of the string Coding For All.
What character is at index 10 in "Coding For All" string.
Create an acronym or an abbreviation for the name 'Python For Everyone'.
Create an acronym or an abbreviation for the name 'Coding For All'.
Use index to determine the position of the first occurrence of C in Coding For All.
Use index to determine the position of the first occurrence of F in Coding For All.
Use rfind to determine the position of the last occurrence of l in Coding For All People.
'''''


def exercise_4():
    companies = 'Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon'
    
    print(companies.split(', '))
    
    yoo = 'Coding For All'
    
    first_let = yoo[0]
    print(first_let)
    
    last_let = yoo[-1]
    print(last_let)
    
    let_10 = yoo[10]
    print(let_10)
    
    words = yoo.split()
    
    anc = words[0][0] + words[1][0]+ words [2][0]
    
    print(anc)
    
    print(yoo.index("C"))
    print(yoo.index("F"))
    
    peoplee = "Coding For All People"
    
    print(peoplee.rfind('l'))




'''

Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
'''

    
def exercise_5():
    
    wordd = 'You cannot end a sentence with because because because is a conjunction'

    print(wordd.find('because'))
    print(wordd.rfind('because'))
    print(len('becasue because because'))
    
    thr_bec = wordd[31:54]
    print(thr_bec)

    
'''
Use the new line escape sequence to separate the following sentences.
I am enjoying this challenge.
I just wonder what is next.
Use a tab escape sequence to write the following lines.
Name      Age     Country   City
Asabeneh  250     Finland   Helsinki
Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
The area of a circle with radius 10 is 314 meters square.
Make the following using string formatting methods:
8 + 6 = 14
8 - 6 = 2
8 * 6 = 48
8 / 6 = 1.33
8 % 6 = 2
8 // 6 = 1
8 ** 6 = 262144

'''

def exercise_6():
    
    print('I am enjoying this challenge\nI just wonder what is next.')
    
    print('Name\tAge\tCountry\tCity\nOscar\t19\tUSA\tBury')
    
    radius = 10
    area = 3.14 * radius ** 2
    
    raddd = ('The area of a circle with radius {} is {:.2f} meters square.').format(radius, area)
    print(raddd)
    
    a = 8
    b = 6
    
    print('{} + {} = {}'.format(a,b, a + b))
    print('{} - {} = {}'.format(a,b, a - b))
    print('{} * {} = {}'.format(a,b, a*b ))
    print('{} / {} = {:.2f}'.format(a,b, a/b))
    print('{} % {} = {}'.format(a,b, a%b))
    print('{} // {} = {}'.format(a,b, a//b))
    print('{} ** {} = {}'.format(a,b, a**b))
  
    
    

    
    
    
exercise_6()


    
    
    




    



    

