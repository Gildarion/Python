numbers = [1, 3, -8, 5, 10]

listEven = filter(lambda x: x % 2 == 0, numbers)

print(listEven)
print(list(numbers))
print(list(listEven))
