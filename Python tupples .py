#                               TUPPLES (tupples are immutable)

#Ways to declare tuple

#1)
#t=()
#print(type(t))
#2)
#t=(1,2,3,4,5)
#print(t)
#3)
#t=tuple('hello world')
#print(t)

#t=(1,) #if we put only one element in tupple , and do not put ending comma it becomes of int class.  So, to make it tupple we have to put ending comma
#print(type(t))


#Ques)inserting value into tupples 
#
#t=(1,2,3,4,5)
#t1=t[0:2]+(50,)+t[3:]
#print(t1)



#Inbuilt functions of tupple
#1)len()
#2)max()
#3)min()
#4)sum()
#5)index()
#6)count()




#Ques)Arrange words in descending order according to length
#l1=[]
#l2=[]
#line1='for about accurate while! is a'
#words=line1.split()
#for word in words:
#    l1.append((len(word),word))
#l1.sort(reverse=True)
#print(l1)
#
#for value,key in l1:
#    l2.append(key)
#print(l2)
#

