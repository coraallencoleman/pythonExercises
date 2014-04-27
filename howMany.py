def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    many = 0
    for key in aDict:
        many += len(aDict[key])
    return many