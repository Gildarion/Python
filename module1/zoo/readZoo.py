import modScreen as screen
from config import priceTicket

def existFile(strFile):
    try:
        openFile = open(strFile,'r')
        return openFile
    except:
        screen.printError("File not found")
        exit()
def outputScreen(output):
    print("Baby....: {:3d}  - {} €".format(output[0], priceTicket['baby'] * output[0]))
    print("Kid.....: {:3d}  - {} €".format(output[1], priceTicket['kid'] * output[1]))
    print("Adult...: {:3d}  - {} €".format(output[2], priceTicket['adult'] * output[2]))
    print("Retired.: {:3d}  - {} €".format(output[3], priceTicket['retired'] * output[3]))
    print("\tTotal    {} €".format(output[4]))

strFile = "transactions.txt"
fInputs = existFile(strFile)
totalTicket = [0, 0, 0, 0]
totalCount = 0
line = fInputs.readline()
while line != '':
    register = line.split(',')
    for i in range(0, 4):
        totalTicket[i] += int(register[i])
        totalCount += totalTicket[i]
    line = fInputs.readline()
fInputs.close()
totalTicket.append(totalCount)
outputScreen(totalTicket)
