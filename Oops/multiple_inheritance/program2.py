# multiple inheritance

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(f"the name of the person is:{self.name}") 
        print(f"and the age of the person is:{self.age}")
        
class employee:
    def __init__(self,eid,eref):
        self.eid=eid
        self.eref=eref
        print(f"the id of the employee is:{self.eid}")
        print(f"the employee ref id is:{self.eref}")
class manager(person,employee):
    def __init__(self,name,age,eid,eref,mname):
        super().__init__(name,age)
        employee.__init__(self,eid,eref)
        self.mname=mname
        
        print(f"the manager name is:{self.mname}")
        
m=manager("yeshwanth",23,"12345","efr200","yeshwanth")
