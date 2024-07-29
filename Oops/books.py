# classs new class

#heirarichal class

class books:
    def __init__(self,name,author):
        self.b_name=name
        self.b_author=author
        
    def display(self):
        print("the book name is:",self.b_name)
        print("the author of the book is",self.b_author)
        
class book1(books):
    def __init__(self,name,author,dor):
        super().__init__(name,author)
        self.b_dor=dor
        
        
    def display(self):
        super().display()
        print("the date of release is:",self.b_dor)
        
class book2(books):
    def __init__(self,name,author,color):
        super().__init__(name,author)
        self.b_color=color
        
    def display(self):
        super().display()
        print("the color of the book is:",self.b_color)
        
b=book1("rich dad poor dad","robert kyoski","1990")
b.display()

b2=book2("think and grow rich","napolean hill","green")
b2.display()
