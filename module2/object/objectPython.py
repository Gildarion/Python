class Dog():
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def __str__(self):
        return "Name:{} Age:{} Weight: {}".format(self.name, self.age, self.weight)

    def bark(self):
            print("{} barks".format(self.name))

if __name__ == "__main__":
    buddy = Dog("Buddy", 3, 12)
    buddy.bark()
    print(buddy)
