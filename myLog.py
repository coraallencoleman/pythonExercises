def myLog(x, b):
    '''
    b**count <= x
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    (15, 3) = 2 (16, 2) = 4
    '''
    #if b**(ans) < x:
    #    return ans
    #    return ans
    ans = 1
    if x < b:
        return ans - 1
        
    elif x == b:
        return ans

    else:
        new = x
        while new > b:
            new = new/b
            ans += 1
            if (b**ans) > x:
                return ans - 1
        return ans



from math import log    
def myLogCheck(x, b):
    if myLog(x, b) == int(log(x, b)):
        return True
    else:
        return False