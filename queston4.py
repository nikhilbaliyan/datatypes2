set1=set()
name1=input("Enter  1st elements in set")
set1.add(name1)
name2=input("Enter 2nd elemtent in set")
set1.add(name2)
name3=input("Enter 3rd elemtent in set")
set1.add(name3)
name4=input('enter the 4th element in set')
set1.add(name4)
print("The set is",set1)

set2=set()
name1=input("Enter  1st elements in set")
set2.add(name1)
name2=input("Enter 2nd elemtent in set")
set2.add(name2)

print("The set is",set2)

'''this is q1'''
print(set1 - set2)

'''this is q3'''
print(set1 & set2)

'''this is q2'''

print(set1.issubset(set2))

print(set2.issubset(set1))

print(set1.issuperset(set2))