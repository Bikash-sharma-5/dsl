def fibonacci_search(rl_num,x):
    fibMMm2 = 0
    fibMMm1 = 1 
    ct1=0
    fibM = fibMMm2 + fibMMm1
    n=len(rl_num)
   
    while (fibM < n) :
        fibMMm2 = fibMMm1
        fibMMm1 = fibM 
        ct1=ct1+1
        fibM = fibMMm2 + fibMMm1
   
   
   
    offset = -1 
   
   
    while (fibM >1) :
        
        i = min(offset + fibMMm2, n - 1)
        ct1=ct1+1
        if (rl_num[i] < x) :
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1 
            offset = i
        
   
       
        elif (rl_num[i] > x) :
            fibM = fibMMm2 
            fibMMm1 = fibMMm1 - fibMMm2
            fibMMm2 = fibM - fibMMm1
        
   
       
        else:
            print("total comparisons in fibonaci search: ",ct1)
            return 1 
    
    if(fibMMm1 and rl_num[n-1] == x):
        ct1=ct1+1
        print("total comparisons in fibonacci search: ",ct1)
        return 1
   
    return 0
 
  



    





def sentinal(rl,ky):
    key=rl[len(rl)-1]
    rl[len(rl)-1]=ky
    
    ct=0
    i=0
    while(ky!=rl[i]):
       i=i+1
       ct=ct+1
    rl[len(rl)-1]=key
    
    if i<(len(rl)-1) or rl[len(rl)-1]==ky:
        ct=ct+1
        print("total number of iteration required in sentinal: ",ct)
        return 1
    else :
        ct=ct+1
        print("total number of iteration required in sentinal: ",ct)
        return 0





def binary(rl,ele):
    x=len(rl)
    f=0
    l=x-1
    ct=0
    cmp=0
    rl.sort()
    check=False
    while f<=l:
        ct+=1
        mid=int((f+l)/2)
        if ele==rl[mid]:
           
            check=True
            break
        elif ele < rl[mid]:
            
            l=mid
        elif ele> rl[mid]:
            
            f=mid
    print("total number of comparisons required in binary search:",ct)
   
    return check







def linear(rl,ele):
    x=len(rl)
    ct=0
    cmp=0
    check=False
    for i in (rl):
        ct+=1
        
        if i==ele:
           
           check=True
           break
        else:
            cmp+=1
    print("total number of comparisons required in linear search:",ct) 
   
    return check    




print("total number of stuents:")
num_std=int(input())
roll_num=[]
print("enter rolll numbers that attend training program\n")
for i in range(num_std):
    x=int(input())
    roll_num.append(x)



for i in range(len(roll_num)):
    print("enter the roll number to search:")
    key=int(input())
    chek=linear(roll_num,key)
    if chek:
       print("roll number is present ")
    else:
       print("roll number is not present")
    chek1=binary(roll_num,key)
    if chek1:
       print("roll number is present ")
    else:
      print("roll number is not present")
    chek2=sentinal(roll_num,key)
    if chek2:
       print("roll number is present ")
    else:
       print("roll number is not present")

    chek2=sentinal(roll_num,key)
    if chek2:
       print("roll number is present ")
    else:
       print("roll number is not present")
    chek3=fibonacci_search(roll_num,key)
    if chek3:
       print("roll number is present ")
    else:
       print("roll number is not present")

