fruits=[]
colour=[]
numbers=[1,2,3,4,5,6,7,8,9]
n=int(input("Enter the list count: "))
for i in range(0,n):
 name=input("Enter the fruit name: ")
 fruits.append(name)
print(fruits)
for i in range(0,n):
 name=input("Enter the colour name: ")
 colour.append(name)
print(colour)
print("List concatenation")
print(fruits+colour)
print("List repetition")
print(fruits*3)
print("List membership operator")
print('apple' in fruits)
print('banana' not in fruits)
print(fruits[0])
print(fruits[2:3])
print(fruits[-1::])
