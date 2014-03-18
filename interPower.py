def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0.0:
        return 1.0
    else: 
        result = 1.0
        while exp > 0.0:
            result *= base
            exp -= 1.0
        return result