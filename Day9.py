#Automorphic Number
n=int(input("enter a num: "))
a=n*n
if str(a).endswith(str(n)):
    print("automorphic")
else:
    print("not automorphic")


#pattern printing
n=int(input("enter a num: "))
for i in range(n):
    for j in range(i+1):
        print((i+j)%2, end="")
    print()


#non repeatable letters in a string
s = input("enter a string: ")
for i in s:
    if s.count(i) == 1:
        print(i)


#majority element in array*****
arr=list(map(int,input("enter a arr: ").split()))
n=len(arr)
for i in arr:
    count=arr.count(i)
    if count > n/2:
        print("majority element",i)
        break
else:
    print("no majority element")




#Move all zeros to the end of an array*********
arr=list(map(int,input("enter arr: ").split()))
new=[]
for i in arr:
    if i!=0:
        new.append(i)
for i in arr:
    if i==0:
        new.append(i)
print(new)