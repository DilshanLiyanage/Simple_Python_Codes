
def age_cal (birth):
    by_no = int(birth)
    age = 2020-by_no
    return age

name = input("What is your name? ")
birth_year = input("What is your birth year? ")
age = age_cal(birth_year)
print("Hi "+name+". You are "+str(age)+" years old.")
