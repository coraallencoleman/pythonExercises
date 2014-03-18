def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    Bools = []
    
    for l in secretWord:
        if l in lettersGuessed:
           Bools.append(l + " ")
        else:
            Bools.append('_ ')
    get = ""
    for n in Bools:
        get += n
    return get
    #if n == '_':
        #    get += "_ "
        #else:
        #    get += l