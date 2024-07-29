# single level inheritance 

class telangana:
    def __init__(self,name,places,capital):
        self.t_name=name
        self.t_places=places
        self.t_capital=capital
        
    def display(self):
        print("the name of the state is:",self.t_name)
        print("the famous places are:",self.t_places)
        print("the capital is:",self.t_capital)
        
class andhra(telangana):
    def __init__(self,name,places,capital,cm):
        super().__init__(name,places,capital)
        self.a_cm=cm
        
    def display(self):
        super().display()
        print("the cm of AP is:",self.a_cm)
        
        
        
t=telangana("telangana","charminar,golkonda,qutib minar,museum,zoo","hyderabad")
t.display()
a=andhra("andhra","tirupati,tirumala,yaganti,kalahasthi","amaravati","chandra babu")
a.display()
