import math
pi = math.pi

def add(a, b = pi):
    """takes two numbers and returns their sum 
and a list containing both numbers in sorted order. 
The second number defaults to pi if it is not provided."""
    print(f' {a=} {b=}')
    sum = a+b
    numbers = [a,b]
    return sum,sorted(numbers)

answer = add(6)
print(answer)

import math
pi = math.pi

def add(a, b = pi,verbose = False):
    """Prints out the parameters and results of the function
 but only if an optional parameter called 'verbose' is True."""
    sum = a+b
    numbers = [a,b]
    numbers = sorted(numbers)
    if verbose == True:
      print(sum, numbers)
    return sum, numbers

answer = add(6,verbose=True)
print(answer)
     

    #Test Code runs unless you are importing me!
if __name__ == '__main__':
    add(6)
    add(6, verbose=True)