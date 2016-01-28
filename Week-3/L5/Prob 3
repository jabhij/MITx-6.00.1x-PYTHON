# Declaring a Function
def recurPowerNew(base, exp):

    # Base case is when exp = 0
    if exp <= 0:
        return 1
        
    # Recursive Call
    elif exp % 2 == 0:
        return recurPowerNew(base*base, exp/2)

    return base * recurPowerNew(base, exp - 1)
