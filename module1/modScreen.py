#dict with color

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
    formatMsg(0,33,41)
    printMsg(error, line)
    reset()

def inputMsg(message, line, column = 1, delEnd = True):
    locateCursor(line, column)
    if delEnd:
        clearLine(line)
    return input(message)

#def printMsg(message, line, column = 1, delEnd = False):
# param : color, line, column, nr, style
def printMsg(message, **params):
    locateCursor(line, column)
    if delEnd:
        clearLine(line)
    print(message, end = "")   

def formatMsg(style, colorText = 37, colorBackground = 40):
    print("\033[{};{};{}m".\
            format(style, colorText, colorBackground), end = "")

def reset():
    formatMsg(0, 39, 49)
