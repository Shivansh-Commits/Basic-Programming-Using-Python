#Q) If the first alphabet of the string is repeated anywhere in the sting again, replace it with '$'
a=input("Enter a string: ")
l=len(a)
c=0
for i in range(l):
    if(a[i]==a[0]):
        if(c==0):
            print(a[i],end="")
            c=1
            continue
        if(c==1):
            print("$",end="") 
    else:
        print(a[i],end="")
    