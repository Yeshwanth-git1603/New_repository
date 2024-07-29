# heirarichal class example on animals

class animal:
    def __init__(self,name,speak):
        self.a_name=name
        self.a_speak=speak
        
    def talk(self):
        print("the animal name is :",self.a_name)
        print("animal speaks is",self.a_speak)
    
class animal2(animal):
    def __init__(self,name,speak):
        super().__init__(name,speak)
    def talk(self):
        super().talk()
        pass
    
    
class animal3(animal):
    def __init__(self,name,speak):
        super().__init__(name,speak)
    def talk(self):
        super().talk()
        pass
    
class animal4(animal):
    def __init__(self,name,speak):
        super().__init__(name,speak)
    def talk(self):
        super().talk()
        pass
    
class animal5(animal):
    def __init__(self,name,speak):
        super().__init__(name,speak)
    def talk(self):
        super().talk()
        pass
    
    
    
a2=animal2("dog","bow bow")
a2.talk()

a3=animal3("cat","meow meow")
a3.talk()

a4=animal4("goat","meeeeh")
a4.talk()

a5=animal5("lion","roar")
a5.talk()
        
