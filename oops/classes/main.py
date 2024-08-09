class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        a = self.x * self.x
        b = self.y * self.y
        c = self.z * self.z
        return(a + b + c)


obj1 = Point(4, 5, 6)
print(obj1.sqSum())

class Student:
    def __init__(self, name, phy, chem, bio):
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio

    def totalObtained(self):
        return(self.phy + self.chem + self.bio)

    def percentage(self):
        return((self.totalObtained() / 300) * 100)

class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return (self.num2 + self.num1)

    def subtract(self):
        return (self.num2 - self.num1)

    def multiply(self):
        return (self.num2 * self.num1)

    def divide(self):
        return (self.num2 / self.num1)


demo1 = Calculator(10, 94)
print("Addition:", demo1.add())
print("Subtraction:", demo1.subtract())
print("Mutliplication:", demo1.multiply())
print("Division:", demo1.divide())