def sumAll(x):
    if x > 0:
        return x + sumAll(x - 1)
    else:
        return 0

if __name__ == "__main__":
    print(sumAll(10))
