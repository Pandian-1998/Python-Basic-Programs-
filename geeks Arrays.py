def sum(arr):
    n = 0
    for i in arr:
        n = n + i
    print(n)
arr=[1,2,3,4,5]
sum(arr)


#2- Program to find largest element in an array

def largest(arr):
    max = arr[0]
    for i in arr:
        if i > max:
            max = i
    return max
arr = [1,2,3,4,5]
ans = largest(arr)
print("largest element is",ans)


#3-Array rotation

def rotate(arr,n):
    for i in range(n,len(arr)+n):
        print(arr[i%len(arr)])
arr=[1,2,3,4,5,6]
rotate(arr,3)


#4-Array inverse rotation

def inverserotate(arr,n):
    for i in range(len(arr)-n,len(arr)-n+len(arr)):
        print(arr[i%len(arr)])
arr=[1,2,3,4,5,6]
inverserotate(arr,2)


#5-Program to Split the array and add the first part to the end

def rotate(arr,n):
    for i in range(n,len(arr)+n):
        print(arr[i%len(arr)])
arr=[1,2,3,4,5,6]
rotate(arr,3)


#6-Program for Find remainder of array multiplication divided by n

def remainder(arr,n):
    count = 1
    for i in arr:
        count = count * i
    answer = count % n
    print(answer)
arr=[100,10,5,25,35,14]
remainder(arr,11)


#8-Monotonic

def Monotonic(A):
    return (all(A[i] <= A[i + 1] for i in range(len(A) - 1)) or
            all(A[i] >= A[i + 1] for i in range(len(A) - 1))) 
A = [6,10,5,4,3]
print(Monotonic(A))

