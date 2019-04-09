import ps1Screen as screen
import ps1Presentation as presentation

dicTicket = {
        "baby":{
            "price":0,
            "quantity":0
            },
        "kid":{
            "price":0,
            "quantity":0
            },
        "adult":{
            "price":0,
            "quantity":0
            },
        "retired":{
            "price":0,
            "quantity":0
            }
        }

def calculateTicket(age):
    ticket = {"price":0,"type":""}
    if age <= 2:
        ticket["type"] = "baby"
        ticket["price"] = 0
    elif age <= 12:
        ticket["type"] = "kid"
        ticket["price"] = 14
    elif age <= 65:
        ticket["type"] = "adult"
        ticket["price"] = 23
    else:
        ticket["type"] = "retired"
        ticket["price"] = 18
    return ticket
    
def main():
    age = presentation.askAge("Introduce the group member age: ")
    intTotalPrice = 0
    intTotalTicket = 0
    ticket = dict()
	
    while age != 0:
        ticket = calculateTicket(age)
        intTotalPrice += ticket["price"]
        intTotalTicket += 1
        
        dicTicket[ticket["type"]]["quantity"] += 1
        dicTicket[ticket["type"]]["price"] += ticket["price"] 
        presentation.posLine(ticket["type"],\
                dicTicket[ticket["type"]]["price"],\
                dicTicket[ticket["type"]]["quantity"])
        presentation.posLine("total", intTotalPrice, intTotalTicket)
        age = presentation.askAge("Introduce the group member age: ")

presentation.outputScreen()
main()
screen.locateCursor(30,1)
screen.pause()
