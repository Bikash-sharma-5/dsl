rw=int(input("enter number of rows of sparse matrix: "))
cl=int(input("enter number of colomns of sparse matrix: "))
sp=[]
nz_el=0
sp_r=[]
sp_r.append([rw,cl,0])
for i in range(0,rw):
    sp1=[]
    print("enter elements of ",i+1,"th row")
    for j in range(0,cl):
        x=int(input())
       
        if x!=0:
            sp_r.append([i,j,x])
            nz_el=nz_el+1

        sp1.append(x)
    sp.append(sp1)

sp_r[0][2]=nz_el

print("sparce matrix is: ")
for i in range(0,rw):
    print(sp[i])

print("sparce matrix without zeroes: ")
for i in range(0,nz_el+1):
    print(sp_r[i])
rw1=int(input("enter number of rows of sparse matrix: "))
cl1=int(input("enter number of colomns of sparse matrix: "))
sp3=[]
nz_el1=0
sp_r1=[]
sp_r1.append([rw1,cl1,0])
for i in range(0,rw1):
    sp4=[]
    print("enter elements of ",i+1,"th row")
    for j in range(0,cl1):
        x=int(input())
       
        if x!=0:
            sp_r1.append([i,j,x])
            nz_el1=nz_el1+1

        sp4.append(x)
    sp3.append(sp4)
print("the second sparce matrix is : ")
for i in range(0,rw):
    print(sp3[i])

sp_r1[0][2]=nz_el

ad_sp=[]
nz_el2=0
sp_r3=[]
sp_r3.append([rw,cl,0])
for i in range(0,rw1):
    ad_sp1=[]
    for j in range(0,cl1):
        ad_sp1.append(sp[i][j]+sp3[i][j])
        if sp[i][j]+sp3[i][j]!=0:
           nz_el2=nz_el2+1
           sp_r3.append([i,j,sp[i][j]+sp3[i][j]])
    ad_sp.append(ad_sp1)
sp_r3[0][2]=nz_el2
print("adiition of two sparce matrix is : ")
for i in range(0,rw):
    print(ad_sp[i])
print("addition of space matrices without zeroes : ")
for i in range(0,nz_el2+1):
    print(sp_r3[i])
print("transpose of sparce matrix : ")
trans_sp=[0]*(nz_el+1)
ct=[0]*cl
trans_sp[0]=[cl,rw,nz_el]
for i in range(1,nz_el+1):
    ct[sp_r[i][1]]=ct[sp_r[i][1]]+1
index=[1]*(cl+1)
for i in range(1,cl+1):
    index[i]=index[i-1]+ct[i-1]

for i in range(1,nz_el+1):
   x=index[sp_r[i][1]]
   trans_sp[x]=[sp_r[i][1],sp_r[i][0],sp_r[i][2]]
   index[sp_r[i][1]]= index[sp_r[i][1]]+1

for i in range(0,nz_el+1):
    print(trans_sp[i])

