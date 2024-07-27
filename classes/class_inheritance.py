# using single level inheritance in classes

class mamals:
    def whale(self,name,lifespan,food):
        self.name=name
        self.lifespan=lifespan
        self.food=food
        print(f"the mamal is {self.name},and the lifespan is {self.lifespan} and the food it eats are {self.food}")
        
class mamals2(mamals):
    def dolphin(self):
        pass

        
        
        
        
        
m1=mamals()
m1.whale("blue whale","500 years","fishes")
m2=mamals2()
m2.whale("dolphin","50 years","fishes")

