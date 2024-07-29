#multilevel inheritance on phone

class phone:
    def __init__(self,name,model):
        self.p_name=name
        self.p_model=model
        
    def display(self):
        print("the name of the phone is :",self.p_name)
        print("the model of the phone is:",self.p_model)

class phone2(phone):
    def __init__(self,name,model,price):
        super().__init__(name,model)
        self.p_price=price
        
    def display(self):
        super().display()
        print("the price of the phone is:",self.p_price)
        
        
class phone3(phone2):
    def __init__(self,name,model,price):
        super().__init__(name,model,price)
        pass
    
    
    def display(self):
        super().display()
        pass
             
             
             
             
             
p2=phone2("iphone","15pro max","150000")
p2.display()

p3=phone3("vivo","v23 pro","500000")
p3.display()
            
