import datetime

year = int((datetime.date.today()).strftime("%Y"))

name = input("What is your name? ")
print("Hi ", name, ". It's a pleasure")


born = int(input("How old are you? "))
test = input("Have you had your birthday yet this year? (y/n) ")
if(test == "y"):
    born = year - born
else:
    born = year - born - 1

print("So you born in ", born)
    