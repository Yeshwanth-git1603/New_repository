# home example

class asset:
    def __init__(self,name,area,sqft):
        self.a_name=name
        self.a_area=area
        self.a_sqft=sqft
        
    def home(self):
        print("the name of the home is:",self.a_name)
        print("the area of the house is:",self.a_area)
        print("the sqft of the home is:",self.a_sqft)
        
        
class asset2(asset):
    def __init__(self,name,area,sqft,address):
        super().__init__(name,area,sqft)
        self.a_address=address
        
    def home(self):
        super().home()
        print("the address of the home is:",self.a_address)
        
class asset3(asset):
    def __init__(self,name,area,sqft,price):
        super().__init__(name,area,sqft)
        self.a_price=price
        
    def home(self):
        super().home()
        print("the price of the home is:",self.a_price)
        

        
a2=asset2("mg towers","madhura nagar","2500","leela mahal")
a2.home()

a3=asset3("tr towers","madhura nagar","2000","20000000")
a3.home()

