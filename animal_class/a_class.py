# heirarichal animal class

class animal:
    def __init__(self,name,color,lifespan):
        self.a_name=name
        self.a_color=color
        self.a_lifespan=lifespan
        
    def display(self):
        print("the animal name is:",self.a_name)
        print("the animal color is:",self.a_color)
        print("the animal lifespan is:",self.a_lifespan)
        
class whale(animal):
    def __init__(self,name,color,lifespan,weight):
        super().__init__(name,color,lifespan)
        self.a_weight=weight
        
    def display(self):
        super().display()
        print("the animal weight is:",self.a_weight)
        
class stingray(animal):
    def __init__(self,name,color,lifespan,speed):
        super().__init__(name,color,lifespan)
        self.a_speed=speed
        
    def display(self):
        super().display()
        print("the speed of the animal is",self.a_speed)

        
w=whale("killer whale","blue","100years","100tons")
w.display()

s=stingray("stingray","gray","100 years","100kmph")
s.display()
