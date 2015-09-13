def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    full = "abcdefghijklmnopqrstuvwxyz"
    list_full = list(full)
    for i in lettersGuessed:
        for x in list_full:
            if x == i:
                list_full.remove(i)
    result_string = "".join(list_full)
    return result_string


    
print getAvailableLetters(['e', 'i', 'k', 'p', 'r', 's'])