# examples on heirarichal classes

# finding the area of rectangle

class formula:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        res=self.length*self.breadth
        
    def rectangle(self):
        print("the area of the rectangle is",res)       

f=formula(3,4)
f.rectangle()

