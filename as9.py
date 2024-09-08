def radix_sort1(l,arr):
    arr1=[0]*l
    li=[0]*10
    lg=max(arr)
    ct=0
    
    while lg>0:
        ct+=1
        lg//=10
    dv=1
    while ct>0:
        for i in range(0,l):
            lst=int((arr[i]//dv)%10)
            li[lst]+=1
        for j in range(1,10):
            li[j]+=li[j-1]
        k=l-1
       
        while k>=0:
             lst=int((arr[k]//dv)%10)
             arr1[li[lst] - 1] = arr[k]
             li[lst]-=1
             k-=1
        
        for i in range(0,l):
            arr[i]=arr1[i]
        ct-=1
        li=[0]*10
        dv*=10
    print(arr)


 





def radix_sort(l,arr):
    li=[[],[],[],[],[],[],[],[],[],[]]
    lg=max(arr)
    ct=0
    
    while lg>0:
        ct+=1
        lg//=10
    dv=1
    while ct>0:
       
        for i in range(0,l):
            lst=int((arr[i]//dv)%10)
           
            li[lst].append(arr[i])
        dv=dv*10
       
        k=0
        arr=[]
        for i in range(0,10):
            for j in range(len(li[i])):
               arr.append(li[i].pop(0))

               k=k+1
        ct=ct-1
    print(arr)

print("enter the length of list:")
le=int(input())

li=[]
for i in range(le):
    print("enter the nubers ")
    x=int(input())
    li.append(x)
radix_sort(le,li)
radix_sort1(le,li)

