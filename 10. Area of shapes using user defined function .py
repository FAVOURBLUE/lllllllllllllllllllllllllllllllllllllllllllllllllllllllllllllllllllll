def 
rectangle(l,b): 
area=l*b
print("area=",area,"cm²) 
def square(a):
area=a*a 
print("area=",area,"cm²)
def circle(r): area=3.14*r*r
print("area=",area,"cm²") 
def triangle(b,h):
area=0.5*b*h 
print("area=",area,"cm²")
ch=int(input("1.rectangle\n2.square\n3.circle\n4.triangle\nenter your choice:"))
if(ch==1):
l=float(input("enter length:")) 
b=float(input("enter 
breadth:")) rectangle(l,b)
elif(ch==2):
a=float(input("Enter the side length:")) 
square(a)
elif(ch==3):
r=float(input("Enter the radius of circle:")) 
circle(r)
elif(ch==4):
b=float(input("enter breadth:")) 
h=float(input("enter height:")) 
triangle(b,h)
else:
print("Invalid choice.Choose from 1-4")
