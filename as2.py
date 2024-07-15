def union(x,y):
    un=x.copy()
    for i in y:
        if (i not in un):
            un.append(i)
    return un

def intersection(x1,y1):
    inter=[]
    for i in x1:
        if(i in y1):
            inter.append(i)
    return inter

def substraction(x2,y2):
    subst=[]
    for i in x2:
        if(i not in y2):
            subst.append(i)
    return subst


n=int(input("Enter total no of students: "))
a=[]
b=[]
c=[]
num_a=int(input("enter number of students who play cricket: "))
print("enter roll no of students who play cricket:")
for i in range(num_a):
    x=int(input())
    a.append(x)

num_b=int(input("entrnumber of students who play badminton: "))
print("enter roll no of students who play badminton:")
for i in range(num_b):
    x=int(input())
    b.append(x)

num_c=int(input("entrnumber of students who play football: "))
print("enter roll no of students who ply football:")
for i in range(num_c):
    x=int(input())
    c.append(x)

print("the required list are: ")
print("cricket: ",a)
print("badminton: ",b)
print("football: ",c)

print("students who play both cricket and badminton: ",intersection(a,b))
print("no of students who play neither cricket nor badminton: ",n-len(union(a,b)))
print("sudents who play either cricket or badminton but not both: ",substraction(union(a,b),intersection(a,b)))
print("students who play all the gams: ",intersection(c,intersection(a,b)))
print("students who play at least one game: ",union(c,union(a,b)))
print("students who do not lay any game: ",n-len(union(c,union(a,b))))
print("number of students who play cricket and football but not badminton: ",len(union(a,b))-len(c))