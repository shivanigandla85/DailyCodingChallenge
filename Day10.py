#requency of each element in an array
arr=list(map(int, input("Enter array: ").split()))
unique=[]
for i in arr:
    if i not in unique:
        unique.append(i)
        print(i, "=", arr.count(i), "times")



#Check whether two strings are Anagrams
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
if sorted(s1) == sorted(s2):
    print("Anagram")
else:
    print("Not Anagram")




#Find the longest word in a sentence
s=input("enter a sentence: ")
w=s.split()
l=""
for i in w:
    if len(i)>len(l):
        l=i
print(l)


#Count the pairs whose sum equals a target
arr=list(map(int,input("enter arr: ").split()))
target=int(input("enter target:"))
pairs=[]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==target:
            pairs.append((arr[i],arr[j]))
print(pairs)


#Rotate an array by one position to the right
arr=list(map(int,input("enter arr: ").split()))
last = arr.pop()
arr.insert(0, last)
print(arr)


