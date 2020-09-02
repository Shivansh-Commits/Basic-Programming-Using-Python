#                                             SETS




#Declaration of set
#set1=set()
#print(set)

#s1={1,2,3,4,5} we can also use curly brackets
#print(s1)

#s1=([1,2,3,4,5])
#print(type(s1))  this is a list

#s1=({1,2,3,4,5}) this is a set
#print(type(s1))



#Ques)adding elements to set
#s1=({1,3,4,5})
#s1.add(0)
#print(s1)


#Ques) Update values into set
#s1=({1,2,3,4,5})
#s1.update([6,7,8,9])
#print(s1)


#Ques)Remove element from set
#s1=({1,2,3,4,5})
#s1.remove(2)
#print(s1)
#Here if the element is not present in the set then, compiler gives error

#OR

#s1=({1,2,3,4,5})
#s1.discard(3)
#print(s1)
#here compiler will not give error if the element is not present in the set


#Ques)POping elemets of the set
#s1=({1,2,3,4})
#s1.pop()
#print(s1)


#Ques)UNION Operation
#s1=({1,2,3,4})
#s2=({5,6,7,8})
#s3=s1|s2  or s3=s1.union(s2)
#print(s3)


#Ques)INTERSECTION Opertion
#s1=({1,2,3,4})
#s2=({3,4,5,6,7})
#s3=s1&s2  or s3=s1.intersection(s2)
#print(s3)




#Ques)Find the set diference
#s1=({1,2,3,4,5})
#s2=({1,2})
#s3=s1.difference(s2)
#print(s3)



#Ques)Using clear function
#s1=({1,2,3,4,5})
#s1.clear()
#print(s1)


