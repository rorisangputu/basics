class Point:
    def __init__(self, x, y): #constructer keyword
        self.x = x
        self.y = y


    def divide(self):
       if self.x != 0:
        return int(self.y / self.x)
    
    def multiply(self):
       return self.x * self.y


point1 = Point(10, 20)

print(point1.divide())

class Person:
    def __init__(self, name):
        self.name = name
    
    def talk(self):
       print(f"Hello, I'm {self.name}!")

person1 = Person('Matthew')

person1.talk()
