n=int(input("Enter the value of n: "))
for i in range(n + 1) :
 fact=1
 for j in range(1,i+1) :
 fact*=j
 term=(i / fact)
sum=1-term
print("Sum=",sum)