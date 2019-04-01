i = 0
num = [0,0]

while(not(i == 2)):
    try:
        num[i] = int(input("Please enter number: "))
        i+=1
    except:
        print("Please insert a int number")

print(num[0], " + ", num[1], " = ", num[0] + num[1])
print(num[0], " - ", num[1], " = ", num[0] - num[1])
print(num[1], " - ", num[0], " = ", num[1] - num[0])
print(num[0], " * ", num[1], " = ", num[0] * num[1])

try:
    print(num[0], " / ", num[1], " = ", "{0:0.2f}".format(num[0] / num[1]))
except:
    print(num[0], " / ", num[1], " this operation is invalid") 
    
try:
    print(num[1], " / ", num[0], " = ", "{0:0.2f}".format(num[1] / num[0]))
except:
    print(num[1], " / ", num[0], " this operation is invalid") 
