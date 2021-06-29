class Animal:
    def __init__(self, name):
        self.animal_name = name
    
    def eat(self):
        raise NotImplementedError("Child class should be implementing this abstract method.")
        
class Monkey(Animal):
    
    def eat(self):
        print("Monkey eating bananas...")
        
class Bird(Animal):
    
    def eat(self):
        print("bird eating seeds...")
        
    def fly(self):
        print("bird flying high...")

# myDog = Animal("jojo")
# myDog.eat()
# NotImplementedError: Child class should be implementing this abstract method.
myMonkey = Monkey("jojo")
myMonkey.eat()

myBird = Bird("Tim")
myBird.fly()