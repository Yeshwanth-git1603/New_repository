#simple class

class animal:
    def __init__(self,name,weight,food):
        self.name=name
        self.weight=weight
        self.food=food
        
    def display(self):
        print("the animal name is",self.name)
        print("the animal weight is",self.weight)
        print("the food animal eat is",self.food)
        
class whale(animal):
    def __init__(self,name,weight,food,color):
        self.color=color
        
    def display(self):
        print("the color of the animal is",self.color)

a=animal("blue whale","100tons","fishes")
a.display()
w=whale("blue whale","100tons","fishes","blue")
w.display()
