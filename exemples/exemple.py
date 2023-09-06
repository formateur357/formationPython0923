#! /usr/bin/env python3

class Test:
    def __init__(self, test) -> None:
        self.test = test

class Shape:
    """An abstract shape"""
    def __init__(self, position) -> None:
        self.position = position
    def area(self):
        raise NotImplementedError

class Rectangle(Test, Shape):
    def __init__(self, test = True, position = (10, 1), width = 10, height = 5) -> None:
        Test.__init__(self, test)
        Shape.__init__(self, position)
        self.width = width
        self.height = height
        
    def area(self) -> int:
        """Calculate the area of the rectangle"""
        return self.height * self.width
    
    def toString(self) -> str:
        """Return a litteral representation of the rectangle"""
        return f"width : {self.width}height: {self.height}\n"


s = Shape((12, 34))
rect2 = Rectangle(False, (55, 67), 90, 34)
rect = Rectangle()

print(f"shape = {str(s.position)}")
print(f"rect = {rect.toString()}rect2 = {rect2.toString()}")
print(f"aire de rect : {str(rect.area())}\naire de rect2 : {rect2.area()}\n")
print(f"rect position : {rect2.position}")
print(f"rect test : {rect2.test}")