#! /usr/bin/env python3

class Test:
    def __init__(self,test=None, *args,**kwargs) -> None:
        #Ajout super(). et de *args et **kwarg
        super().__init__(*args, **kwargs)
        self.test = test
        
class Shape:
    """An abstract shape"""
    def __init__(self, position=None, *args,**kwargs) -> None:
        #Ajout super(). et de *args et **kwarg
        super().__init__(*args, **kwargs)
        self.position = position
        
    def area(self):
        raise NotImplementedError

class Rectangle(Shape,Test):
    def __init__(self,test=True,position=(10, 1),width=10,height=5, *args, **kwargs) -> None:
        #Ajout de *args et **kwarg en parametre
        super().__init__(test=test,position=position,*args, **kwargs)
        self.width = width
        self.height = height
        
    def area(self) -> int:
        """Calculate the area of the rectangle"""
        return self.height * self.width
    
    def toString(self) -> str:
        """Return a litteral representation of the rectangle"""
        return f"width : {self.width} => height: {self.height}\n"

#Instanciation
s = Shape((12, 34))
rect = Rectangle()
rect2 = Rectangle(False,(55, 67),90,34)

#Affichage
print(f"shape = {str(s.position)}")
print(f"rect = {rect.toString()}rect2 = {rect2.toString()}")
print(f"aire de rect : {str(rect.area())}\naire de rect2 : {rect2.area()}\n")
print(f"rect position : {rect2.position}")
print(f"rect test : {rect2.test}")