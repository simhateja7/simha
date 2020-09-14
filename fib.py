def fib(n):
    a=0
    b=1
    print("fibonaccis series of first",n,"numbers is:")
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)
n=int(input("enter upto which number you want fibonacci series:"))
if n<=0:
    print("please enter a number greater than zero!")

elif n==1:
    print("fibonacci series upto",n,"is",n)
else:
    fib(n)
    
    
    


