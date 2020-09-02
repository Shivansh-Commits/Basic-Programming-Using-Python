""" #defination of function
def display():
    print("Hello")
    print("THIS IS A TEST")

display()   
"""
  
"""   
def pallindom(a,b):
    for i in range(b//2+1):
        if(a[i]!=a[b]):
            print("Not pallindrome")
            return 0
        else:
            b=b-1
            continue      
    return 1
a=input("enter a string")  
b=len(a)-1  
flag=pallindom(a,b)

if flag==1 :
    print("Yes it Pallindrom")
"""