## OOPS in Python

### An Introduction To Classes and Related Keywords


Sure! I'll explain each concept along with a corresponding Python code example.

### 1. **Classes**
A class in Python is a blueprint for creating objects (instances). It defines a set of attributes and methods that the created objects will have.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name  # Instance variable
        self.breed = breed  # Instance variable
    
    def bark(self):
        return f"{self.name} says Woof!"

# Creating an instance of Dog
dog = Dog("Rex", "Golden Retriever")
print(dog.bark())  # Output: Rex says Woof!
```

### 2. **Methods**
Methods are functions defined inside a class. They describe the behaviors of the objects that are instances of the class.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):
        return f"{self.name} says Woof!"

dog = Dog("Rex", "Golden Retriever")
print(dog.bark())  # Output: Rex says Woof!
```

### 3. **self Keyword**
The `self` keyword represents the instance of the class. It is used to access variables and methods associated with the current object.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name  # self refers to the instance being created
        self.breed = breed
    
    def bark(self):
        return f"{self.name} says Woof!"

dog = Dog("Rex", "Golden Retriever")
print(dog.bark())  # Output: Rex says Woof!
```

### 4. **Properties**
Properties in Python are a way of managing the access to instance variables by defining getter and setter methods. They allow you to control the behavior when an attribute is accessed or modified.

```python
class Dog:
    def __init__(self, name):
        self._name = name  # Use _name to denote a private variable
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if len(new_name) > 2:
            self._name = new_name
        else:
            raise ValueError("Name must be more than 2 characters")

dog = Dog("Rex")
print(dog.name)  # Output: Rex

dog.name = "Max"  # Set new name
print(dog.name)  # Output: Max
```

### 5. **Private Properties**
Private properties are those that should not be accessed directly outside the class. In Python, these are usually denoted by a single underscore `_` or double underscore `__` before the variable name.

```python
class Dog:
    def __init__(self, name, breed):
        self.__name = name  # Private property
        self.__breed = breed  # Private property
    
    def get_name(self):
        return self.__name

dog = Dog("Rex", "Golden Retriever")
print(dog.get_name())  # Output: Rex
# print(dog.__name)  # This will raise an AttributeError
```

### 6. **Class Variables**
Class variables are shared across all instances of a class. They are defined within the class but outside of any instance methods.

```python
class Dog:
    species = "Canine"  # Class variable
    
    def __init__(self, name):
        self.name = name

dog1 = Dog("Rex")
dog2 = Dog("Max")
print(Dog.species)  # Output: Canine
print(dog1.species)  # Output: Canine
print(dog2.species)  # Output: Canine
```

### 7. **Instance Variables**
Instance variables are unique to each instance of a class. They are usually defined within the `__init__` method and prefixed with `self`.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name  # Instance variable
        self.breed = breed  # Instance variable

dog1 = Dog("Rex", "Golden Retriever")
dog2 = Dog("Max", "Bulldog")

print(dog1.name)  # Output: Rex
print(dog2.name)  # Output: Max
```

### 8. **Static Methods**
Static methods do not access or modify the class state. They are defined with the `@staticmethod` decorator and do not take `self` or `cls` as the first parameter.

```python
class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

print(MathOperations.add(5, 3))  # Output: 8
```

### 9. **Class Methods**
Class methods are methods that have access to the class itself rather than instance variables. They are defined with the `@classmethod` decorator and take `cls` as the first parameter.

```python
class Dog:
    species = "Canine"
    
    def __init__(self, name):
        self.name = name
    
    @classmethod
    def change_species(cls, new_species):
        cls.species = new_species

Dog.change_species("New Canine")
print(Dog.species)  # Output: New Canine
```

These concepts and examples should provide a solid foundation for understanding how object-oriented programming works in Python!
