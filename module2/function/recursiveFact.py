def factor(x):
    if x > 0:
        return x * factor(x - 1)
    else:
        return 1

if __name__ == "__main__":
    print(factor(10))
    print(factor(0))
