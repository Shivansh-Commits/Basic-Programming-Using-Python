#Q) If a word ends with 'ing' replace 'ing' with 'ly' else place 'ing' at the end of the word
x=input("Enter a string : ")
ch=x[-3::1]
l=len(x)
if(l>3):
    if(ch=="ing"):
        print(x[0:l-3]+"ly")
    else:
        print(x+"ing")
else:
    print(x)