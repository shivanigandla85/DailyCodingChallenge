#Temperature Conversion
c=int(input("enter Celsius: "))
F=(c*9/5)+32
print("Fahrenheit:", F)

#Harshad Number
n=int(input("Enter a number: "))
div=int(input("Enter a divisor: "))
sum=0
while n>0:
    digit=n%10
    sum+=digit
    n//=10
if sum%div==0:
    print("Harshad Number")
else:
    print("Not a Harshad Number")


#Inverted Star Pattern
n=int(input("Enter size: "))
for i in range(n,0,-1):
    print("*"*i)


#Count Vowels and Consonants
s=input("Enter a string: ")
v=0
c=0
for i in s:
    if i in "aeiouAEIOU":
        v+=1
    else:
        c+=1
print("Vowels:", v)
print("Consonants:", c)


#Find the GCD
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
for i in range(1,min(a,b)+1):
    if a%i==0 and b%i==0:
        gcd=i
print("GCD:", gcd)