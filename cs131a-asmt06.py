A = [1,2,3,4,5]
B = [2,4,6,8,10]

I = [-1, 0, 1, 2]
R = [2.7818, 0.0, -3.14159]

S = [item*7 for item in A]
print(S)
Plus = [A[i] + B[i] for i in range(len(A)) ]
print(Plus)
Even = [A[j] for j in range(len(A))  if (A[j]%2 == 0)]
print(Even)
#Create empty list NonNeg, then parse through list I and R for integers greater than or equal to zero. isinstance() checks if datatype is a type integer. Subsequent conditonal statement checks if value is greater than or equal to zero.
NonNeg = []
for k in I:
  if (isinstance(k, int) == True):
    if k >= 0:
        NonNeg.append(k)
for p in R:
  if (isinstance(p, int) == True):
    if p >= 0:
        NonNeg.append(p)
print(NonNeg)