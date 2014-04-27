def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
        length = 0
    for s in aStr:
        length += 1
    return length
    '''
    if aStr == '':
        return 0
    else:
        for s in aStr[0]:
            return 1 + lenRecur(aStr[1:])
        
        