#CS 131A Lab 3 - Spring 2018
#Andy Y. Ly
import random
flip_amt = int(input('Enter number of tosses to perform: '))
count = 0

while True:
  if count != flip_amt:
    RNG = random.randint(0,1)
    if RNG == 1:
        result = "Heads"
    if RNG == 0:
        result = "Tails"
    print(result)
    count = count + 1
  