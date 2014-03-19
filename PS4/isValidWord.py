WORDLIST_FILENAME = "H:/PS4/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    newHand = hand.copy()
    wordDict = getFrequencyDict(word)
    if (word in wordList and len(word) > 0):
        try:
            for key in wordDict:
                if wordDict[key] > newHand[key]:
                    return False
                    break
            return True
        except KeyError:
            return False
    else:
        return False
    
    #try:
    #    if word in wordList:
    #        for key in wordDict:
    #            for key in range(wordDict[key]):
    #                if newHand[key] > 0:
    #                    newHand[key] -= 1
    #                    print newHand
    #                else:
    #                    print False
    #                    break
    #        return True
    #    else:
    #        return False
    #except KeyError:
    #    return False
    
    #if word in wordList:
    #    
    #    for l in word:
    #        if l in newHand.keys():
    #            print True
            #    if newHand[l] > 0:
            #        newHand[l] -= 1
            #    else:
            #        print False
            #else:
            #    print False
            #else:
            #    print False       
    #else:
    #    False
    #newHand = hand.copy()
    #for l in word:
    #    newHand[l] -= 1
    #return newHand