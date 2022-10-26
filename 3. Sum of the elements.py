Start=int(input("Enter the starting value ")) 
End=int(input("Enter the ending value")) 
sum=0
for num in range(Start,End+1): 
    sum+=num
    print("Sum = ",sum) 
else:
    print("The starting and ending value must be positive numbers")