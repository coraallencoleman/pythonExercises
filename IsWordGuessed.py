def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    Bools = []
    
    for l in secretWord:
        if l in lettersGuessed:
           Bools.append('y')
        else:
            Bools.append('n')
        
    if Bools.count('n') > 0:
        return False
    else:
        return True
     

#global = guesses
##make a counter
#guesses = 0
##each round
#guesses += 1
#
#when guess < 8
#    raw_input("Make a guess")
#    