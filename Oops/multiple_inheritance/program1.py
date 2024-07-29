# multiple inheritance for vehicle class

class vw:
    def __init__(self,child):
        self.vw_child=child
        
    def display(self):
        print("the child name is:",self.vw_child)
        
class audi(vw):
    def __init__(self,child,parent):
        super().__init__(child)
        self.vw_parent=parent
        pass
    
    def display(self):
        super().display()
        pass
    
class bmw(audi,vw):
    def __init__(self,child,parent):
        super().__init__(child,parent)
        
    def display(self):
        super().display()
        print("the parent name is:",self.vw_parent)
        print("the  child name is:",self.vw_child)
    
a=audi("audi","vw")
a.display()

b=bmw("rolls royce","bmw")
b.display()
