# dictionary in classes

class anime:
    def hashiras(self):
        
        
        dict1={"name":"gyomei","age":"27","breathing_style":"stone breathing"}
        dict2={"name":"sanemi","age":"23","breathing_style":"wind breathing"}
        dict3={"name":"giyu","age":"22","breathing_style":"water breathing"}
        dict4={"name":"obanai","age":"22","breathing_style":"serpant breathing"}
        dict5={"name":"muichiro","age":"14","breathing_style":"mist breathing"}
        dict6={"name":"mitsuri","age":"22","breathing_style":"love breathing"}
        dict7={"name":"shinobu","age":"22","breathing_style":"insect breathing"}
        
        
        self.dict1=dict1
        self.dict2=dict2
        self.dict3=dict3
        self.dict4=dict4
        self.dict5=dict5
        self.dict6=dict6
        self.dict7=dict7
        
        for g in dict1.values():
            print(g)
        for s in dict2.values():
            print(s)
        for g in dict3.values():
            print(g)
        for o in dict4.values():
            print(o)
        for m in dict5.values():
            print(m)
        for m2 in dict6.values():
            print(m2)
        for s in dict7.values():
            print(s)
            
    def demons(self):
    
        d1={"name":"kokushibo","rank":"upper moon one"}
        d2={"name":"douma","rank":"upper moon two"}
        d3={"name":"akaza","rank":"upper moon three"}
        
        
        self.d1=d1
        self.d2=d2
        self.d3=d3
        
        print(self.d1,self.d2,self.d3)

        
        
a=anime()
a.hashiras()
a.demons()
        
