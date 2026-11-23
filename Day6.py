#Swap Two Numbers without Using Third Variable
a=int(input("Enter a: "))
b=int(input("Enter b: "))
a=a+b
b=a-b
a=a-b
print("swapping: a =", a, "b =", b)



#Count Even and Odd Numbers
n=int(input("Enter a 1st number: "))
n=int(input("Enter a 2nd number: "))
n=int(input("Enter a 3rd number: "))
n=int(input("Enter a 4th number: "))
n=int(input("Enter a 5th number: "))
n=int(input("Enter a 6th number: "))
n=int(input("Enter a 7th number: "))
n=int(input("Enter a 8th number: "))
even=0
odd=0
for i in range(1,n+1):
    if i%2==0:
        even+=1
    else:
        odd+=1
print("Even nums:", even)
print("Odd nums:", odd)


#Electricity Bill

units=int(input("enter units: "))
if units<=100:
    bill=units*2
elif units<=200:
    bill=(100*2)+(units-100)*3
else:
    bill= (100*2) + (100*3) + (units-200) * 5
print("Electricity bill:", bill)


#Prime Factors of a Number
n=int(input("Enter a number: "))
factors=[]
for i in range(1,n+1):
    if n%i==0:
        factors.append(i)
print(factors)

#Hollow Square Pattern
n=int(input("Enter size: "))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()