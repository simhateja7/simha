a=int(input("enter the first number in a list:"))
b=int(input("enter the second number in a list:"))
c=int(input("enter the third number in a list:"))
d=int(input("enter the fourth number in a list:"))
e=int(input("enter the fifth number in a list:"))
l1=list((a,b,c,d,e))
print("list1 is ")
print(l1)
print("number which are greater than 1 in list 1 is:")

for i in l1:
    if i>1:
        print(i,end=',')



print('\nenter numbers that you want to be in the list:')
n1=int(input())
n2=int(input())
n3=int(input())
n4=int(input())
l2=list((n1,n2,n3,n4))
print("list2 is")
print(l2)
print("number which are greater than 1 in list 2 is:")

b=[]
for a in l2:
    if a>1:
        b.append(a)


print(b)
