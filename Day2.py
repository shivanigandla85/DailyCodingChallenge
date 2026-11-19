# #Reverse a number
n=int(input("enter a number:"))
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10
print("The reversed number is:",rev)


# #Count the number of digits
n=int(input("enter a number:"))
count=0
while n> 0:
    n=n//10
    count+=1
print("The number of digits is:",count)


#amstrong number
n=int(input("enter a num:"))
temp=n
sum=0
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
if sum==n:
    print(n,"Armstrong num")
else:
    print(n,"not Armstrong num")



#perfect number
n=int(input("enter a num:"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if sum==n:
    print(n,"perfect num")
else:
    print(n,"not perfect num")


#multiplication table
n=int(input("enter a num:"))
for i in range(1,11):
    print(n,"*",i,"=",n*i)

