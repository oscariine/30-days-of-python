print("\nExercise 1A - Count from 0 to 10 with a for loop")

for number in range(11):
    print(number)


print("\nExercise 1B - Count from 0 to 10 with a while loop")

number = 0

while number <= 10:
    print(number)
    number += 1


print("\nExercise 2A - Count from 10 to 0 with a for loop")

for number in range(10, -1, -1):
    print(number)


print("\nExercise 2B - Count from 10 to 0 with a while loop")

number = 10

while number >= 0:
    print(number)
    number -= 1


print("\nExercise 3 - Seven-row triangle")

for number in range(1, 8):
    print("#" * number)


print("\nExercise 4 - 8 by 8 grid")

for row in range(8):
    for column in range(8):
        print("#", end=" ")
    print()


print("\nExercise 5 - Number multiplied by itself")

for number in range(11):
    print(f"{number} x {number} = {number * number}")


print("\nExercise 6 - Print technologies")

technologies = ["Python", "Numpy", "Pandas", "Django", "Flask"]

for technology in technologies:
    print(technology)


print("\nExercise 7 - Sum all numbers from 0 to 100")

total = 0

for number in range(101):
    total += number

print(total)


print("\nExercise 8 - Sum even and odd numbers separately")

total_even = 0
total_odd = 0

for number in range(101):
    if number % 2 == 0:
        total_even += number
    else:
        total_odd += number

print(
    f"The sum of all evens is {total_even}. "
    f"The sum of all odds is {total_odd}."
)


print("\nExercise 9 - Countries containing 'land'")

countries = [
    "Afghanistan",
    "Albania",
    "Algeria",
    "Andorra",
    "Angola",
    "Antigua and Barbuda",
    "Argentina",
    "Armenia",
    "Australia",
    "Austria",
    "Azerbaijan",
    "Bahamas",
    "Bahrain",
    "Bangladesh",
    "Barbados",
    "Belarus",
    "Belgium",
    "Belize",
    "Benin",
    "Bhutan",
    "Bolivia",
    "Bosnia and Herzegovina",
    "Botswana",
    "Brazil",
    "Brunei",
    "Bulgaria",
    "Burkina Faso",
    "Burundi",
    "Cabo Verde",
    "Cambodia",
    "Cameroon",
    "Canada",
    "Central African Republic",
    "Chad",
    "Chile",
    "China",
    "Colombia",
    "Comoros",
    "Congo, Democratic Republic of the",
    "Congo, Republic of the",
    "Costa Rica",
    "Côte d'Ivoire",
    "Croatia",
    "Cuba",
    "Cyprus",
    "Czech Republic",
    "Denmark",
    "Djibouti",
    "Dominica",
    "Dominican Republic",
    "East Timor (Timor-Leste)",
    "Ecuador",
    "Egypt",
    "El Salvador",
    "Equatorial Guinea",
    "Eritrea",
    "Estonia",
    "Eswatini",
    "Ethiopia",
    "Fiji",
    "Finland",
    "France",
    "Gabon",
    "Gambia",
    "Georgia",
    "Germany",
    "Ghana",
    "Greece",
    "Grenada",
    "Guatemala",
    "Guinea",
    "Guinea-Bissau",
    "Guyana",
    "Haiti",
    "Honduras",
    "Hungary",
    "Iceland",
    "India",
    "Indonesia",
    "Iran",
    "Iraq",
    "Ireland",
    "Israel",
    "Italy",
    "Jamaica",
    "Japan",
    "Jordan",
    "Kazakhstan",
    "Kenya",
    "Kiribati",
    "Korea, North",
    "Korea, South",
    "Kuwait",
    "Kyrgyzstan",
    "Laos",
    "Latvia",
    "Lebanon",
    "Lesotho",
    "Liberia",
    "Libya",
    "Liechtenstein",
    "Lithuania",
    "Luxembourg",
    "Madagascar",
    "Malawi",
    "Malaysia",
    "Maldives",
    "Mali",
    "Malta",
    "Marshall Islands",
    "Mauritania",
    "Mauritius",
    "Mexico",
    "Micronesia",
    "Moldova",
    "Monaco",
    "Mongolia",
    "Montenegro",
    "Morocco",
    "Mozambique",
    "Myanmar",
    "Namibia",
    "Nauru",
    "Nepal",
    "Netherlands",
    "New Zealand",
    "Nicaragua",
    "Niger",
    "Nigeria",
    "North Macedonia",
    "Norway",
    "Oman",
    "Pakistan",
    "Palau",
    "Palestine",
    "Panama",
    "Papua New Guinea",
    "Paraguay",
    "Peru",
    "Philippines",
    "Poland",
    "Portugal",
    "Qatar",
    "Romania",
    "Russia",
    "Rwanda",
    "Saint Kitts and Nevis",
    "Saint Lucia",
    "Saint Vincent and the Grenadines",
    "Samoa",
    "San Marino",
    "Sao Tome and Principe",
    "Saudi Arabia",
    "Senegal",
    "Serbia",
    "Seychelles",
    "Sierra Leone",
    "Singapore",
    "Slovakia",
    "Slovenia",
    "Solomon Islands",
    "Somalia",
    "South Africa",
    "South Sudan",
    "Spain",
    "Sri Lanka",
    "Sudan",
    "Suriname",
    "Sweden",
    "Switzerland",
    "Syria",
    "Tajikistan",
    "Tanzania",
    "Thailand",
    "Togo",
    "Tonga",
    "Trinidad and Tobago",
    "Tunisia",
    "Turkey",
    "Turkmenistan",
    "Tuvalu",
    "Uganda",
    "Ukraine",
    "United Arab Emirates",
    "United Kingdom",
    "United States",
    "Uruguay",
    "Uzbekistan",
    "Vanuatu",
    "Vatican City",
    "Venezuela",
    "Vietnam",
    "Yemen",
    "Zambia",
    "Zimbabwe",
]

