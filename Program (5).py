#Q) Print the Digit '5'
c=0
k=1
for i in range(1,8):
    for j in range(1,8):

        if(i==1 or i==4 or i== 7 ):
            print("*",end="")
        else:
            if(i==2 or i==3 ):
                if(c==0):
                    print("*",end="")
                    c=1
            
            if(i==5 and j==7 or i==6 and j==7 ):
                print("*",end="")
            else:
                print(" ",end="")
    print()
    c=0
    k=1
