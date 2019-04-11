class Thermometer():
    def __init__(self):
        self.__temperature = 0
        self.__typeDegree = 'C'

    def __converter(self, temperature, typeDegree):
        if typeDegree.upper() == 'C':
            return "{} ºF".format(temperature * 9/5 +32)
        elif typeDegree.upper() == 'F':
            return "{} ºC".format((temperature - 32) * 5/9)
        else:
            return "ERROR - Type of degree invalid"
    
    def __str__(self):
        return "{} º{}".format(self.__temperature, self.__typeDegree)

    def degree(self, typeDegree = None):
        if typeDegree is None:
            return "{}".format(self.__typeDegree)
        else:
            self.__typeDegree = typeDegree
    
    def changeTemperature(self, temperature = 0):
        if temperature == 0:
            return "{}".format(self.__temperature)
        else:
            self.__temperature = temperature
    
    def measure(self, typeDegree = None):
        if typeDegree is None or typeDegree.upper() == self.__typeDegree:
           return self.__str__()
        else:
            if typeDegree.upper() == 'F' or typeDegree.upper() == 'C':
                self.__typeDegree = typeDegree
                return self.__converter(self.__temperature, self.__typeDegree)
            else:
                return self.__str__()

