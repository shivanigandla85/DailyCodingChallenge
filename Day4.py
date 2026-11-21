# #Divisibility Check
n=int(input("enter a num: "))
if n%5==0 & n%11==0:
    print(n,"id divisible")
else:
    print(n,"is not divisible")



#patten printing
n=int(input("enter a num: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()



#Second Largest Number without Sorting

a = int(input("Enter number: "))
b = int(input("Enter number: "))
c = int(input("Enter number: "))
d = int(input("Enter number: "))
e = int(input("Enter number: "))

numbers = [a, b, c, d, e]

largest = 0
second = 0

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Largest:", largest)
print("Second largest:", second)


#product of all digits

n = int(input("enter a num: "))
p = 1

while n > 0:
    digit = n % 10
    p = p * digit
    n = n // 10

print(p)


#Strong Number
n = int(input("Enter a number: "))
temp = n
total = 0
while temp > 0:
    digit = temp % 10
    fact = 1
    for i in range(1, digit + 1):
        fact = fact * i
    total = total + fact
    temp = temp // 10
if total == n:
    print("Strong Number")
else:
    print("Not a Strong Number")