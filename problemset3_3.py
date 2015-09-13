def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    string = secretWord
    nospace = "_" * len(string)
    string_list = list(string)
    if lettersGuessed == []:
        return nospace
    list_start = list(nospace)
    for i in lettersGuessed:
        for (n,e) in enumerate(string_list):
            if e == i:
                list_start[n] = i
    string_update = "".join(list_start)
    return string_update

print getGuessedWord('pineapple', ['y', 'l', 'u', 'h', 'x', 'i', 'g', 's', 'j', 'a'])  
    