for country in countries:
    if "land" in country.lower():
        print(country)


print("\nExercise 10 - Reverse the fruits list")

fruits = ["banana", "orange", "mango", "lemon"]

for index in range(len(fruits) - 1, -1, -1):
    print(fruits[index])


print("\nExercise 11 - Print values from a nested list")

matrix = [
    [1, 2],
    [3, 4],
]

for row in matrix:
    for number in row:
        print(number)


print("\nExercise 12 - Count vowels in a word")

word = "programming"
vowel_count = 0

for letter in word:
    if letter.lower() in "aeiou":
        vowel_count += 1

print(f"The word contains {vowel_count} vowels.")


print("\nExercise 13 - Print every number")

numbers = [4, 8, 15, 16, 23, 42]

for number in numbers:
    print(number)


print("\nExercise 14 - Find the sum")

numbers = [4, 8, 15, 16, 23, 42]
total = 0

for number in numbers:
    total += number

print(f"The sum is {total}")


print("\nExercise 15 - Print even and odd numbers")

numbers = [4, 8, 15, 16, 23, 42]

for number in numbers:
    if number % 2 == 0:
        print(f"{number} is an even number")
    else:
        print(f"{number} is an odd number")


print("\nExercise 16 - Count even numbers")

numbers = [4, 8, 15, 16, 23, 42]
even_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count += 1

print(f"There are {even_count} even numbers.")


print("\nExercise 17 - Find the largest number")

numbers = [4, 8, 15, 16, 23, 42]
largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print(f"The largest number is {largest}")


print("\nExercise 18 - Find the smallest number")

numbers = [4, 8, 15, 16, 23, 42]
smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number

print(f"The smallest number is {smallest}")


print("\nExercise 19 - Find the largest and smallest numbers")

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


print("\nExercise 20 - Count vowels in text")

text = "Hello World"
vowel_count = 0

for letter in text:
    if letter.lower() in "aeiou":
        vowel_count += 1

print(f"There are {vowel_count} vowels.")


print("\nExercise 21 - Print each row")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

for row in matrix:
    print(row)


print("\nExercise 22 - Print every number in a matrix")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

for row in matrix:
    for number in row:
        print(number)


print("\nExercise 23 - Sum every number in a matrix")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

total = 0

for row in matrix:
    for number in row:
        total += number

print(f"The total is {total}")


print("\nExercise 24 - Countries data exercises")

try:
    from countries_data import countriess
except ImportError:
    print(
        "Skipped: countries_data.py was not found in the same folder as this file."
    )
else:
    language_entry_count = 0

    for country in countriess:
        for language in country["languages"]:
            language_entry_count += 1

    print(
        f"The total number of language entries is: "
        f"{language_entry_count}"
    )

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
        reverse=True,
    )

    top_ten_languages = sorted_languages[:10]

    print("\nThe 10 most spoken languages are:")

    for language, count in top_ten_languages:
        print(language, count)

    sorted_countries = sorted(
        countriess,
        key=lambda country: country["population"],
        reverse=True,
    )

    top_ten_countries = sorted_countries[:10]

    print("\nThe 10 most populated countries are:")

    for country in top_ten_countries:
        print(country["name"], country["population"])
