# using reduce function and adding basic sum of given numbers

from functools import reduce
def nums_sum():
    sum1=0
    for x in range(1,11):
        sum1=sum1+x
    print("the sum of given nums is",sum1)
        
nums_sum()

# using reduce function
l3=[1,2,3,4,5,6,7,8,9,10]

res3=reduce(lambda x,y:x+y,l3)
print(res3)


