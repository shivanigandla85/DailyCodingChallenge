#sum of digits of a number
n=int(input("enter a number:"))
sum=0
while n>0:
    digit=n%10
    sum=sum+digit
    n=n//10
print("sum of digits:",sum)



#Prime number check
n=int(input("Enter a number:"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print("prime num")
else:
    print("not a prime num")



#Palindrome check
s=input("Enter a string:")
if s==s[::-1]:
    print("palindrome")
else:
    print("not a palindrome")



#Fibonacci series
n=int(input("enter a number: "))
a=0
b=1
for i in range(n):
    print(a)
    c=a+b
    a=b
    b=c



#factorial of a number
n=int(input("enter a number: "))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)


