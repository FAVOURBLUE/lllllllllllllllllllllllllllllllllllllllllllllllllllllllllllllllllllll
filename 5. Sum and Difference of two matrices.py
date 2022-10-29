r=int(input("Enter the no. of rows :"))
c=int(input("Enter the no. of columns :")) 
mat1=[ ]
print("Enter the elements for 1st Matrix :") 
for i in range(r) :
    mat1.append([ ]) 
    for j in range(c) :
        num=int(input()) 
        mat1[i].append(num)
print("Matrix 1 is : ") 
for i in range(r):
    for j in range(c) : 
        print(mat1[i][j],end=" ")
    print() 
mat2=[ ]
print("Enter the elements for 2nd Matrix :") 
for i in range(r) :
    mat2.append([ ]) 
    for j in range(c) :
        num=int(input()) 
    mat2[i].append(num)
print("Matrix 2 is : ") 
for i in range(r):
    for j in range(c) : 
        print(mat2[i][j],end=" ")
    print()
mat3=[ ]
for i in range(r) : 
    mat3.append([ ]) 
    for j in range(c) :
        sum=0
    sum=(mat1[i][j] + mat2[i][j]) 
    mat3[i].append(sum)
print("\nAddition Result of Two given Matrix is :") 
for i in range(r):
    for j in range(c) : 
        print(mat3[i][j],end=" ")
print()