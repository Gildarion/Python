import turtle as t
from random import randint

class Circuit():
    racers = []
    __posStartY = (-30, -10, 10, 30) 
    __color = ("red","blue","green","orange")

    def __init__(self, widthCircuit, longCircuit):
        
        self.__startLine = (- widthCircuit / 2) + (widthCircuit * 0.10)
        self.__finishLine = widthCircuit / 2 - widthCircuit * 0.05
        self.__field = t.Screen()
        self.__field.setup(widthCircuit, longCircuit)
        self.__field.bgcolor("lightgrey")
        
        self.__createRacers()
    
    def __createRacers(self):
        for i in range(4):
            newRacer = t.Turtle()
            newRacer.color(self.__color[i])
            newRacer.shape("turtle")
            newRacer.up()
            newRacer.setpos(self.__startLine, self.__posStartY[i])

            self.racers.append(newRacer)

    def race(self):

        winner = False

        while not winner:
            for turtle in self.racers:
                forward = randint(1,8)
                turtle.forward(forward)

                if turtle.position()[0] >= self.__finishLine:
                    winner = True
                    print("The winner is {}".format(turtle.color()[0]))
                    break



if __name__ == "__main__":
    circuit1 = Circuit(640, 300)
    circuit1.race()
    input("")

