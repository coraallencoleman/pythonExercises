def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''    
    import string
    AvailableLetters = []
    for n in string.ascii_lowercase:
        AvailableLetters += n        
        
    for n in lettersGuessed:
        if n in string.ascii_lowercase:
            AvailableLetters.remove(n)
    return ''.join(AvailableLetters)


