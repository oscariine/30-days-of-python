'''
Exercises: Level 1
Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years. Output:

Enter your age: 30
You are old enough to learn to drive.
Output:
Enter your age: 15
You need 3 more years to learn to drive.
Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age. Output:

Enter your age: 30
You are 5 years older than me.
Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b. Output:

Enter number one: 4
Enter number two: 3
4 is greater than 3

'''

def exer():
    age = int(input("Enter your age: "))

    if age >= 18:
        print("You are old enough to drive.")
    else:
        years_left = 18 - age
        print(f"You need {years_left} more years to learn how to drive")
    
    
def exer2():
    my_age = 20

    your_age = int(input("Whats your age: "))
    
    if your_age > my_age:
        diff = your_age - my_age
        if diff == 1: 
            print(f"Your {diff} older then me ")
        else:
            print(f"Your {diff} older then me ")
    elif your_age < my_age:
        diff = my_age - your_age
        if diff ==1:
            print(f"your {diff} younger then me ")
        else:
            print(f"your {diff} younger then me ")
            
    else: 
        your_age == my_age
        print(f"YOUR THE SAME AGE AS ME SILLY")

        
        #greater then less then and equal to
        
def exer3():
    
    a = int(input("Enter # one: "))
    b = int(input("Enter # two: "))
    
    if a > b:
        print(f" {a} is greater than {b}")
    elif a < b:
        print(f"{b} is greater than {a}")
    else:
        print(f"{a} is equal too {b}")
        
    
    
    
    
    
    
    
def exer4():
    your_grade = int(input("Whats your grade: "))
    
    if your_grade >= 90:
        print("Your Grade is a A")
    elif your_grade >= 80:
        print("Your grade is a B")  
    elif your_grade >= 70:
        print("Your grade is a C") 
    elif your_grade >= 60:
        print("Your grade is a D") 
    else:
        print("Your grade is a F")
        

def exer5():
    
    Month = input("Enter the Month: ")
    
    Autumn = 'September', 'October' ,'November'
    Winter = 'December', 'January','February'
    Spring = 'March', 'April', 'May'
    Summer = 'June', 'July', 'August'
    
    if Month in Autumn:
        print('The season is Autumn')
    elif Month in Winter:
        print('The season is Winter')
    elif Month in Spring:
        print('The season is spring ')
    elif Month in Summer:
        print("Your season is summer")
    else:
        print("THIS IS NOT A MONTH")
        
def exer5():
    
    fruits = ['banana', 'orange', 'mango', 'lemon']
    fruit = input("Enter a fruit: ").lower()
    
    if fruit in fruits:
        print("This fruit already exists")
    else:
        fruits.append(fruit)
        print(fruits)


def exer6():
    
            '''
            * Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
            * Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
            * If a person skills has only JavaScript and React, print('He is a front end developer'), 
            if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
            if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), else print('unknown title') -
            for more accurate results more conditions can be nested!
            * If the person is married and if he lives in Finland, print the information in the following format:
                Asabeneh Yetayeh lives in Finland. He is married.
            '''

            person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
            }
            
            if 'skills' in person:
                skills = person['skills']
                middle = len(skills) // 2
                print("Your Middle Skill is", skills[middle])
                
            if 'skills'in person:
                print("Python" in person['skills'])
                
            if 'skills' in person:
                skills = person['skills']
                
            if 'JavaScript' in skills and 'React' in skills and len(skills) == 2:
                print("He is a frontend dev")
                
            elif 'MongoDB' in skills and 'Node' in skills and 'Python' in skills:
                print('He is a Backend dev ')
            
            elif 'MongoDB' in skills and 'Node' in skills and 'React' in skills:
                print("HE is a full stack dev")
            
            else:
                print('Input error ')
                
            if person['is_married'] and person['country'] == 'Finland':
                print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. He is {person['is_married']}")
        
        
        
'''
* print the middle skill
* check if 'SQL' is in skills
* if skills have Python and SQL, print "She is a data teacher"
* if she is not married and lives in Canada, print the sentence
'''

        
                
def exer7():
    teacher = {

    'first_name1': 'Sarah',

    'last_name1': 'Lee',

    'age1': 35,

    'country1': 'Canada',

    'is_married1': False,

    'skills1': ['Excel', 'Python', 'SQL'],

    'address1': {

        'street1': 'Lake Road',

        'zipcode1': 'A1234'

    }
    }
    
    if 'skills1' in teacher:
        skills_1 = teacher['skills1']
        middle1 = len(skills_1) // 2 
        middle_skill =skills_1[middle1]
        print(f'Your middle skill is {middle_skill}')
        
    if 'SQL' in skills_1:
        print('TRUE')
        
    if 'Python' in skills_1 and 'SQL' in skills_1:
        print('She is a data teacher')
        
    if teacher['is_married1'] == False and teacher['country1'] == 'Canada':
         print(f"{teacher['first_name1']} {teacher['last_name1']} lives in {teacher['country1']}. She is not married.")
        
      
      
      
      
      



'''
1. Check if the employee dictionary has a skills key. If it does, print the middle skill.
2. Check if the employee dictionary has a skills key. If it does, check if the employee has 'SQL' skill and print the result.
3. If the employee has both 'Python' and 'SQL', print:
    "He is a data employee"
4. If the employee is married and lives in Mexico, print:
    "Daniel Cruz lives in Mexico. He is married."
'''

def exer8():
    employee = {
    'first_name': 'Daniel',
    'last_name': 'Cruz',
    'age': 28,
    'country': 'Mexico',
    'is_married': True,
    'skills': ['Excel', 'Power BI', 'SQL', 'Python'],
    'address': {
        'street': 'Sunset Avenue',
        'zipcode': '55021'
    }
    }
    
    if 'skills' in employee:
        emp_skills = employee['skills']
        middle_skill = len(emp_skills) // 2 
        middle_skilll = emp_skills[middle_skill]
        print(middle_skilll)
    
    if 'SQL' in emp_skills:
        print('TRUE')
        
    if 'SQL' in emp_skills and 'Python' in emp_skills:
        print('He is a data employee')
        
    if employee['is_married'] == True and employee['country'] == 'Mexico':
        print(f'{employee["first_name"]} {employee["last_name"]} lives in {employee["country"]}')
        

    


'''
1. Check if the dictionary has a points key. If it does, print the points.
2. Check if the player scored 20 or more. If yes, print:
    "High scorer"
3. Check if the player has 10 or more rebounds. If yes, print:
    "Double-digit rebounds"
4. Check if the player has 5 or more assists and is a starter. If yes, print:
    "All-around starter"
5. If the player is a starter, print:
    "Oscar starts for the Falcons."
'''



def exer9():
        player = {
    'name': 'Oscar',
    'team': 'Falcons',
    'points': 18,
    'assists': 7,
    'rebounds': 11,
    'is_starter': True
}
        
        if 'points' in player:
            player_p = player['points']
            print(player_p)
            
        if player_p >= 20:
            print("High scorer ") 
        
        if player['rebounds'] >= 10:
            print('Double-digit rebounds')
            
        if player['assists'] >= 5 and player['is_starter'] == True:
            print("All-around starter")
            
        if player['is_starter'] == True:
            print("Oscar starts for the Falcons.")
            
            
            
exer9()
                
                
            
    
            
      