intElement = 100
maxIndex = intElement + 1
accumulator = 0

print(" - The program will calculate the total sum of the first hundred numbers")

for i in range(0,maxIndex):
    accumulator += i

print(" - The total sum is: ", accumulator)
