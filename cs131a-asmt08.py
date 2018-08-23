#CS131A - Python - Lab 8
import re
string1 = "A man a plan a canal panama"
string2 = "ALPHA BRAVO CHARLIE DELTA ECHO FOXTROT"
string3 = "alphabravocharliedeltaechofoxtrot"
string4 = "0123456789"
stringobject = [string1 , string2, string3, string4]
stringnames = ['string1' , 'string2', 'string3', 'string4']
x = 0
while x < len(stringnames):
  for stringobject in stringobject:
    l = re.match('[a-z]', stringobject)
    if l:
      print(stringnames[x] + "contains one or more lowercase characters.")
    else:
      print(stringnames[x]  + " does not contain one or more lowercase characters")

    u = re.match('[A-Z]', stringobject)
    if u:
      print(stringnames[x] + " contains one or more uppercase characters.")
    else:
      print(stringnames[x] + " does not contain one or more uppercase characters")

    d = re.match('[0-9]', stringobject)
    if d:
      print(stringnames[x] + " contains one or more digits.")
    else:
      print(stringnames[x] + " does not contain one or more digits")
    x+=1