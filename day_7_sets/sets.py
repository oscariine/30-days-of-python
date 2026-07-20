
'''
Exercises: Level 1
Find the length of the set it_companies
Add 'Twitter' to it_companies
Insert multiple IT companies at once to the set it_companies
Remove one of the companies from the set it_companies
What is the difference between remove and discard

Exercises: Level 3
Convert the ages to a set and compare the length of the list and the set, which one is bigger?
Explain the difference between the following data types: string, list, tuple and set
I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
'''
def exer_1_3():

    # sets
    it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
    A = {19, 22, 24, 20, 25, 26}
    B = {19, 22, 20, 25, 26, 24, 28, 27}
    age = [22, 19, 24, 25, 26, 24, 25, 24]



    print(len(it_companies))

    it_companies.add('Twitter')
    print(it_companies)
    it_companies.update(['X', 'Meta', 'Visco'])
    print(it_companies)
    it_companies.remove('Microsoft')
    print(it_companies)
    
    st = set(age)
    
    print(st)
    
    sent = 'I am a teacher and I love to inspire and teach people'
    sep_sent = sent.split()
    print(sep_sent)
    
    stt = set(sep_sent)
    print(stt)
    print(len(stt))
   
   
    
    
    
exer_1_3()
    
    

exer_1_3()


'''
Join A and B
Find A intersection B
Is A subset of B
Are A and B disjoint sets
Join A with B and B with A
What is the symmetric difference between A and B
Delete the sets completely
'''


def exercise_2():
    A = {1, 2, 3}
    B = {3, 4, 5}
    
    C = A.union(B)
    print(C)
    
    print(A.intersection(B))
    
   
    
    print(A.issubset(B))
    
    print(A.isdisjoint(B))
    
    A.update(B)
    print(A)
    
    B.update(A)
    print(B)
    
    print(A.symmetric_difference(B))
    
    del A
    del B 
    
        
    
        
        
        
        
        

