#Q) print the following pattern:
# *
# **
# ***
# ****
# *****
# ***
# **
# *
for i in range(1,10):
    c=i
    k=10
    for j in range(1,6):
        if(i<=5):
            if(c>0):
                print("*",end="")
                c=c-1
        if(i>5):
            if(k>i):
                print("*",end="")
            k=k-1
    print()