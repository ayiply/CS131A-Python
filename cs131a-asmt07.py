from functools import reduce
# reduce() is used to apply a particular function (in this case a lambda function) passed in its argument to all of the list elements of myList. 
myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
myMaxList = reduce(lambda x, y: x if (x > y) else y, myList)
print(myMaxList)
return_result = map(lambda x: x*x, myList)
print(list(return_result))