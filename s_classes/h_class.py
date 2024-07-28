# single level inheritance

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def display(self):
        print("name is :",self.name)
        print("age is:",self.age)
        
class student(person):
    def __init__(self,name,age,sid,branch):
        super().__init__(name,age)
        self.student_id=sid
        self.major=branch
        
    def display(self):
        super().display()
        print("the student id is:",self.student_id)
        print("the student branch is:",self.major)
        
        
class teacher(person):
    def __init__(self,name,age,tid,sub,t_contact):
        super().__init__(name,age)
        self.teacher_id=tid
        self.subject=sub
        self.contact=t_contact
        
    def display(self):
        super().display()
        print("the teacher id is:",self.teacher_id)
        print("the subject is :",self.subject)
        print("the contact is:",self.contact)
    
        
        
s1=student("yeshwanth",23,565,"cse")
s1.display()

t1=teacher("rambo",23,"23","jungle","6600565655")
t1.display()




