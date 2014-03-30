def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    #if len(s1) < len(s2):
    #    for item in range(len(s1)):
    newStr = ''
    if len(s1) == len(s2):
        for item in range(len(s1)):
            newStr += s1[item] + s2[item]
        return newStr
    elif len(s1) > len(s2):
        for item in range(len(s2)):
            newStr += s1[item] + s2[item]
        newStr += s1[len(s2):]
        return newStr  
    elif len(s1) < len(s2):
        for item in range(len(s1)):
            newStr += s1[item] + s2[item]
        newStr += s2[len(s1):]
        return newStr    
            