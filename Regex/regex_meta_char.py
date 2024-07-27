# meta characters for the string
#[] prints from the given ranhe in the brackets
wish="happy birthday to you happy birthday happy birthday to you 1672629"
x=re.findall("[a-m]",wish)
print(x)
x=re.findall("[1-9]",wish)
print(x)
#'.' period used to find the strings doesnt care about the in between strings
x=re.findall("h.{3}y",wish)
print(x)
# '$' to find the last character 
x=re.findall("h.$y",wish)
print(x)

# ''^' to find the first character

x=re.findall("^t.o",wish)
print(x)
# '*' to find whethere occurances are zero or more
x=re.findall("h*.y",wish)
print(x)
# '+' to find the occurances are one or more
x=re.findall("h+.{3}",wish)
print(x)

# '?' to find the occcurances zero or one
x=re.findall("h?y",wish)
print(x)

# '|' either find one word or finds the another word given

x=re.findall("bith|birthday",wish)
print(x)

#'\' escape char used to find the given word or . or ? or any special character

x=re.findall("\ happy",wish)
print(x)

