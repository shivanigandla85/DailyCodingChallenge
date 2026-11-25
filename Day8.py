#Find the Smallest of Three Numbers without min()
a=int(input("Enter 1st num: "))
b=int(input("Enter 2nd num: "))
c=int(input("Enter 3rd num: "))
if a < b and a < c:
    print(a,"is smallest")
elif b < a and b < c:
    print(b,"is smallest")
else:
    print(c,"is smallest")




#Spy Number
n = int(input("enter a num: "))
temp=n
s=0
p=1
while n>0:
    digit=n%10
    s+=digit
    p*=digit
    n//=10
if s==p:
    print("spy num")
else:
    print("not a spy num")




#Number Triangle
n=int(input("enter num: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    print()




#Best Time to Buy and Sell Stock
prices=list(map(int, input("enter prices: ").split()))
min_price = prices[0]
max_profit = 0
for i in range(1, len(prices)):
    if prices[i] < min_price:
        min_price = prices[i]
    profit = prices[i] - min_price
    if profit > max_profit:
        max_profit = profit
print("Maximum Profit:", max_profit)





#Abundant Number
n=int(input("Enter a num: "))
s=0
for i in range(1, n):
    if n % i==0:
        s=s+i
if s>n:
    print("Abundant Num")
else:
    print("not Abundant Num")