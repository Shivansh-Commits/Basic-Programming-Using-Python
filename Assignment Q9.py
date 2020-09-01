#Q)Print the no. of odd and even no.
a=[1,2,3,4,5,6,7,8]
e=0
o=0
for i in range(0,8):
    if(a[i]%2==0):
        e=e+1
    else:
        o=o+1
print(e,"Even no.s")
print(o,"Odd no.s")