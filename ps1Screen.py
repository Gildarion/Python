def clearScreen():
    print("\033[2J")

def locateCursor(line, column):
    if column is None:
        column = 1
    print("\033[{};{}H".format(line, column), end = "")

def clearLine(line = None, column = None):
    if line is not None and column is not None:
        locateCursor(line, column)
    elif line is not None:
        locateCursor(line, 1)
    print("\033[K", end = "")

def pause():
    input("")

def printError(message, line = 25):
    error = "ERROR - " + message
    locateCursor(line,1)
    clearLine(line)
    print("\033[1;37;40m{}".format(error), end = "")

def inputMsg(message, line, column = 1, delEnd = True):
    locateCursor(line, column)
    if delEnd:
        clearLine(line)
    return input(message)

def printMsg(message, line, column = 1, delEnd = False):
    locateCursor(line, column)
    if delEnd:
        clearLine(line)
    print(message, end = "")   
