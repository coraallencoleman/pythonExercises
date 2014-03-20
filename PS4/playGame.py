def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    n = HAND_SIZE
    decision = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
    while decision != "e":
        if decision == "n":
            player = raw_input("Enter u to have yourself play, c to have the computer play: ")
            hand = dealHand(n)
            playHand(hand, wordList, n)
            decision = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        elif decision == "r":
            try:
                playHand(hand, wordList, n)
                decision = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
            except UnboundLocalError:
                print "You have not played a hand yet. Please play a new hand first!"
                decision = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        elif decision == "e":
            break
        else:
            print "Invalid command."
            decision = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
    else: 
        return
    
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1    
    """
    n = HAND_SIZE
    decision = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
    while decision != "e":
        if decision == "n":
            hand = dealHand(n)
            playHand(hand, wordList, n)
            decision = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        elif decision == "r":
            try:
                playHand(hand, wordList, n)
                decision = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
            except UnboundLocalError:
                print "You have not played a hand yet. Please play a new hand first!"
                decision = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        elif decision == "e":
            break
        else:
            print "Invalid command."
            decision = raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
    else: 
        return