class addition:
    def sum1(self,a,b):
        self.a=a
        self.b=b
        res=self.a+self.b
        print(f"the sum of {self.a} and {self.b} is {res}")
class subtraction(addition):
    def diff(self,a,b):
        self.a=a
        self.b=b
        res=self.a-self.b
        print(f"the diff of {self.a} and {self.b} is {res}")

a=addition()
a.sum1(1,2)
s=subtraction()
s.diff(10,5)

