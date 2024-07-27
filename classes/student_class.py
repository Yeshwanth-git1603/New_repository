# using single level inheritance in student data

class student:
    def details(self,name,age,height,weight,section):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
        self.section=section
        
    def display_details(self):
        print("the details of the student is here",self.name,self.age,self.height,self.weight,self.section)

        
class student2(student):
    def details_two(self):
        pass
    

s1=student()
s1.details("yeshwanth",23,5.9,100,"A")
s1.display_details()
s2=student2()
s2.details("mukesh",23,5.7,60,"A")
s2.display_details()
