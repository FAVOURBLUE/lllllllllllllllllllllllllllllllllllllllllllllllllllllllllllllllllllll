#Temperature Conversion
print("1.Fahrenheit to Celsius\n2.Celsius to Fahrenheit \n") 
c=int(input("Enter your choice\n"))
if c==1:
    f=float(input("Enter the temperature in Fahrenheit\n")) 
    c=((f-32)*5)/9
    print("Celsius= ",c) 
elif c==2:
    c=float(input("Enter the temperature in Celsius \n")) 
    f=(c*9/5)+32
    print("Fahrenheit= ",f)
