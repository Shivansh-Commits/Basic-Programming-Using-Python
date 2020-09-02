
#import re 
#fhand= open('mbox.txt')
#for line in fhand:
#    line = line.rstrip()
#    if re.search('^X.\S+',line):
#        print(line)
        
        


#Finding Vowels in a string
#import re 
#x='My 2 favorite numbers are 19 and 42'
#y=re.findall('[a,e,i,o,u]+',x)
#print(y)




#GREEDY APPROACH
#import re
#x='From : Using the : character'
#y=re.findall('^F.+:',x)
#print(y)


#NON-GREEDY APPROACH
#import re
#x='From : Using the : character'
#y=re.findall('^F.+?:',x)
#print(y)
        


#Extract email-id from string:
#import re
#x='From stephen.marquad@uct.ac.za' 
#y=re.findall('\S+@\S+',x)
#print(y)



#Extract All email-ids from mbox .txt:
#import re
#fhand = open('mbox.txt')
#for line in fhand:
#    y=re.findall('^From (\S+@\S+)',line)
#    if len(y)!=0:
#        print(y)
#    


#Extract numbers written in front of X-DSPAM-Confidence in the file 
#import re
#fhand = open('mbox-short.txt')
#for line in fhand:
#    y=re.findall('^X\S*: ([0-9.]+)',line)
#    if len(y)>0:
#        print(y)

    

#FInd Domain names from a file:
#import re
#fhand=open('mbox-short.txt')
#for line in fhand:
#    y=re.findall('@([^ ]*)',line)
#    if len(y)>0:
#        print(y)




#Find max among the extracted no.
#import re
#l=list()
#fhand = open('mbox-short.txt')
#for line in fhand:
#    y=re.findall('^X\S*: ([0-9.]+)',line)
#    if(len(y)>0):
#        l.append(y)
#        print(y)
#print(max(l))
#fhand.close()
#
#l2=list()   
#for i in l:
#    for j in i:
#        l2.append(j)
#print(max(l2),min(l2))





#Find numeric values written in front of New Revision:
#import re
#l=list()
#l2=list()
#fhand = open('mbox-short.txt')
#for line in fhand:
#    y=re.findall('^New Revision: ([0-9.]\S+)',line)
#    if len(y)>0:
#        l.append(y)
#for i in l:
#    for j in i:
#        l2.append(int(j))
#print(l2)    

#avg=0
#sum=0
#for i in l2:
#    sum=sum+i
 
#avg=sum/len(l2)
#print()
#print('average: ',avg)
#print()
#print('sum:',sum)





#l=list()
#import re
#fhand = open('mbox.txt')
#for i in fhand:
#    y=re.findall('^From.+([0-9][0-9])',i)
#    if len(y)>0:
#        l.append(y)
#
#print(l)







    
    
    
    
