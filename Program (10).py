#Q) Find all prime nos. from 1 to 30
c=0
for i in range(2,30):
    for j in range(2,(i//2)+1):
        if(i%j==0):
            c+=1
    if(c==0):
        print(i,"is a Prime Number")
    c=0
