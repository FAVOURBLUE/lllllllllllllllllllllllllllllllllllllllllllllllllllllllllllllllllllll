nterm=int(input("Enter how many terms "))
n1,n2=0,1
count=0
if nterm<=0:
 print("Enter the positive number")
elif nterm==1:
 print("Fibonacci sequence upto ", nterm)
 print(n1)
else:
 print("Fibonacci Series")
 while count<nterm:
 print(n1)
 nth=n1+n2
 n1=n2
 n2=nth
 count+=1
