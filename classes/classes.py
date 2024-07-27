#using classes and methods`

class vehicle:
    def __init__(self,name,brand,color):
        self.name=name
        self.brand=brand
        self.color=color
        
    def running(self):
        print(f"the car name is{self.name} and the car brand is {self.brand} the color is {self.color}")
        
        
v=vehicle("911gt3rs","porsche","green")
v.running()
        class company:
    def shares(self,price,ipo,vesting_period):
        self.price=price
        self.ipo=ipo
        self.vesting_period=vesting_period
        print(f"the share price is{self.price} and the ipo is {self.ipo} and the vesting period would be{self.vesting_period}")
class company2(company):
    def sub_shares():
        print(f"the share price is{self.price} and the ipo is {self.ipo} and the vesting period would be{self.vesting_period}")
        
        

        
c=company()
c.shares("150$","100$","4 years")
c2=company2()
c2.shares("200$","140$","5years")
