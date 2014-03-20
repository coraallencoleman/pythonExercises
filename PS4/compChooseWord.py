def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    maxScore = 0 # Create a new variable to store the maximum score seen so far (initially 0)

    bestWord = "" # Create a new variable to store the best word seen so far (initially None)  
    
    for word in wordList: # For each word in the wordList
        if isValidWord(word, hand, wordList) == True: # If you can construct the word from your hand
            wordScore = getWordScore(word, n)  # Find out how much making that word is worth # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
            if wordScore > maxScore:    # If the score for that word is higher than your best score
                bestWord = word
                maxScore = getWordScore(bestWord, n) # Update your best score, and best word accordingly
    return bestWord # return the best word you found.
            
           

            

                


    

