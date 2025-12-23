   #take input from user
a = int(input("enter first number:"))
b = int(input("enter second number:"))
    
    #add two numbers
sum = a+b
print("sum =",sum)

    #check which number is bigger
if a > b:
    print(a, "is bigger")
elif b > a:
    print(b, "is bigger")
else:
    print("both number are equal")