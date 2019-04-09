import datetime


today = datetime.datetime.today()
yearActual = int(today.strftime("%Y"))
dayActual = int(today.strftime("%d"))
monthActual = int(today.strftime("%m"))
calendar = [31, 28, 31, 30, 31, 30, 31, 31, 31, 30, 31]

name = input("What is your name? ")
print("Hi ", name, ". It's a pleasure")

i = 0
days = 0

while (i < monthActual - 1):
    days += int(calendar[i])
    i += 1
days += dayActual


born = int(input("How old are you? "))
born = yearActual - born

prob = (100 * days) / 365

print("The probability that you born in ", born, 
      "is ", prob, "%")

if(prob < 60):
    print("So, maybe, you born in ", born - 1)
