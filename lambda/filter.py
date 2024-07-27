# using filter function added with function code

def is_even(x):
    if x % 2==0:
        print("even")
    else:
        print("odd")
        
is_even(5)
        
# using filter function

l1=[11,21,32,43,22,34]

res=filter(lambda x:True if x%2==0 else False,l1)
print(list(res))
