i = 0
num = [0,0]

#Input
print("The numbers will be divide by 10")
while(i < 2):
    try:
        num[i] = int(input("Please enter a number: "))
        i+=1
    except:
        print("Please insert a int number")

#Data processing
num[0] = num[0] / 10
num[1] = num[1] /10
add = num[0] + num[1]
sub0 = num[0] - num[1]
sub1 = num[1] - num[0]
mul = num[0] * num[1]
try:
    div0 = num[0] / num[1]
except:
    div0 = "Operation Invalid"
try:
    div1 = num[1] / num[0]
except:
    div1 = "Operation Invalid"

i = 0

while(i < 2):
    num[i] = "{0:0.2f}".format(float(num[i]))
    i+=1

#Output
print("The operations between both numbers are: ")
print("  ", num[0], " + ", num[1], " = ", "{0:0.2f}".format(add))
print("  ", num[0], " - ", num[1], " = ", "{0:0.2f}".format(sub0))
print("  ", num[1], " - ", num[0], " = ", "{0:0.2f}".format(sub1))
print("  ", num[0], " * ", num[1], " = ", "{0:0.2f}".format(mul))
try:
    print("  ", num[0], " / ", num[1], " = ", "{0:0.2f}".format(div0))
except:
    print("  ", num[0], " / ", num[1], " = ", div0)
try:
    print("  ", num[1], " / ", num[0], " = ", "{0:0.2f}".format(div1))
except:
    print("  ", num[1], " / ", num[0], " = ", div1)
