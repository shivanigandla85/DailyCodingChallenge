
#positive negitive or zero
n=int(input("enter a number: "))
if n < 0 : 
    print("Negative")
elif n==0:
    print("Zero")
else:
    print("positive")




#Sum of even numbers
n=int(input("enter a num: "))
sum=0
for i in range(1,n+1):
    if i%2==0:
        sum=sum+i
print(sum)



#pattern printing
n=int(input("enter a num: "))
for i in range(1,n+1):
        print("*"*i)



# vowels in a string
s=input("enter a string: ")
vowels="aeiouAEIOU"
sum=0
for char in s:
    if char in vowels:
        sum+=1
print("number of vowels:",sum)




#max of 3 numbers
a=int(input("enter a num: "))
b=int(input("enter a num: "))
c=int(input("enter a num: "))
if a>=b and a>=c:
    print(a,"is the maximum number")
elif b>=a and b>=c:
    print(b,"is the maximum number")
else:
    print(c,"is the maximum number")
