def normal(x):
    return x

def square(x):
    return x * x

def sumAll(limitTo, f):
    result = 0
    for i in range(limitTo + 1):
        result += f(i)
    return result

print(sumAll(100, normal))
print(sumAll(3, square))
