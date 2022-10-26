import math
print(“Program to calculate quadratic equation”) 
a=int(input(“Enter a:”))
b=int(input(“Enter b:”)) 
c=int(input(“Enter c:”)) 
if a==0:
print(“Value of “,a,”should not be zero”) 
print(“\n Aborting!!!”)
else:
delta=b*b-4*a*c if 
delta>0:
root1=(-b+math.sqrt(delta))/(2*a) 
root2=(-b-math.sqrt(delta))/(2*a) 
print(“Roots are Real & Unequal”) 
print(“Root1=”,root1,”Root2=”,root2)
elif delta==0: 
root1=-b/(2*a)
print(“Roots are Real & Equal”) 
print(“Root1=”,root1,”Root2=”,root1)
else:
print(“Roots are Complex & Imaginary”)