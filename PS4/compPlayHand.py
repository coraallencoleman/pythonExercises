def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # TO DO ... <-- Remove this comment when you code this function
    
    totalScore = 0     # Keep track of the total score
    displayHandStr = ""
    
    while calculateHandlen(hand) > 0:     # As long as there are still letters left in the hand:
        displayHandStr = ""
        for letter in hand.keys():
            for j in range(hand[letter]):
                displayHandStr += " " + letter 
        print "Current Hand: " + str(displayHandStr)          # Display the hand
        if word != None:
            word = compChooseWord(hand, wordList, n)
        else:
            print "Total score: " + str(totalScore) + " points."
            break
        print repr(word) + " earned " + str(getWordScore(word, n)) + " points. Total: " + str(totalScore) + " points." # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
        hand = updateHand(hand, word)              # Update the hand
    