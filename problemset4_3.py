hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}    

#Valid Words 
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    copy = hand.copy()
    for i in word:
        if i in copy.keys() and copy[i] >= 1:
            copy[i] -= 1
            return True
        else:
            return False
    if word in wordList:
        return True
    else:
        return False
    

print isValidWord("hello", hand, "abcdefghhi")
                          
    

















