#Andy Y. Ly 
#cs_131a_python_programming
#2/15/2018


#Lists
numbersList = [2, 3, 5, 7, 11, 13, 17]
listOfStrings = ['table', 'chair', 'door', 'ceiling', 'floor']



# 1 — print out each single element of the numbers list.  Each element should be printed on its own print line.
print(*numbersList, sep = "\n")

# 2 — print out all of the elements of the strings lists that are not pieces of furniture
print(*listOfStrings[2:5], sep = "\n")


# 3 — using slicing, print out all of the elements of the number list except the element in index 0, the element in index 4 and the element in index 6
mySliceObj = slice(5,6)
print(*numbersList[1:4], *numbersList[mySliceObj], sep = "\n")

# 4 — using slicing with positive values for indices print out only the last three elements of the strings list
mySlice = slice(2,5)
print(*listOfStrings[mySlice], sep = "\n")

# 5 — using slicing with negative values for indices print out only the last three elements of the strings list
aSlice = slice(-1,-3)
print(*listOfStrings[aSlice], sep = "\n")



# 6 — using the if command and a true/false expression print out “Yes” if the number at the lowest index in the numbers list is less than the number at the highest index
length = len(numbersList) - 1 
if numbersList[0] < numbersList[length]:
  print("Yes")

  

# 7 — using the if command and true/false expressions print out “No” if the string at the lowest index in the string list is not the same string at the highest index
new_length = len(listOfStrings) - 1
if listOfStrings[0] != listOfStrings[new_length]:
      print("No")


# 8 — print out all of the characters in the string at the lowest index in reverse order.  That is, the last character of the string should be printed first, the second to last character should be printed second, the third to last character should be printed third, ... , the first character should be printed last
rev_word = listOfStrings[0]

print(rev_word[::-1])

