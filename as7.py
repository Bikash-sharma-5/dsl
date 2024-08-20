def selection_sort(l,li):
    for i in range(0,l-1):
        x=li[i]
        index=i
        for j in range(i+1,l):
            if x>li[j]:
               x=li[j]
               index=j
        li[i],li[index]=li[index],li[i]

    print(li)


def insertion_sort(l,li):
    for i in range(1,l):
       
       
        j=i
        while j>0 and li[i]<li[i-1]:

           li[i],li[i-1]=li[i-1],li[i]
           j=j-1
               

    print(li)




def bubble_sort(l,li):
    for i in range(l):
       
        for j in range(l-i-1):
            if li[j]>li[j+1]:
                li[j],li[j+1]=li[j+1],li[j]

    print(li)



print("enter the length of list:")
le=int(input())

li=[]
for i in range(le):
    print("enter the nubers that to be sorted")
    x=int(input())
    li.append(x)
print("--------------------------")
print("choose the option:")
print("choose:1 for bubble sort")
print("choose:2 for selection sort")
print("choose:3 for insertion sort sort")
print("the sorted array is: ")
print("---------------------------")

while 1:
    print("enter the option:")
    op=int(input())
    if op==1:
        bubble_sort(le,li)
    elif op==2:
        selection_sort(le,li)
    elif op==3:
        insertion_sort(le,li)
    print("you want to continue press 0 is not press 1:")
    y=int(input())
    if y==0:
        break




    
