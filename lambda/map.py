# using map function and adding basic function code

def prod_num(x):
    return x*x

l2=[1,2,3,4,5]
for i in l2:
    res=i*i
print("the prod of the give nums is",res)

#using map function

result=map(lambda x: x*x ,l2)
print(list(result))

