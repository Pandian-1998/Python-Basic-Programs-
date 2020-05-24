#1-program to interchange first and last elements in a list

def interchange(list):
    list[0],list[-1] = list[-1],list[0]

    return list
        
list = [10,2,3,20]
print(interchange(list))


#2-program to swap two elements in a list

def swapping(list,pos1,pos2):

    list[pos1],list[pos2] = list[pos2],list[pos1]
    return list
pos1=2
pos2=4
list=[2,3,4,5,6]
print(swapping(list,pos1-1,pos2-1))


#3-program to remove Nth occurrence of the given word

def remove(list,word,n):
    count = 0
    for i in range(0,len(list)):
        if list[i] == word:
            count = count + 1

            if count == n:
                del(list[i])
                return True
    return False
list = ["geeks","for","geeks"]
n = 2
word = "geeks"

flag = remove(list,word,n)

if(flag==True):
    print("Updated list is:",list)
else:
    print("list is not updated")


#4-Ways to find length of list

#naive

list = ["geeks","for","geeks"]

counter = 0
for i in list:
    counter  = counter + 1
print(counter)

#using len()
# print(len(list))

##5-Ways to check if element exists in list

def check(list,find):
    for i in list:
        if find == i:
            print(i)
list=[1,2,3,4,5]
find = 3
check(list,find)


#6-clear the list

list = [1,2,3,4,5]

print("list before clear",list)

list.clear()

print("list after clearing",list)


#7-reversing the list

def ging(list):
    new = []
    for i in list:
        new.insert(0,i)
    return new
list = ["geeks","for","geem"]
print(ging(list))

def reverse(list):
    list.reverse()
    return list
list = [10,9,8,7,6,5,4,3,2,1]
print(reverse(list))


#8-cloning the list

def cloning(list):
    list1=[]
    list1.extend(list)
    return list1
list=[1,2,3]
li2=cloning(list)
print("orginal list",list)
print("cloning list",li2)


#9-Count occurrences of an element in a list

def counting(list,num):
    count = 0
    for i in list:
        if num == i:
            count = count + 1
    return count
list = [10,2,3,3,10,10,5,4,9]
num=3
print(f"number of occurences of {num} is ",counting(list,num))


#10-sum of elements of list

def sum(list):
    add = 0
    for i in list:
        add = add + i
    return add
list = [1,2,3,4]
print(sum(list))


#11-multiply elements in a list

def multiply(list):
    mul = 1
    for i in list:
        mul = mul * i
    return mul
list = [5,5,5]
print(multiply(list))


#12-program to find smallest number in a list

def smallest(list):
    small = list[0]
    for i in list:
        if i < small:
            small = i 
    return small
list = [20,3,45,1]
print(smallest(list))


#13-largest number in a list

