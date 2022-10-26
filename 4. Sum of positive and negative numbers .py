num=[ ] 
posum=0 
negsum=0 
positive=[ ] 
negative= [ ] 
i=0
n=int(input(“Enter the limit:”)) 
while(i<n):
a=int(input(“Enter the number :”)) 
num.append(a)
i=i+1 for i 
in num :
if (i>0) : 
positive.append(i) 
posum+=i
else : 
negative.append(i) 
negsum+=i
print(“The given list is :”,num)
print(“The list of positive numbers :”,positive) 
print(“The list of negative numbers :”,negative) 
print(“The sum of positive numbers :”,posum) 
print(“The sum of negative numbers :”,negsum)