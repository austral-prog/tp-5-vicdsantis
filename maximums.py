# Replace the "ANSWER HERE" for your answer
def max_of_two(x, y):
    """Given x and y, that are 2 numbers, return the biggest number."""
    if y < x:
        return x 

    elif y > x:
        return y 

    else:
        return x 

def max_of_three(x, y, z):
    """Given x, y and z, that are 3 numbers, return the biggest number of the three."""
    if y < x and z < x:
        return x

    elif y < z and x < z:
        return z

    else: 
        return y
