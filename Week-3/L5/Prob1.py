# Defining a Function
def iterPower(base, exp):

    # Making an Iterative Call
    result = 1
    while exp > 0:
        result *= base
        exp -= 1
        
    return result
