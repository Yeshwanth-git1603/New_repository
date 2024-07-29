# multilevel inheritance using fruit class

class fruits:
    def __init__(self,name,color):
        self.f_name=name
        self.f_color=color
        
    def display(self):
        print("the name of the fruit is :",self.f_name)
        print("the color of the fruit is:",self.f_color)
        
        
class fruits2(fruits):
    def __init__(self,name,color,price):
        super().__init__(name,color)
        self.f_price=price
        
    def display(self):
        super().display()
        print("the price of the fruit is:",self.f_price)
        
        
class fruits3(fruits2):
    def __init__(self,name,color,price,availability):
        super().__init__(name,color,price)
        self.f_availability=availability
        
    def display(self):
        super().display()
        print("the availability of the fruits are:",self.f_availability)

        
        
f2=fruits2("apple","red","20")
f2.display()

f3=fruits3("banana","yellow","30","allday")
f3.display()


