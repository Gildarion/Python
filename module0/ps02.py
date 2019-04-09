import datetime

year = int((datetime.date.today()).strftime("%Y"))

name = input("What is your name? ")
print("Hi ", name, ". It's a pleasure")


born = int(input("How old are you? "))
print("So you born in ", year - born)