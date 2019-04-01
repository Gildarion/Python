i = 0
num = [0,0]

#Input
while(not(i == 2)):
    try:
        num[i] = int(input("Please enter number: "))
        i+=1
    except:
        print("Please insert a int number")

#Data processing
add = num[0] + num[1]
sub0 = num[0] - num[1]
sub1 = num[1] - num[0]
mul = num[0] * num[1]
try:
    div0 = num[0] / num[1]
    div0 = "{0.0.2f}".format(div0)
except:
    div0 = "Operation Invalid"
try:
    div1 = num[1] / num[0]
    div1 = "{0.0.2f}".format(div1)
except:
    div1 = "Operation Invalid"

#Output
print("The operations between both numbers are: ")
print(num[0], " + ", num[1], " = ", add)
print(num[0], " - ", num[1], " = ", sub0)
print(num[1], " - ", num[0], " = ", sub1)
print(num[0], " * ", num[1], " = ", mul)
print(num[0], " / ", num[1], " = ", div0)
print(num[1], " / ", num[0], " = ", div1)
