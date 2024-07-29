# multilevel inheritance using vehicle class


class vehicle:
    def __init__(self,name,brand):
        self.c_name=name
        self.c_brand=brand
    
    def display(self):
        print("the name of the car is:",self.c_name)
        print("the brand of the car is:",self.c_brand)
        
        
class bmw(vehicle):
    def __init__(self,name,brand,model):
        super().__init__(name,brand)
        self.c_model=model
        
    def display(self):
        super().display()
        print("the model of the car is :",self.c_model)
        
class ferrari(bmw):
    def __init__(self,name,brand,model,price):
        super().__init__(name,brand,model)
        self.c_price=price
        
    def display(self):
        super().display()
        print("the price of the car is",self.c_price)
        
        
b=bmw("vw","bmw","m340i")
b.display()

f=ferrari("Enzo ferrari","ferrari","sf90","10cr")
f.display()

