#Student Mark Details

print("Enter the marks")

mark1=int(input("Mark1: "))

mark2=int(input("Mark2: "))

mark3=int(input("Mark3: "))

total=mark1+mark2+mark3

print("Total = ",total)

perc=total/3

print ("Percentage = ",perc) 
if(perc>=90 and perc<=100):
    print("Grade is: A") 
    
elif(perc>=70 and perc<90):
    print("Grade is: B")

elif (perc>=50 and perc<70):
    print("Grade is: C")

elif (perc>=35 and perc<50): 
    print("Grade is: D")

elif (perc>=20 and perc<35):
    print("Grade is: E")

elif (perc>=0 and perc<20): 
    print("Grade is: F")
