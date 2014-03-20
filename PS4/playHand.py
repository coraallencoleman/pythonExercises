def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed. X
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # BEGIN PSEUDOCODE (download ps4a.py to see)# BEGIN PSEUDOCODE <-- Remove this comment when you code this function; do your coding within the pseudocode (leaving those comments in-place!)
    word = ""
    totalScore = 0     # Keep track of the total score
    displayHandStr = ""
    
    while calculateHandlen(hand) > 0:     # As long as there are still letters left in the hand:
        displayHandStr = ""
        for letter in hand.keys():
            for j in range(hand[letter]):
                displayHandStr += " " + letter 
        print "Current Hand: " + str(displayHandStr)          # Display the hand
        word = raw_input('Enter word, or a "." to indicate that you are finished: ') # Ask user for input
        if word == ".":            # If the input is a single period:
            print "Goodbye! Total score: " + str(totalScore) + " points."
            break                # End the game (break out of the loop)
        else:                   # Otherwise (the input is not a single period):
            if isValidWord(word, hand, wordList) != True: # If the word is not valid:
                print "Invalid word, please try again." # Reject invalid word (print a message followed by a blank line)
            else:                       # Otherwise (the word is valid):
                totalScore += getWordScore(word, n) 
                print repr(word) + " earned " + str(getWordScore(word, n)) + " points. Total: " + str(totalScore) + " points." # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                print
                hand = updateHand(hand, word)              # Update the hand
                
    if calculateHandlen(hand) == 0:
        print "Run out of letters. Total score: " + str(totalScore) + " points."  # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    return
    
    
    #word = ""
    #totalScore = 0     # Keep track of the total score
    #displayHandStr = ""
    #
    #while calculateHandlen(hand) > 0:     # As long as there are still letters left in the hand:
    #    for letter in hand.keys():
    #        for j in range(hand[letter]):
    #            displayHandStr += letter 
    #    print "Current Hand: " + str(displayHandStr)          # Display the hand
    #    word = raw_input('Enter word, or a "." to indicate that you are finished: ') # Ask user for input
    #    if word == ".":            # If the input is a single period:
    #        break                # End the game (break out of the loop)
    #    else:                   # Otherwise (the input is not a single period):
    #        if isValidWord(word, hand, wordList) != True: # If the word is not valid:
    #            print "That is not a valid word. Please choose another word" # Reject invalid word (print a message followed by a blank line)
    #        else:                       # Otherwise (the word is valid):
    #            totalScore += getWordScore(word, n) 
    #            print word + "earned " + str(getWordScore(word, n)) + " points. Total: " + str(totalScore) + " points." # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
    #            updateHand(hand, word)              # Update the hand
    #            
    #return "Run out of letters. Total score: " + str(totalScore) + "points."  # Game is over (user entered a '.' or ran out of letters), so tell user the total score
