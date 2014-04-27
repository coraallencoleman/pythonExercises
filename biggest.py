def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    big = 0
    biggest = None
    if aDict == {}:
        return None
    for key in aDict:
        if len(aDict[key]) > big:
            biggest = key
            big = len(aDict[key])
        if big == 0:
            biggest = key
    return biggest