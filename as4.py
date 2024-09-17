n1=int(input("Enter the highest power of polynomial 1: "))
n2=int(input("Enter the highest power of polynomial 2: "))
p1=[]
p2=[]
for i in range(0,n1+1):
    print("enter coeficient of polynomial 1 of",i,"th power of x: ")
    x=int(input())
    p1.append(x)
for i in range(0,n2+1):
    print("enter coeficient of polynomial 2 of",i,"th power of x: ")
    x=int(input())
    p2.append(x)
for i in range(n1,-1,-1):
    if p1[i]!=0:
      if i!=0:
       print(p1[i],"x^",i,end="")
    if i==0:
        print(p1[i])
    if i!=0:
        print("+",end="")

for i in range(n2,-1,-1):
    if p2[i]!=0:
      if i!=0:
        print(p2[i],"x^",i,end="")
      if i==0:
        print(p2[i],end="")
      if i!=0:
        print("+",end="")
pc=int(input("enter the polynomial to evaluate: "))
print("enter the number to evaluate for ",pc,"polynomial: ")
num=int(input())
ans=0
if pc==1:
   for i in range(0,n1+1):
     ans=ans+pow(num,i)*p1[i]
else:
    for i in range(0,n2+1):
     ans=ans+pow(num,i)*p2[i]

print("value of polynomial at ",num,"is : ", ans)

p3=[]
if n1>=n2:
    for i in range(0,n2+1):
       p3.append(p1[i]+p2[i])
    for i in range(n2+1,n1+1):
       p3.append(p1[i])
else:
     for i in range(0,n1+1):
       p3.append(p1[i]+p2[i])
     for i in range(n1+1,n2+1):
         p3.append(p2[i])
   
print("the addition of two polynomial is: ")
if n1>=n2:
  for i in range(n1,-1,-1):
    if p3[i]!=0:
      if i!=0:
       print(p3[i],"x^",i,end="")
      if i==0:
        print(p3[i])
      if i!=0:
        print("+",end="")
else:
     for i in range(n2,-1,-1):
         if p3[i]!=0:
              if i!=0:
                 print(p3[i],"x^",i,end="")
              if i==0:
                 print(p3[i])
              if i!=0:
                 print("+",end="")
print("multiplication of two matrices is: ")
ml=[0]*(n1+n2+1)
for i in range(0,n1+1):
    for j in range(0,n2+1):
        ml[i+j]+=p1[i]*p2[j]
       

for i in range(n1+n2,-1,-1):
    if ml[i]!=0:
      if i!=0:
       print(ml[i],"x^",i,end="")
      if i==0:
        print(ml[i])
      if i!=0:
        print("+",end="")
