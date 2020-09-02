#Dictonaries work as unordered list

#declaration of Dictonaries
#1):
#    d=dict()
#    print(d)
#2):
#    d={}
#    print(d)


#Ques)inserting values into dictonaries

#purse=dict()
#purse={'money' :12 ,'candy':3}#basic syntax = name={key:index,key:index}
#purse['tissues']=15 #separately inserting elements into dictonaries
#print(purse)


#Ques)Incrementing the Values of the index

#purse=dict()
#purse={'money' :12+10 ,'candy':3}#basic syntax = name={key:index,key:index}
#purse['tissues']=15 #separately inserting elements into dictonaries
#print(purse)


 
#Ques)Incrementing the values in Dictonaries
#l={'a':1,'b':2}
#l['a']=l['a']+10
#print(l)



#Ques)Printng the values of dictonary
#l={'a':1,'b':4}
#print(l['b'])



#Ques)Function of Extract all keys and values from dictonary in to a List
#l={'a':2,'b':5,'c':'hello'}
#l1=list(l.keys())
#l2=list(l.values())
#print(l1,l2)



#Ques)Store the items of dictonaries in a list
#l={'a':3,'b':5}
#l1=list(l.items())
#print(l1)#l1 is a tupple as it contains the items of dictonary comma seperated




#Ques)Find the Frequency of each Alphabet in the dictonary
#str='AAAPPLE'
#d=dict()
#for i in str:
#    if i not in d:
#        d[i]=1
#    else:
#        d[i]=d[i]+1
#
#print(d)




#Ques)Count the  frequency of Words in a String"a the the of of were were were hello"
#str=input("Enter a String: ")
#l1=list(str.split())
#d=dict()
#for i in l1:
#    if i not in d:
#        d[i]=1
#    else:
#        d[i]=d[i]+1
#        
#        
#for i in d:  #for finding items that have values more than 2
#    if d[i]>2:
#        print(i)





#Ques)Usign Get Function find frequency of values in dict
#
#Syntax of get() function -> d.get(a,b) here a is the key that we are searching for and b 
#is the default value that get function returns if the key is not availabe.if a is present
#then it will return the value of that key
#str='AAPPLE'
#d=dict()
#for i in str:
#    d[i]=d.get(i,0)+1
#print(d)





#Ques)Sort the keys of dictonary in decending order
#d={'b':1,'a':3,'c':5,'d':9}
#l1=list(d.keys())
#l1.sort()
#
#for i in l1:   
#    print(i,d[i])




#Ques)Delete an item from the dictonary
#d={'a':3,'f':1,'g':8}
#del d['a']
#print(d)




#Ques)Remove all items from the dictonary
#d={'a':9,'f':2,'s':8,'v':3}
#d.clear()
#print(d)




#Ques)Finding max Value of Dictonary
#d={'x':5,'w':9,'a':4,'c':1}
#l1=list(d.values())
#m=max(l1)
#for i in d:
#    if d[i]==m:
#        print(i,d[i])
#


#    """ALTERNATIVE"""


#d={'x':5,'w':9,'a':4,'c':1}
#bigword=None
#bigcount=None
#for word,count in d.items():
#    if bigcount is None or count > bigcount:
#        bigword=word
#        bigcount=count
#    
#print(bigcount , bigword)




#Ques)Nested Dictonary
#d={'Kohli':{'ODI':1500 , 'Test':1000},'Dhoni':{'ODI':14000 , 'Test':16000}}
#for a,b in d.items():
#    print(a)
#    for i,j in b.items():
#        print(i,j)
#    print()





























