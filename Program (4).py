#Q) Print the no. of ALphabets and Digits in the iputed String
a=input("Enter a String of No. and Alphabets :")
d=0
c=0
for i in a:
    if(i.isdigit()):
        d=d+1
    if(i.isalpha()):
        c=c+1
        
print(d,"Digits")
print(c,"Alphabets")        
