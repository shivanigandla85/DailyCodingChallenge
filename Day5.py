#Neon Number
n=int(input("enter a num: "))
s=n*n
sum=0
while s>0:
    digit=s%10 
    sum= digit + sum
    s= s//10
if sum==n:
    print("Neon Number")
else:
    print("Not a Neon Number")



#Reverse counting
n=int(input("enter a num: "))
for i in range(n,0,-1):
    print(i)



#remove duplicates from string
s=input("Enter a string: ")
result=""
for i in s:
    if i not in result:
        result+=i
print("String without duplicates:", result)




#Find Missing Number
arr=list(map(int,input("Enter nums separated by space: ").split()))
for i in range(1,len(arr)+2):
    if i not in arr:
        print("Missing number:", i)
    



#two sum problem
arr=list(map(int,input("Enter nums separated by space: ").split()))
target=int(input("Enter the target sum: "))
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==target:
            print("Pair found:", arr[i], arr[j])