def square(number):
    n = number
    grains = 2 ** (n-1)
    if number >= 1 and number <= 64:
        return grains
    else :
      raise ValueError("square must be between 1 and 64")
    pass
    

def total():
    # We can use G.P. to calculate. And represent powers by **, for ex- 2**3 => 2*2*2 
    # for GP the formula to calculate the sum of all terms is a(r^n -1) / r-1
    # r is ratio for second term by first, which is 2 here.
    r = 2
    a = 1 # a is starting term which is 1.
    # total_grains = (a * (r**n - 1)) / (r-1)
    total_grains = (2 ** 64) - 1 
    return total_grains
    pass
