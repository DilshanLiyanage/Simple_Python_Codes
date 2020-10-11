
name = input("What is your name? ")
birth_year = int(input("What is your birth year? "))
age = 2020-birth_year
print ("Hi "+name+". You are "+str(age)+" years old.")

count = 0
while count <= 5:
    print ("While loop value "+ str(count))
    count += 1


fruits = ['banana', 'mangoes', 'apple', 'orange'];

for fruit in fruits:
    if fruit == 'banana':
        fruits[0] = "banana one"
        print ("For loop fruit is "+ fruit.upper())
    elif fruit == 'mangoes':
        print ("For loop fruit is "+ fruit.lower())
    elif fruit == 'apple':
        print ("For loop fruit is " + fruit.upper())
    else:
        break


for gg in fruits:
    print ("second for loop "+gg)

cars = ('BMW', 'Benz', 'Audi')

for car in cars:
    print ('Tuple loop '+ car)


obj = {'name':'Ravi', 'age':24, 'email':'ravi@gmail.com'}

print(obj['name'])
print(obj['age'])
print(obj['email'])
