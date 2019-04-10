class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def __str__(self):
        return "Name:{} Age:{} Weight: {}".format(self.name, self.age, self.weight)

    def bark(self):
            print("{} barks".format(self.name))

class DogService(Dog):
    def __init__(self, name, age, weight, owner):
        Dog.__init__(self, name, age, weight)
        self.owner = owner
        #private attrib
        self.__working = False
    
    #return print
    def __str__(self):
        return "{} owns {}".format(self.name, self.owner)

    def bark(self):
        if self.__working:
            print("{} cannot bark, it is working".format(self.name))
        else:
            Dog.bark(self)
    
    def work(self, value=None):
        if value is None:
            return self.__working
        else:
            self.__working = value

    def walk(self):
        print("{} walks with {}".format(self.name, self.owner))

if __name__ == "__main__":
    buddy = Dog("Buddy", 3, 12)
    buddy.bark()
    print(buddy)
    oscar = DogService("Oscar",6,20,"Jasper")
    oscar.walk()
    oscar.work()
    oscar.bark()
    oscar.work(True)
    oscar.bark()

