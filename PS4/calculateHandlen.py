def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    # turn a dictionary into a string, get len(string)
    #handString = ""
    #for letter in hand.values():
    #    for j in range(hand[letter]):
    #         handString += letter
    #print handString      
    count = 0
    for letter in hand.keys():
        for j in range(hand[letter]):
             count += 1 
    return count