def countDown(x):
    if x != 0:
        print("{},".format(x), end = " ")
        return countDown(x - 1)
    else:
        return 0

print(countDown(10))
