#Q) Print 'Hello' if the no. is only divisible by 3
#Print 'Python' if the no. is only divisible by 5
#print 'Hello Python' if the no. is divisible by both 3&5
for i in range(1,51):
    if(i%3==0 and i%5==0):
        print("Hello Python")
    elif(i%3==0):
        print("Hello")
    elif(i%5==0):
        print("Python")
    else:
        print(i)