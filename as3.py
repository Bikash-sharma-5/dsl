def add(matrix1,matrix2):
    row=len(matrix1)
    col=len(matrix1[0])
    row1=len(matrix2)
    col1=len(matrix2[0])
    result=[[0]*col for _ in range(row)]

    if(row!=row1 or col1!=col):
        return None
    else:
        for row in range (row):
            for coloumn in range(col):
                result[row][coloumn]=matrix1[row][coloumn]+matrix2[row][coloumn]
    return result

def subs(matrix1,matrix2):
    row=len(matrix1)
    col=len(matrix1[0])
    row1=len(matrix2)
    col1=len(matrix2[0])
    result=[[0]*col for _ in range(row)]

    if(row!=row1 or col1!=col):
        return None
    else:
        for row in range (row):
            for coloumn in range(col):
                result[row][coloumn]=matrix1[row][coloumn] - matrix2[row][coloumn]
    return result

def multiply(matrix1,matrix2):
    row=len(matrix1)
    col=len(matrix1[0])
    row1=len(matrix2)
    col1=len(matrix2[0])
    result=[[0]*col1 for _ in range(row)]

    if(col!=row1):
        return None
    
    for i in range (row):
            for j in range(col1):
                for k in range(col):
                  result[i][j]+=matrix1[i][k]*matrix2[j][k]
    return result

def diag_ele(matrix):
    result=0
    row=len(matrix)
    col=len(matrix[0])
    if row!=col:
        return None
    for i in range(len(matrix)):
        result+=matrix[i][i] 

    return result

def uppr_tria(matrix):
    row=len(matrix)
    col=len(matrix[0])
    is_upper=True
    for i in range (row):
            for j in range(i):
                if matrix[i][j]!=0:
                    is_upper=False
                    break
    if is_upper:
        return True
    else:
        return False
    


    


def trans(matrix):
   
    row=len(matrix)
    col=len(matrix[0])
    result= [[0]*row for _ in range(col)]
    for row in range (row):
            for coloumn in range(col):
                result[coloumn][row]=matrix[row][coloumn]

    return result

def saddle_pt(matrix):
     row=len(matrix)
     col=len(matrix[0])
     for i in range(row):
         min_ele=min(matrix[i])
         min_index=matrix[i].index(min_ele)

         is_saddle=True
         for k in range(row):
             if matrix[k][min_index]>min_ele:
                 is_saddle=False
                 break
         if is_saddle:
             return (i,min_index)
     return None


row=int(input("enter number of rows: "))
col=int(input("enter number of col1: "))

matrix1=[]
for i in range(row):
    a=[]
    for j in range(col):
        x=int(input())
        a.append(x)
    matrix1.append(a)

row1=int(input("enter number of rows: "))
col1=int(input("enter number of col1: "))

matrix2=[]
for i in range(row1):
    a=[]
    for j in range(col1):
        x=int(input())
        a.append(x)
    matrix2.append(a)

print("--------menu--------")
print("1.addition ")
print("2.substraction ")
print("3.multiplication ")
print("4.upper_triangular")
print("5.transpose")
print("6.sum_of_diagonal_ele ")
print("7.saddle")

for i in range(7):
    print("enter the option:")
    x=int(input())
    if x==1:
        add_matrix=add(matrix1,matrix2)
        if add_matrix:
          print("matrix addition:")
          for row in add_matrix:
            print(row)
          print()
    if x==2:
        subs_matrix=subs(matrix1,matrix2)
        if subs_matrix:
           print("matrix substraction:")
           for row in subs_matrix:
             print(row)
           print()
    if x==3:
        multiply_matrix=multiply(matrix1,matrix2)
        if multiply_matrix:
           print("matrix multiplication:")
           for row in multiply_matrix:
              print(row)
           print()

    if x==4:
        upper_tria=uppr_tria(matrix1)
        if upper_tria:
           print("matrix is upper traiangular")
        else:
           print("matrix is not upper triangular")
    if x==5:
        trans_matrix=trans(matrix1)
        if trans_matrix:
          print("transpose of matrix:")
        for row in trans_matrix:
          print(row)
        print()
    if x==6:
        sum_diag=diag_ele(matrix1)
        if sum_diag:
           print("sum of diagonal element:")
           print(sum_diag)
        print()
    if x==7:
        saddle_pt=saddle_pt(matrix1)
        if saddle_pt:
           print("saddle pt: ",saddle_pt)
        else:
            print("saddle pt is not present")











