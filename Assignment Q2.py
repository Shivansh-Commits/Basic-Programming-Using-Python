#Q) Take input from user and print the string in reverse order
a=input("Enter a word: ")
l=len(a)-1
for i in range(l+1):
    print(a[l],end="")
    l=l-1