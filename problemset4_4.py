#Hand Length 
hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}   
def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    total = 0
    copy = hand.copy()
    for k in copy.values():
        total += k
    return total
 
print calculateHandlen(hand)



