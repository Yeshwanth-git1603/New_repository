# min of two
y=lambda x , y : x if x<y else y
print(y(2,3))

# max of tree

z=lambda x,y,z: x if x>y and x>z else y if y>z else z
print(z(10,3,4))





# min of three
z=lambda x,y,z: x if x<y and x<z else y if y<z else z
print(z(2,3,4))



#even check

s=lambda x:"even" if x%2==0 else "odd"
x=9
print(s(x))



#leap year

z=lambda x :"leap year" if x%4==0 else "non leap year"
x=2968
print(z(x))




# positive or negative

res=lambda x,y,z :"negative x" if x<0 or "negative y" y<0 or z<0 else "positive"
x=-2
y=-33
z=1
print(res(x,y,z))

neg=lambda x:"negative" if x<0 else "positive"
print(neg(-9))


p=lambda x :"not prime" if x % 2==0  else "prime"
print(p(97))





# filter
l1=[11,2,3,34,55,66,77,88]
res=(filter(lambda x : True if x % 2==0 else False ,l1))
print(list(res))









