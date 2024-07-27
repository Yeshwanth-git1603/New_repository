#inner classes in python

class outer:
    def out_func(self,hero,heroin):
        self.hero=hero
        self.heroin=heroin
        print(f"hero is {self.hero} and the heroin is {self.heroin}")
        
    class inner:
        def inn_func(self,movie):
            self.movie=movie
            print(f"the movie name is {self.movie}")
            
o=outer()
o.out_func("spiderman","spidergwen")
i=o.inner()
i.inn_func("spiderman")

