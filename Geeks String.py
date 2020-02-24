#1-program to check if a string is palindrome or not

def is_palindrome(s):
    rev = s.casefold()
    rev = "".join(reversed(s))
    if rev == s:
        print("string is reversed",s)
    else:
        print("not reversed")
s="Mam"
print(is_palindrome(s))

#method-2

def reverse(s):
    return s[::-1]

def palindrome(s):

    rev = reverse(s)

    if s == rev:
        return True
    return False
s = "malayalam"
ans = palindrome(s)
if ans == 1:
    print("yes")
else:
    print("no")


#2-Reverse words in a given String in Python

def reverse(input):

    ip = input.split()

    ip = ip[-1::-1]

    # op = "".join(ip)

    return ip

input = "geeks quiz practice code"
print(reverse(input))



#3-remove i’th character from string

ip = "Sachin10Tendulkar"

print("The original string is "+ ip)

new = ""

for i in range(0,len(ip)):
    if i != 6 and i != 7:
        new = new  + ip[i]
print("The string after removal of ith character is " + new)


#4-Check if a Substring is Present in a Given String

def check_substring(s1,s2):
    if s1.find(s2) == -1:
        print("no")
    else:
        print("yes")
s1="SachinTendulkar"
s2="Sachin"
print(check_substring(s1,s2))


#5-Find length of a string in python


def size(s):
    count = 0
    for i in s:
        count+=1
    print(count)
s="sachin"
print(size(s))


#6- program to print even length words in a string

def words(s):
    s = s.split()
    for i in s:
        if len(i) % 2 == 0:
            print(i)
s= "master blaster sachin"
print(words(s))


#7-Program to accept the strings which contains all vowels

def vowels(s):

    s=s.lower()

    vow = set("aeiou")

    vowe = set({})

    for i in s:
        if i in vow:
            vowe.add(i)
        else:
            pass
    if len(vowe) == len(vow):
        print("accepted")
    else:
        print("not accepted")
s = "SEEquoiaL"
print(vowels(s))


#8- Count the Number of matching characters in a pair of string

def matching(s1,s2):
    count = 0
    for i in s1:
        if s2.find(i) >=0:
            count+=1
    print("matched char are",count)
s1 = 'abcdef'
s2 = 'defghia'
print(matching(s1,s2))


#9-program to count number of vowels using sets in given string

def counting(s):
    vow = set("aeiouAEIOU")
    char = []
    count = 0
    for i in s:
        if i in vow:
            count +=1
            char.append(i)
    print(f"matching vowels are {char} and count is {count}")
s="pandian"
print(counting(s))


#10-Remove all duplicates from a given string

a="pandian"
s=""
for i in a:
    if i not in s:
        s = s + i
print(s)

#11-Program to check if a string contains any special character

import re
def check(s):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

    if regex.search(s) == None:
        print("string is accepted")
    else:
        print("string is not acepted")
s="Geeks$For$Geeks"
print(check(s))


#12-Generating random strings until a given string is generated

import random
import string

#13-Find words which are greater than given length k

def k(s,l):
    s= s.split()
    f=[]
    for i in s:
        if len(i) > l:
            f.append(i)
    return f
s="hello geeks for geeks is computer science portal"
l = 4
print(k(s,l))


#14-program for removing i-th character from a string

def removal(s,i):
    a = s[:i]
    b = s[i+1:]
    return a+b
s="geeks"
i=2
print(removal(s,i))


#15-program to split and join a string

def split(s):
    sem = s.split(" ")
    sam = "-".join(sem)
    return sem,sam
s="Geeks for Geeks"
print(split(s))


#16-Check if a given string is binary string or not

def binary(s):
    t = "01"
    co = 0
    for i in s:
        if i not in t:
            co = 1
            break
        else:
            pass
    if co:
        print("no")
    else:
        print("yes")
s="10101201"
print(binary(s))


#17-Find all close matches of input string from a list

from difflib import get_close_matches

def close_matches(pattens,word):
    print(get_close_matches(word,pattens))
pattens = ['ape', 'apple', 'peach', 'puppy'] 
word = 'appel'
print(close_matches(pattens, word))


#18-program to find uncommon words from two Strings

def uncommon(A,B):
    count = {}

    for i in A.split():
        count[i] = count.get(i,0)+1
    for i in B.split():
        count[i] = count.get(i,0)+1
    return [i for i in count if count[i] == 1]
A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"
print(uncommon(A,B))


#19-Swap commas and dots in a String

def replace(s):
    str1 = s.replace(',','.')
    str1 = s.replace('.',',')
    return str1
s = "14, 625, 498.002"
print(replace(s))


#20-Permutation of a given string using inbuilt function

from itertools import permutations

def allpermutations(str):
    permlist = permutations(str)
    for i in list(permlist):
        print(''.join(i))
str="ABC"
print(allpermutations(str))


#21-Check for URL in a String

import re
def find(str):
    url =  re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+] [!*\(\), ]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str)
    return url
str = 'My Profile: https://auth.geeksforgeeks.org / user / Chinmoy % 20Lenka / articles in the portal of http://www.geeksforgeeks.org/'
print("urls:",find(str))  


#22-Execute a String of Code in Python

def exec_code(): 
    LOC = """ 
def factorial(num): 
    fact=1 
    for i in range(1,num+1): 
        fact = fact*i 
    return fact 
print(factorial(5)) 
"""
    exec(LOC)  
exec_code() 


#23-String slicing in Python to rotate a string

def rotate(ip,d): 
    # slice string in two parts for left and right 
    Lfirst = ip[0 : d] 
    Lsecond = ip[d :] 
    Rfirst = ip[0 : len(ip)-d] 
    Rsecond = ip[len(ip)-d : ] 
  
    # now concatenate two parts together 
    print("Left Rotation : " , (Lsecond + Lfirst)) 
    print("Right Rotation : " , (Rsecond + Rfirst))
ip = 'GeeksforGeeks'
d=2
print(rotate(ip,d))


##24-

##25-Find all duplicate characters in string

a="geeksforgeeks"
s=""
for i in a:
    if i not in s:
        s = s + i
print(s)

