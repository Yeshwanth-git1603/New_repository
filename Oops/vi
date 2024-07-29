# heirarichal class

class people:
    def __init__(self,name,age,phno):
        self.p_name=name
        self.p_age=age
        self.p_phno=phno
        
    def display(self):
        print("the name of the person is",self.p_name)
        print("the age of the person is",self.p_age)
        print("the phno of the person is",self.p_phno)
        
        
class friend(people):
    def __init__(self,name,age,phno,weight):
        super().__init__(name,age,phno)
        self.p_weight=weight
        
    def display(self):
        super().display()
        print("the weight of the person is ",self.p_weight)
        
class friend2(people):
    def __init__(self,name,age,phno,height):
        super().__init__(name,age,phno)
        self.p_height=height
        
    def display(self):
        super().display()
        print("the height of the person is",self.p_height)
        
        
        
f=friend("yeshwanth",23,"6305464772","100")
f.display()

f2=friend2("mukesh",23,"73883833","5.8")
f2.display()
