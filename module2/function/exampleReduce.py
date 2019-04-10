from functools import reduce

numbers = [1, 3, -8, 5, 10]

sumAll = reduce(lambda x, y: x + y, numbers)

print(sumAll)
print(list(numbers))
