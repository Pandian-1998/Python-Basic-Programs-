#program-1

n=int(input("enter the number: "))
for i in range(1,n+1):
    print(n * "*")

program-2

n = int(input("> "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end="")
    print()

program-3

n = int(input("> "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end="")
    print()

program-4

n = int(input("> "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(64+i),end="")
    print()

program-5

n = int(input("> "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(64+j),end="")
    print()


program-6
n = int(input("> "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(n+1-i,end = "")
    print()

program-7
n = int(input("> "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(n+1-j,end = "")
    print()

program-8
n = int(input("> "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(65+n-i),end = "")
    print()


program-9

n = int(input("> "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(65+n-j),end = "")
    print()


program-10

n = int(input(" > "))
for i in range(1,n+1):
    print(i*"*")

program-11

n = int(input("> "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end = "")
    print()

program-12

n = int(input("> "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end = "")
    print()

program-13


n = int(input("> "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+i),end = "")
    print()


program-14

n = int(input("> "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+j),end = "")
    print()

program-15

n = int(input("> "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print("*",end="")
    print()

program-16

n = int(input("> "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(i,end="")
    print()

program-17

n = int(input("> "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(j,end="")
    print()

program-18

n = int(input("> "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(chr(64+i),end="")
    print()

program-19

n = int(input("> "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(chr(64+j),end="")
    print()

program-20

n = int(input("> "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(n+1-i,end="")
    print()

program-21

n = int(input("> "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(n+1-j,end="")
    print()

program-22

n = int(input("> "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(chr(64+n+1-i),end="")
    print()

program-23

n = int(input("> "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(chr(64+n+1-j),end="")
    print()

program-24

n=int(input("enter the input:"))
for i in range(n):
    print(" "*(n-i-1)+"* "*(i+1))

program-25

n = int(input("enter the input:"))
for i in range(1,n+1):
    print(" " * (n-i),end="")
    for j in range(1,i+1):
        print("*",end=' ')
    print()

program-26

n=int(input("enter the input:"))
for i in range(n):
    print(" "*(n-i-1)+(str(i+1)+' ')*(i+1))


program-27

n=int(input("enter the input:"))
for i in range(n):
    print(" "*(n-i-1),end=" ")
    for j in range(i+1):
        print(j+1,end = " ")
    print()


program-28

n=int(input("enter the input:"))
for i in range(n):
    print(" "*(n-i-1)+(chr(64+i)+' ')*(i+1))

program-29

n=int(input("enter the input:"))
for i in range(n):
    print(" "*(n-i-1),end=" ")
    for j in range(i+1):
        print(chr(64+j+1),end = " ")
    print()


program-30

n = int(input(" > "))
for i in range(1,n+1):
    print("  "*(i-1),"* "*(n+1-i))

program-31

n = int(input("> "))
for i in range(1,n+1):
    print("  "*(i-1),(str(n-i+1)+" ")*(n-i+1))

program-32

n = int(input("> "))
for i in range(1,n+1):
    print("  "*(i-1),end="")
    for j in range(1,n+2-i):
        print(j,end=" ")
    print()

program-33

n = int(input(" > "))
for i in range(1,n+1):
    print("  "*(i-1),(str(chr(65+n-i))+" ")*(n-i+1))

program-34

n=int(input(" >"))
for i in range(1,n+1):
    print("  "*(i-1),end='')
    for j in range(1,n+2-i):
        print(chr(64+j),end=" ")
    print()

program-35

n = int(input(" > "))
for i in range(1,n+1):
    print("  "*(n-i),"* "*(2*i-1))

program-36

n=int(input("> "))
for i in range(1,n+1):
    print("  "*(n-i),(str(i)+" ")*(2*i-1))

program-37

n=int(input("> "))
for i in range(1,n+1):
    print("  "*(n-i),(str(chr(64+i)+" "))*(2*i-1))

program-38

n=int(input("> "))
for i in range(1,n+1):
    print("  "*(n-i),(str(chr(64+2*i-1)+" "))*(2*i-1))

program-39

n=int(input("> "))
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(1,2*i):
        print(j,end=" ")
    print()

program-40

n=int(input("> "))
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(2*i-1,0,-1):
        print(j,end=" ")
    print()



program-41

n=int(input("> "))
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(1,2*i):
        print(chr(64+j),end=" ")
    print()


program-42

n=int(input("> "))
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(2*i-1,0,-1):
        print(chr(64+j),end=" ")
    print()

program-43

n=int(input("> "))
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(1,i):
        print(i-j,end=" ")
    for k in range(0,i):
        print(k,end=" ")
    print()


program-44

n = int(input(" > "))
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(1,i):
        print(chr(i-j+65),end=" ")
    for k in range(0,i):
        print(chr(k+65),end=" ")
    print()


program-45

n = int(input("> "))
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end=" ")
    for k in range(i-1,0,-1):
        print(k,end=" ")
    print()

program-46

n=int(input("> "))
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    for k in range(1,i):
        print(chr(64+k),end=" ")
    print()


program-47

n=int(input("> "))
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(1,i+1):
        print(n+1-j,end="  ")
    print()

program-48

n=int(input("> "))
for i in range(n):
    print("  "*i+"*   "*(n-i))



program-49
n = int(input("> "))
for i in range(1,n+1):
    print("  "*i,end="")
    for j in range(0,n+1-i):
        print(n+1-i,end=" ")
    for k in range(1,n+1-i):
        print(n+1-i,end=" ")
    print()


program-50

n= int(input("> "))
for i in range(1,n+1):
    print("  "*i,end="")
    for j in range(0,n+1-i):
        print(2*n+1-2 *i,end=" ")
    for k in range(1,n+1-i):
        print(2*n+1-2*i,end=" ")
    print()




program-51

n = int(input("> "))
for i in range(1,n+1):
    print("  "*(i-1),end="")
    for j in range(1,n+2-i):
        print(j,end=" ")
    for k in range(2,n+2-i):
        print(n+k-i,end=" ")
    print()

program-52

n=int(input("> "))
for i in range(1,n+1):
    print("  "*(i),end="")
    for j in range(1,n+2-i):
        print(chr(65+n-i),end=" ")
    for k in range(2,n+2-i):
        print(chr(65+n-i),end=" ")
    print()


program-53

n=int(input("> "))
for i in range(1,n+1):
    print("  "*i,end="")
    for j in range(1,n+2-i):
        print(chr(65+2*n-2*i),end=" ")
    for k in range(2,n+2-i):
        print(chr(65+2*n-2*i),end=" ")
    print()


program-54

n = int(input("> "))
for i in range(1,n+1):
    print("  "*i,end="")
    for j in range(1,n+2-i):
        print(chr(64+j),end=" ")
    for k in range(2,n+2-i):
        print()

program-55

n = int(input("> "))
for i in range(n):
    print("  "*(n-i-1),end="")
    for j in range(i+1):
        print(j+1,end="   ")
    print()
for i in range(n-1):
    print("  "*(i+1),end="")
    for j in range(n-i-1):
        print(j+1,end="   ")
    print()



program-56

n=int(input("> "))
for i in range(n):
    print("  "*(n-i-1)+"*   "*(i+1))
for i in range(n-1):
    print("  "*(i+1)+"*   "*(n-i-1))

program-57

n=int(input("> "))
for i in range(n):
    print("  "*(n-i),end="")
    for j in range(i+1):
        print(n-j,end="   ")
    print()
for i in range(n-1):
    print("  "*(i+2),end="")
    for j in range(n-i-1):
        print(n-j,end="   ")
    print()


program-58

n = int(input("> "))
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(0,i):
        print(n+j-i,end="  ")
    print()
for k in range(1,n):
    print("  "*(k),end="")
    for l in range(1,n+1-k):
        print(l+k-1,end="  ")
    print()


program-59

n = int(input("> "))
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(0,i):
        print(chr(65+n+j-i),end="  ")
    print()
for k in range(1,n):
    print("  "*(k),end="")
    for l in range(1,n+1-k):
        print(chr(65+l+k-1),end="  ")
    print()

program-60

n = int(input("> "))
for i in range(1,n+1):
    print("* "*(i))
for j in range(1,n):
    print("* "*(n-j))


program-61

n=int(input("> "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(n-j,end=" ")
    print()
for k in range(1,n):
    for l in range(1,n+1-k):
        print(n-l,end=" ")
    print()

program-62

n=int(input("> "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(n-i+j-1,end=" ")
    print()
for k in range(1,n+1):
    for l in range(0,n-k):
        print(l+k,end = " ")
    print()

program-63

n = int(input("> "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(65+n-i),end=" ")
    print()
for k in range(1,n+1):
    for l in range(0,n-k):
        print(chr(65+k),end=" ")
    print()


program-64

n = int(input("> "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(65+n-j),end=" ")
    print()
for k in range(1,n+1):
    for l in range(n-k,0,-1):
        print(chr(65+l+k),end=" ")
    print()

program-65

n=int(input("> "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+n-i+j),end=" ")
    print()
for k in range(1,n+1):
    for l in range(1,n-k+1):
        print(chr(64+l+k),end=" ")
    print()

program-66

n =int(input("> "))
for i in range(1,n+1):
    print("  "*(n-i)+"*  "*(i))


program-67

n = int(input("> "))
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(1,i+1):
        print(i,end="  ")
    print()

program-68

n = int(input("> "))
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end="  ")
    print()

program-69

n = int(input("> "))
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(1,i+1):
        print(chr(64+i),end="  ")
    print()

program-70

n = int(input("> "))
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(1,i+1):
        print(chr(64+j),end="  ")
    print()


program-71

n = int(input("> "))
for i in range(1,n+1):
    print("  "*(i)+"*  "*(n-i+1))

program-72

n = int(input("> "))
for i in range(1,n+1):
    print("  "*(i),end="")
    for j in range(1,n-i+2):
        print(n-i+1,end="  ")
    print()

program-73

n = int(input("> "))
for i in range(1,n+1):
    print("  "*(i),end="")
    for j in range(1,n-i+2):
        print(n+2-i-j,end="  ")
    print()

program-74

n = int(input("> "))
for i in range(1,n+1):
    print("  "*(i),end="")
    for j in range(1,n+2-i):
        print(chr(65+n-i),end="  ")
    print()



program-75

n = int(input("> "))
for i in range(1,n+1):
    print("  "*(i),end="")
    for j in range(1,n+2-i):
        print(chr(65+n+1-i-j),end="  ")
    print()



program-76

n = int(input("> "))
for i in range(1,n+1):
    print("  "*(i),end="")
    for j in range(1,n-i+2):
        print(chr(64+j),end="  ")
    print()


program-77

n = int(input("> "))
for i in range(1,n+1):
    print("  "*(n-i)+"*  "*(i))
print()
for j in range(1,n):
    print("  "*(j)+"*  "*(n-j))
print()

program-78

n = int(input("> "))
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(1,i+1):
        print(i,end="  ")
    print()
for k in range(1,n):
    print("  "*(k),end="")
    for l in range(1,n+1-k):
        print(n-k,end="  ")
    print()


program-79

n = int(input("> "))
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end="  ")
    print()
for k in range(1,n):
    print("  "*(k),end="")
    for l in range(1,n-k+1):
        print(l+k,end="  ")
    print()


program-80

n = int(input("> "))
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end="  ")
    print()
for k in range(1,n):
    print("  "*(k),end="")
    for l in range(1,n-k+1):
        print(l,end="  ")
    print()

program-81

n=int(input("> "))
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(1,i+1):
        print(chr(64+i),end="  ")
    print()
for k in range(1,n):
    print("  "*(k),end="")
    for l in range(1,n-k+1):
        print(chr(64+n-k),end="  ")
    print()

program-82

n=int(input("> "))
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(1,i+1):
        print(chr(64+j),end="  ")
    print()
for k in range(1,n):
    print("  "*(k),end="")
    for l in range(1,n-k+1):
        print(chr(64+l+k),end="  ")
    print()


program-83

n = int(input("> "))
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(1,i+1):
        print(n-i+j,end="  ")
    for k in range(2,i+1):
        print(n+1-k,end="  ")
    print()
for a in range(1,n):
    print("  "*(a),end="")
    for b in range(1+a,n+1):
        print(j,end="  ")
    for c in range(2,n+1-a):
        print(n+1-c,end="  ")
    print()


program-84

n = int(input("> "))
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(1,i+1):
        print(n+1-j,end="  ")
    for k in range(2,i+1):
        print(n-i+k,end="  ")
    print()
for a in range(1,n):
    print("  "*(a),end="")
    for b in range(1,n+1-a):
        print(n+1-b,end="  ")
    for c in range(2,n+1-a):
        print(a+c,end="  ")
    print()

program-85

n=int(input("> "))
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(i,i+1):
        print("* ",end="  ")
        if i>=1:
            print("  "*(2*i-4),end="")
        for k in range(i,i+1):
            print("* ",end="  ")
        print()
    

program-86

n=int(input("> "))
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(i,i+1):
        print(i ,end="  ")
        if i>=1:
            print("  "*(2*i-4),end="")
        for k in range(i,i+1):
            print(k,end="  ")
        print()
    

program-87

n=int(input("> "))
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(i,i+1):
        print(n+1-i ,end="  ")
        if i>=1:
            print("  "*(2*i-4),end="")
        for k in range(i,i+1):
            print(n+1-i,end="  ")
        print()


program-88


n=int(input("> "))
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(i,i+1):
        print(chr(64+n+1-i) ,end="  ")
        if i>=1:
            print("  "*(2*i-4),end="")
        for k in range(i,i+1):
            print(chr(64+n+1-i),end="  ")
        print()


program-89


n=int(input("> "))
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(i,i+1):
        print(chr(64+i) ,end="  ")
        if i>=1:
            print("  "*(2*i-4),end="")
        for k in range(i,i+1):
            print(chr(64+i),end="  ")
        print()


program-90

n = int(input("> "))
for i in range(1,n+1):
    print("  "*(i-1),end="")
    for j in range(i,i+1):
        print("*",end="  ")
        if i<=4:
            print("  "*(2*n-2*i-2),end="")
            for k in range(i,i+1):
                print("*",end="  ")
            print()

program-91

n = int(input("> "))
for i in range(1,n+1):
    print("  "*(i-1),end="")
    for j in range(i,i+1):
        print(i,end="  ")
        if i<=4:
            print("  "*(2*n-2*i-2),end="")
            for k in range(i,i+1):
                print(i,end="  ")
            print()

program-92

n = int(input("> "))
for i in range(1,n+1):
    print("  "*(i-1),end="")
    for j in range(i,i+1):
        print(n-i+1,end="  ")
        if i<=4:
            print("  "*(2*n-2*i-2),end="")
            for k in range(i,i+1):
                print(n-i+1,end="  ")
            print()

program-93

n = int(input("> "))
for i in range(1,n+1):
    print("  "*(i-1),end="")
    for j in range(i,i+1):
        print(chr(64+n-i+1),end="  ")
        if i<=4:
            print("  "*(2*n-2*i-2),end="")
            for k in range(i,i+1):
                print(chr(64+n-i+1),end="  ")
            print()


program-94


n = int(input("> "))
for i in range(1,n+1):
    print("  "*(i-1),end="")
    for j in range(i,i+1):
        print(chr(64+i),end="  ")
        if i<=4:
            print("  "*(2*n-2*i-2),end="")
            for k in range(i,i+1):
                print(chr(64+i),end="  ")
            print()
program-95

n=int(input("> "))
for i in range(1,n+1):
    print("  "*(i+1),end="")
    for j in range(1,n+1):
        print("*",end=" ")
    print()


program-96

n=int(input("> "))
for i in range(1,n+1):
    print("  "*(n-i),end="")
    for j in range(1,i+1):
        print("*",end="  ")
    print("  "*(n-i),end="")
    for k in range(1,i+1):
        print("*",end="  ")
    print()



program-97

n = int(input("> "))
for i in range(1,n+1):
    for j in range(1,i+1):
        if (i  % 2 !=0 and j % 2 !=0)or(i % 2==0 and j % 2 == 0):
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()

program-98

n = int(input("> "))
for i in range(1,n+1):
    print("  "*(2*n-i+3),end="")
    for j in range(1,i+1):
        print("*",end="  ")
    print()
for i in range(1,n+3):
    print("  "*(2*n-i+1),end="")
    for j in range(-1,i+1):
        print("*",end="  ")
    print()
for i in range(1,n+5):
    print("  "*(2*n-i),end="")
    for j in range(-2,i+1):
        print("*",end="  ")
    print()
for i in range(1,n+3):
    print("  "*((2*n)),end="")
    print("* "*3)



program-99

n = int(input("> "))
for i in range(1,n+1):
    print(" "*(2*n-i),end="")
    for j in range(1,i+1):
        print("*",end="  ")
    print()
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print("*",end="  ")
    print(" "*(n-i),end="")
    for k in range(1,i+1):
        print("*",end="  ")
    print()





program-100

n = int(input("> "))
for i in range(1,2*n+1):
    if i % 2 == 0:
        print("*"*i,end="")
    else:
        print("*"*(i+1),end=" ")
    print()



program-101

n=int(input("Enter a number:"))
for a in range(1,n+1,2):
    for i in range(1,n+1):
        print(" "*(2*n-i-a),end="")
        for j in range(1,i+a):
            print("*",end=" ")
        print()
for b in range(1,n+1):
    print(" "*(n-2),end="")
    print("* "*3)




























































