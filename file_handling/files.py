#file handling methods
# using write mode

f=open("sample.txt","w")
f.write("hello there good morning")
l1=["good day to you"]
f.writelines(l1)
f.close()

f=open("sample.txt","r")
print(f.read())

for x in f.readlines():
    print(x)
    
# using append mode

f=open("sample.txt","a")
f.write("python codes are written here")
f.close()

f=open("sample.txt","r")
print(f.readlines())

# using read mode

f=open("sample.txt","r")
print(f.read())




