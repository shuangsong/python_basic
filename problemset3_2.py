# write a function that if all char in string , return true, else return false:
def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    if lettersGuessed == []:
        return False
    point = 0
    for i in lettersGuessed:
        if i in secretWord: 
            point += 1
    if point >= len(secretWord):
        return True
    else: 
        return False  
    
print isWordGuessed('durian', ['h', 'a', 'c', 'd', 'i', 'm', 'n', 'r', 't', 'u'])