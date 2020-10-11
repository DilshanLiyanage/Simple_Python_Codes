class Student:

    def __init__(self, name, birth_year, address):
        self.name = name
        self.birth_year = birth_year
        self.address = address

    def get_age(self):
        age = 2020 - int(self.birth_year)
        return  age


name = input("What is your name? ")
age = input("What is your birth year? ")
address = input("What is your address? ")

student = Student(name, age, address)
act_name = student.name
act_address = student.address
act_age = student.get_age();

print ("Hi "+act_name+". you is "+str(act_age)+" years old and you stay in "+act_address)