'''
Iterate 0 to 10 using for loop, do the same using while loop.

Iterate 10 to 0 using for loop, do the same using while loop.
'''



#for x in range(1,11):
 #   print(x)
    
#for y in range(10,1,-1):
  #  print(y)
  
'''
Write a loop that makes seven calls to print(), so we get on the output the following triangle:
'''


#for num in range(1,8):
  #  print("#" * num )
  
  
  
"""
Use nested loops to create the following:

# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #

for row in range(8):
    for column in range (8):
        print("#", end=" ")
    print()
"""


'''
0 x 0 = 0
1 x 1 = 1
2 x 2 = 4
3 x 3 = 9
4 x 4 = 16
5 x 5 = 25
6 x 6 = 36
7 x 7 = 49
8 x 8 = 64
9 x 9 = 81
10 x 10 = 100


for num in range(11):
    print(f'{num} x {num} = {num * num}')
    
'''

'''
comp = ['Python', 'Numpy','Pandas','Django', 'Flask'] 

for x in comp:
    print(x)

'''
'''
total_even = 0
total_odd = 0 
for num in range(0,101, +2):
    total_even += num
for numm in range(1 ,100, 2):
    total_odd += numm
print(f'The sum of all evens is {total_even}. And the sum of all odds is {total_odd}.')


    
 
  

total = 0
for x in range(0,101):
    total += x
print(total)
'''
'''
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]

for x in countries:
    if 'land' in x:
        print(x)
    
'''

'''
fruits = ['banana', 'orange', 'mango', 'lemon']

for x in range(len(fruits)- 1, -1, -1 ):
    print(fruits[x])
'''

'''
    "name": "Afghanistan",
        "capital": "Kabul",
        "languages": [
            "Pashto",
            "Uzbek",
            "Turkmen"
        ],
        "population": 27657145,
        "flag": "https://restcountries.eu/data/afg.svg",
        "currency": "Afghan afghani"
'''

'''

from countries_data import countriess


# 1. Total number of language entries

count_lang = 0

for country in countriess:
    for language in country["languages"]:
        count_lang += 1

print(f"The total number of language entries is: {count_lang}")


# 2. Ten most spoken languages

language_counts = {}

for country in countriess:
    for language in country["languages"]:

        if language in language_counts:
            language_counts[language] += 1
        else:
            language_counts[language] = 1

sorted_languages = sorted(
    language_counts.items(),
    key=lambda item: item[1],
    reverse=True
)

top_ten_languages = sorted_languages[:10]

print("\nThe 10 most spoken languages are:")

for language, count in top_ten_languages:
    print(language, count)


# 3. Ten most populated countries

sorted_countries = sorted(
    countriess,
    key=lambda country: country["population"],
    reverse=True
)

top_ten_countries = sorted_countries[:10]

print("\nThe 10 most populated countries are:")

for country in top_ten_countries:
    print(country["name"], country["population"])
    
    
    
matrix = [

    [1, 2],

    [3, 4]

]

for row in matrix:

    for number in row:

        print(number)
        
'''




word = "programming"
vowel_count = 0
for letter in word:
    if letter.lower() in 'aeiou':
        vowel_count += 1
print(f'The word contains {vowel_count} vowels')
        


    
    
    
    # ==========================================
# Exercise 1 - Print Every Number
# ==========================================

numbers = [4, 8, 15, 16, 23, 42]

for number in numbers:
    print(number)


# ==========================================
# Exercise 2 - Find the Sum
# ==========================================

numbers = [4, 8, 15, 16, 23, 42]

total = 0

for number in numbers:
    total += number

print(f"The sum is {total}")


# ==========================================
# Exercise 3 - Print Even Numbers
# ==========================================

numbers = [4, 8, 15, 16, 23, 42]

for number in numbers:
    if number % 2 == 0:
        print(number)
    else:
        print(f"{number} is an odd number")


# ==========================================
# Exercise 4 - Count Even Numbers
# ==========================================

numbers = [4, 8, 15, 16, 23, 42]

even_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count += 1

print(f"There are {even_count} even numbers.")


# ==========================================
# Exercise 5 - Find the Largest Number
# ==========================================

numbers = [4, 8, 15, 16, 23, 42]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print(f"The largest number is {largest}")


# ==========================================
# Exercise 6 - Find the Smallest Number
# ==========================================

numbers = [4, 8, 15, 16, 23, 42]

smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number

print(f"The smallest number is {smallest}")


# ==========================================
# Exercise 7 - Find Largest and Smallest
# ==========================================

numbers = [4, 8, 15, 16, 23, 42]

largest = numbers[0]
smallest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

    if number < smallest:
        smallest = number

print(f"The largest number is {largest}")
print(f"The smallest number is {smallest}")


# ==========================================
# Exercise 8 - Count Vowels
# ==========================================

text = "Hello World"

vowel_count = 0

for letter in text:
    if letter.lower() in "aeiou":
        vowel_count += 1

print(f"There are {vowel_count} vowels.")


# ==========================================
# Exercise 9 - Print Each Row
# ==========================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    print(row)


# ==========================================
# Exercise 10 - Print Every Number
# ==========================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for number in row:
        print(number)


# ==========================================
# Exercise 11 - Sum Every Number
# ==========================================

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

total = 0

for row in matrix:
    for number in row:
        total += number

print(f"The total is {total}")

    
    
    