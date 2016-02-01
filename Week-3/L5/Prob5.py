# Declaring a Function
def gcdRecur(a, b):
   
    # Here comes the Recursive call
    # The Base Case
    if (b == 0):
       return a
       
    # Making a Recursive Call
    else:
       return gcdRecur(b, a % b)
