#Q) Print the following pattern
# 1 

# 2 4

# 3 6 9 

# 4 8 12 16 

# 5 10 15 20 25

for i in range(1,6):
    sum=i
    c=i
    for j in range(5):
        if(c!=0):
            print(sum,end=" ")
            sum=sum+i
            c=c-1
    print("\n")