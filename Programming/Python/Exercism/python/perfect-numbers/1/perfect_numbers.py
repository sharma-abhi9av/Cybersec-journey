def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    divisors = []
    if number < 1 :
        raise ValueError("Classification is only possible for positive integers.")
    else: 
        for a in range(1, number):
            if number % a == 0:
                divisors.append(a)
    sum_of_divisors = sum(divisors)
    if sum_of_divisors == number:
        return("perfect")
    elif sum_of_divisors > number:
        return("abundant")
    elif sum_of_divisors < number:
        return("deficient")
                
    pass
