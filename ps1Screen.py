def clearScreen():
    print("\033[2J")

def locateCursor(line, column):
    print("\033[{};{}H".format(line, column), end = "")


