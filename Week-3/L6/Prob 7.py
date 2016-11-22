"""""""""""""""""""""""""""""""""""""""""""""""""
# Here is the code for a function applyToEach:

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

# testList = [1, -4, 8, -9]

"""""""""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""
Prob 7a
>>> print testList[2, 3, 9, 8]
""""""""""""""""""""""""""""""""""""
applyToEach(testList, abs)

""""""""""""""""""""""""""""""""""""
Prob 7b
>>> print testList [2, -3, 9, -8]
""""""""""""""""""""""""""""""""""""
def addOne(i):
    return (i+1)
applyToEach(testList, addOne)

""""""""""""""""""""""""""""""""""""
Prob 7c
 >>> print testList [1, 16, 64, 81]
""""""""""""""""""""""""""""""""""""
def square(i):
    return (i**2)
applyToEach(testList, square)
