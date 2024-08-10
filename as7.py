def sentinelSearch( arr, key):

    ct=0
    n=len(arr)
    last = arr[n - 1]
 
    
    arr[n - 1] = key
    i = 0
 
    while (arr[i] != key):
        i=i+1
        ct=ct+1
 
    
    arr[n - 1] = last
 
    if ((i < n - 1) or (arr[n - 1] == key)):
        ct=ct+1
        print("total comparisons : ",ct)
        return 1
    else:
       ct=ct+1
       print("total comparisons: ",ct)
       return 0





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
            print("total comparisons: ",ct1)
            return 1 
    
    if(fibMMm1 and rl_num[n-1] == x):
        ct1=ct1+1
        print("total comparisons: ",ct1)
        return 1
   
    return 0
 
  





rl_num=[]
print("enter total number of student that attend lecture")
tl_std=int(input())
print("enter roll number of students that  attend lecture")
for i in range(0,tl_std):
    x=int(input())
    rl_num.append(x)
rl_num.sort()
rl_ck=int(input(("enter roll number to check whether it attend lecture or not by fibonacci: ")))
pr_n=fibonacci_search(rl_num,rl_ck)
if pr_n:
    print("roll numberis prsent")
else:
    print("roll number is not present")
rl_ck1=int(input(("enter roll number to check whether it attend lecture or not by sentinal search: ")))
pr_n1= sentinelSearch(rl_num,rl_ck1)
if pr_n1:
    print("roll numberis prsent")
else:
    print("roll number is not present")
