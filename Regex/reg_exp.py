# findall function
import re

string="dileep"
x=re.findall("e",string)
print(x)
#search function
x=re.search("il",string)
print(x)
#methods in search
print(x.start())
print(x.span())
print(x.string)

# split function

x=re.split("i",string)
print(x)

# sub function

x=re.sub("d","D",string)
print(x)
