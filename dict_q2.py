import operator
d1={}
key1=input('Enter the name')
value1=input('enter the marks')
d1[key1]=value1
key2=input('Enter the name')
value2=input('enter the marks')
d1[key2]=value2
key3=input('Enter the name')
value3=input('enter the marks')
d1[key3]=value3
key4=input('Enter the name')
value4=input('enter the marks')
d1[key4]=value4
key5=input('Enter the name')
value5=input('enter the marks')
d1[key5]=value5
key6=input('Enter the name')
value6=input('enter the marks')
d1[key6]=value6
key7=input('Enter the name')
value7=input('enter the marks')
d1[key7]=value7
key8=input('Enter the name')
value8=input('enter the marks')
d1[key8]=value8
key9=input('Enter the name')
value9=input('enter the marks')
d1[key9]=value9
key0=input('Enter the name')
value0=input('enter the marks')
d1[key0]=value0
d1_sort=sorted(d1.items(),key=lambda d1: d1[1])
print(d1_sort)