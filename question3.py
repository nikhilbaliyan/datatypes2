from functools import reduce
list1 = [10, 10, 10]
list2 = [4, 5, 5]
result1 = reduce((lambda x, y: x * y), list1)
result2 = reduce((lambda x, y: x * y), list2)
print(result1)
print(result2)