def largest(list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max
list = [12,7,8,2,10,20]
print(largest(list))


#14-program to find second largest number in a list

list = [10,30,40,7,5]
n = len(list)
firstmax = max(list[0],list[1])
secondmax = min(list[0],list[1])
for i in range(2,n):
    if list[i]> firstmax:
        secondmax = firstmax
        firstmax = list[i]
    elif list[i]>secondmax and firstmax != list[i]:
        secondmax = list[i]
    else:
        if secondmax == firstmax:
            secondmax = list[i]
print(secondmax)

#method-2
def second_largest(lst):
    n = len(list)
    for i in range(0,n):

        for j in range(0,n-i-1):
            if list[j] > list[j+1]:
                list[j],list[j+1] = list[j+1],list[j]
    return list[-2]

list = [2,1,4,3,5,6,10]
print(second_largest(list))


#15-N largest element in the list

def N_largest(list,n):
    new_list=[]
    
    for i in range(0,n):
        max = list[0]
        for j in range(len(list)):
            if list[j] > max:
                max = list[j]
        list.remove(max)
        new_list.append(max)
    print(new_list)
list = [10,2,3,8,6,11]
n=2
print(N_largest(list,n))


#16-even

def even(list):
    for i in list:
        if i % 2 == 0:
            print(i)
list=[1,2,3,4,5,6,7,8,9,10]
even(list)


#17-odd

def odd(list):
    for i in list:
        if i % 2 != 0:
            print(i)
list=[1,2,3,4,5,6,7,8,9,10]
odd(list)


#18-even numbers range:

def even_range(list,n1,n2):
    for i in range(n1,n2):
        if i % 2 == 0:
            print(i)
list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(even_range(list,5,15))


#19-odd numbers range

def odd_range(list,n1,n2):
    for i in range(n1,n2):
        if i % 2 != 0:
            print(i)
list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(odd_range(list,5,15))


#20-count of odd and even numbers in list

def count(list):
    count1 = 0
    count2 = 0
    for i in list:
        if i % 2 ==0:
            count1+=1
        elif i % 2 !=0:
            count2+=1
    print("even numbers count in list:",count1)
    print("odd numbers count in list:",count2)
list = [1,2,3,4,5,6,7,8,9]
print(count(list))


#21-positive numbers in list:

def positive(list):
    for i in list:
        if i > 0:
            print(i)
list=[-1,-2,1,-3,4,5]
print(positive(list))


#22-negative numbers in list:

def negative(list):
    for i in list:
        if i < 0:
            print(i)
list=[-1,-2,1,-3,4,5]
print(negative(list))


#23-range of positive numbers

def positive_range(list,n1,n2):
    for i in range(n1,n2):
        if i > 0:
            print(i)
list = [1,-1,2,-2,3,-3,4,-4,5,-5]
print(positive_range(list,1,5))


#24-range of negative numbers

def negative_range(n1,n2):
    for i in range(n1,n2):
        if i < 0:
            print(i)
print(negative_range(-5,-1))


#25-count of positive and negative numbers

def count(list):
    count1 = 0
    count2 = 0
    for i in list:
        if i > 0:
            count1+=1
        elif i < 0:
            count2+=1
    print("positive numbers count in list:",count1)
    print("negative numbers count in list:",count2)
list = [1,-2,3,-4,5,-6,-7,8,-9]
print(count(list))



#26- remove multipe elements from list

def remove_multiples(list):
    for i in list:
        if i % 2 == 0:
            list.remove(i)
    return list
list=[11,5,17,18,23,50]
print(remove_multiples(list))


#27- Remove empty tuples from a list

def remove_empty(l):
    for t in l:
        if t:
            print(t)
l = [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
print(remove_empty(l))

#28 - remove duplicate integers from the list

list = [2,2,3,4,4,5,10,6,9]
print("The original list",list)

newlist = []
for i in list:
    if i not in newlist:
        newlist.append(i)
print("The list after removing the duplicates",(newlist))

#method-2

def remove_duplicates(list):
    for i in range(0,len(list)):
        for j in range(i+1,len(list)):
            if list[i] == list[j]:
                print(list[i])
list=[10, 20,10,20,4,5,6,7,-20,-20]
print(remove_duplicates(list))


#29-cumulative sum of list

def cummulative(list):
    count = 0
    for i in list:
        count = count + i
        print(count)
list=[10, 20, 30, 40, 50]
print(cummulative(list))


#30-divide n chunks

def divide_chunks(l, n): 
    for i in range(0,len(l),n):
        yield l[i:i + n] 
n = 5
l = ['geeks', 'for', 'geeks', 'like', 
           'geeky','nerdy', 'geek', 'love', 
               'questions','words', 'life'] 
print(list(divide_chunks(l, n)))  


#31-Sort the values of first list using second list

def sort(x,y):
    zipped = zip(y,x)
    z = [x for _, x in sorted(zipped)]
    return z
x = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
y = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]
print(sort(x,y))


#32-Summation after elements removal

original = [1, 3, 4, 6, 7, 6]
removed = [3,6]
count = 0
for i in original:
    if i not in removed:
        count+=i
print(count)


#33-Custom Index Range Summation


#34-Elements with Frequency equal K

list = [9,4,5,4,4,5,9,5]
k = 3
last = []
for i in list:
    freq = list.count(i)
    if freq == k and i not in last:
        last.append(i)
print("k is:",last) 


#35-Check for Descending Sorted List

list = [10, 8, 4, 3, 1] 
flag = 0
i =1
while i < len(list):
    if list[i] > list[i-1]:
        flag = 1
    i+=1
if (not flag):
    print("yes,list is reversed sorted")
else:
    print("no,list is not reversed sorted")


#36-Concatenate Kth element in Tuple List

test_list = [(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]

k =1
res = " ".join([lis[k] for lis in test_list])
print("kth tuple:",res)


#37-iterate the triplet


#38-Convert Alternate String Character to Integer

list = ['1', '4', '3', '6', '7','8'] 

for i in range(0,len(list)):
        list[i] = int(list[i])
print("modified list is:" + str(list))


#39-False values Frequency

list = [3, False, False, 6, False, 9]
for i in list:
    if not i:
        res=sum(1 for i in  list if not i)
print(res)


#40-Element indices Summation

list = [1, 3, 3, 3, 6, 7]
don = [i for i in range(len(list)) if list[i]== 3]
res = sum(don)
print(res)


##41-Count % K elements

list= [3, 5, 1, 6, 7, 9]
k = 3
res = sum(1 for i in list if i % k != 0)
print(res)


#42-Descending Sort String Numbers

list = [ '4', '6', '7', '2', '1'] 
for i in range(0,len(list)):
    list[i] = int(list[i])
list.sort(reverse = True) 
print("descending order:" + str(list))


#43-Odd elements removal in List

list=[1,2,3,4,5]
res=[]
for i in list:
    if not i % 2 !=0:
        res.append(i)
print(res)


#44-Words lengths in String

string1 = "Geeksforgeeks is best Computer Science Portal"
res= list(map(len,string1.split()))
print(string1)
print(str(res))


#45-Odd elements indices

list = [5, 6, 10, 4, 7, 1, 19,21]
res=[]
for index,i in enumerate(list):
    if i % 2 != 0:
        res.append(index)
print(res)


#46-Random Numbers Summation

import random

res = sum([random.randrange(1,50,1) for i in range(7)])
print(res)


#47-Reverse Sort Row Matrix integration

#48-Column Average in Record List

test_list = [(1, 6), (3, 4), (5, 8)] 
res = []
temp = sum(i[0] for i in test_list),sum(i[1] for i in test_list)
for j in temp:
    res.append( j / len(test_list))
print(res)

#49-Reverse Order Sort in String List

list = ['gfg', 'is', 'good'] 
for i in list:
    res = [''.join(sorted(i, reverse = True)) for ele in list]  

    # res  = "".join(sorted(i, reverse = True))
print(res)


#50-Common Row elements Summation


              
