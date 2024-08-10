def fibonacci_search(rl_num,x):
    fibMMm2 = 0
    fibMMm1 = 1 
    fibM = fibMMm2 + fibMMm1
    n=len(rl_num)
   
    while (fibM < n) :
        fibMMm2 = fibMMm1
        fibMMm1 = fibM 
        fibM = fibMMm2 + fibMMm1
    
   
   
    offset = -1 
   
   
    while (fibM >=1) :
        
        i = min(offset + fibMMm2, n - 1)
   
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
            return 1 
    
    if(fibMMm1 and rl_num[n-1] == x):
        return 1
   
    return 0
 
  





rl_num=[]
print("enter total number of student that attend lecture")
tl_std=int(input())
print("enter rool number of students that  attend lecture")
for i in range(0,tl_std):
    x=int(input())
    rl_num.append(x)
rl_num.sort()
rl_ck=int(input(("enter roll number to check whether it attend lecture or not: ")))
pr_n=fibonacci_search(rl_num,rl_ck)
if pr_n:
    print("roll numberis prsent")
else:
    print("roll number is not present")