[200~for i in range(1,6):
      for j in range(1,6):
          print("*",end=" ")
      print(end="\n")
      
      
  n=int(input('enter a number'))
  for i in range(n):
      print("+"*i)
      
  l=[10,20,30,40,50,60,70,80,20,30,40]

  s=[]

  for x in l:
      if x not in s:
          s.append(x)
  print(s)

  max=80

  if max in s:
      print("max value is found",max)
  else:
      print("not found")


  count=0
  for i in range(1,100):
      if i%2==0:
          print("not prime",i)
          break
      else:
          if i%2==1:
              print("prime",i)
              
              

  i=1
  j=1
  k=1
  while i<=1:
      print(i)
      i+=1
      while j<=2:
          print(j,end=" ")
          j+=1

  while k<=3:
      print(k)
      k+=1
            
for x in range(1,5):
        print(" * "*x)
            
            for x in range(1,5):
                    print("*",end=" ")
                        for y in range(1,5):
                                    print(y,end=" ")
                                        
