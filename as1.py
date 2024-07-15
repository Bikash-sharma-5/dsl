num_std=int(input("enter number of students: "))
abs_std=0
marks=[]
total_marks=0
print("enter marks of student")

for i in range(0,num_std):
    x=int(input())
    if x<0:
        abs_std+=1
    else:
        marks.append(x)
        total_marks+=x
avg_marks=total_marks/num_std
max_marks=max(marks)
min_marks=min(marks)
hghfreq=1
ttl=1
marks2=0
marks.sort()
for i in range (1,len(marks)):
    if marks[i]!=marks[i-1]:
        if ttl>hghfreq:
            marks2=marks[i-1]
            hghfreq=max(hghfreq,ttl)
            ttl+=1
print("average marks of class: ",avg_marks)
print("highest score is: ",max_marks)
print("number of absent student is : ",abs_std)
print("marks with high freq : ",marks2)